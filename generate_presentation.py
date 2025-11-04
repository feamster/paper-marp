#!/usr/bin/env python3
"""
Generate Marp presentation from academic paper repository.
This is a helper script - it should be invoked BY Claude, not standalone.
Claude will handle the paper analysis and content generation.
"""

import argparse
import os
import sys
import subprocess
import re
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF not installed. Run: pip3 install PyMuPDF")
    sys.exit(1)


def clone_repo(repo_url, output_dir):
    """Clone the paper repository."""
    repo_name = repo_url.rstrip('/').split('/')[-1]
    repo_path = os.path.join(output_dir, repo_name)

    if os.path.exists(repo_path):
        print(f"Repository already exists: {repo_path}")
        return repo_path, repo_name

    print(f"Cloning repository: {repo_url}")
    subprocess.run(['git', 'clone', repo_url], cwd=output_dir, check=True)
    return repo_path, repo_name


def find_graphics_dir(repo_path):
    """Find the graphics/figures directory in the repository."""
    possible_dirs = ['graphics', 'figures', 'imgs', 'images', 'fig', 'plots']

    for dir_name in possible_dirs:
        graphics_path = os.path.join(repo_path, dir_name)
        if os.path.exists(graphics_path):
            print(f"Found graphics directory: {graphics_path}")
            return graphics_path

    # Try recursive search
    for root, dirs, files in os.walk(repo_path):
        for dir_name in dirs:
            if dir_name in possible_dirs:
                graphics_path = os.path.join(root, dir_name)
                print(f"Found graphics directory: {graphics_path}")
                return graphics_path

    return None


def list_available_figures(graphics_dir):
    """List all available PDF figures."""
    if not graphics_dir or not os.path.exists(graphics_dir):
        return []

    pdf_files = sorted([f for f in os.listdir(graphics_dir) if f.endswith('.pdf')])

    # Filter out common non-figure PDFs
    exclude = ['mouse.pdf', 'template.pdf', 'draft.pdf']
    pdf_files = [f for f in pdf_files if f not in exclude]

    return pdf_files


def convert_figures(graphics_dir, output_dir, figure_list=None):
    """Convert specified PDF figures to PNG format."""
    os.makedirs(output_dir, exist_ok=True)

    if figure_list is None:
        figure_list = list_available_figures(graphics_dir)

    if not figure_list:
        print("Warning: No PDF figures found to convert")
        return []

    print(f"Converting {len(figure_list)} figures...")
    converted = []
    for pdf_file in figure_list:
        pdf_path = os.path.join(graphics_dir, pdf_file)
        if not os.path.exists(pdf_path):
            print(f"  ✗ {pdf_file} not found")
            continue

        png_file = pdf_file.replace('.pdf', '.png')
        png_path = os.path.join(output_dir, png_file)

        try:
            doc = fitz.open(pdf_path)
            page = doc[0]
            # Render at 3x resolution for quality
            pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
            pix.save(png_path)
            doc.close()
            print(f"  ✓ {pdf_file} -> {png_file}")
            converted.append(png_file)
        except Exception as e:
            print(f"  ✗ Error converting {pdf_file}: {e}")

    return converted


def compile_to_pdf(markdown_path, pdf_path):
    """Compile Marp markdown to PDF."""
    print(f"Compiling presentation to PDF...")
    cmd = [
        'marp',
        markdown_path,
        '--pdf',
        '--output', pdf_path,
        '--allow-local-files'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Generated PDF: {pdf_path}")
    else:
        print(f"Error compiling PDF: {result.stderr}")
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(
        description='Helper script for generating Marp presentations. Should be invoked BY Claude.',
        epilog='This script handles repo cloning and figure conversion. Claude handles content generation.'
    )
    parser.add_argument('--repo', required=True, help='GitHub repository URL')
    parser.add_argument('--output', required=True, help='Output directory')
    parser.add_argument('--list-figures', action='store_true', help='List available figures and exit')
    parser.add_argument('--convert-figures', nargs='+', help='Convert specific figures')
    parser.add_argument('--convert-all', action='store_true', help='Convert all figures')
    parser.add_argument('--compile', help='Compile markdown file to PDF')

    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    # Clone repository
    repo_path, repo_name = clone_repo(args.repo, args.output)

    # Find graphics directory
    graphics_dir = find_graphics_dir(repo_path)

    if args.list_figures:
        if not graphics_dir:
            print("No graphics directory found")
            return
        figures = list_available_figures(graphics_dir)
        print(f"\nAvailable figures ({len(figures)}):")
        for fig in figures:
            print(f"  - {fig}")
        return

    if args.convert_all or args.convert_figures:
        if not graphics_dir:
            print("Error: No graphics directory found")
            sys.exit(1)

        figures_dir = os.path.join(args.output, 'figures')
        figure_list = args.convert_figures if args.convert_figures else None
        converted = convert_figures(graphics_dir, figures_dir, figure_list)
        print(f"\nConverted {len(converted)} figures to {figures_dir}/")

    if args.compile:
        pdf_path = args.compile.replace('.md', '.pdf')
        success = compile_to_pdf(args.compile, pdf_path)
        sys.exit(0 if success else 1)

    print("\n=== Repository Setup Complete ===")
    print(f"Repository: {repo_path}")
    print(f"Graphics: {graphics_dir or 'Not found'}")
    print("\nNext: Have Claude analyze the paper and generate presentation content")


if __name__ == '__main__':
    main()
