# Paper-to-Marp Presentation Generator

Automated workflow for generating Marp presentations from academic paper repositories using Claude Code.

## What This Does

Give Claude a GitHub URL of a paper repository, and it automatically:
- Clones the repository
- Reads the paper LaTeX sources
- Intelligently selects 4-8 key figures
- Converts PDF figures to PNG
- Generates presentation slides with real content from the paper
- Compiles to PDF
- Cleans up temporary files

## Quick Start

### Prerequisites

```bash
# Install dependencies
pip3 install PyMuPDF
npm install -g @marp-team/marp-cli
```

### Usage

From **anywhere** (this is location-independent), tell Claude Code:

```
Make me a marp presentation from https://github.com/USER/REPO
Output to: ~/talks/my-talk
```

That's it! Claude will handle everything automatically.

### Example

```
Make me a marp presentation from https://github.com/synwww/consolidation-paper-2023
Output to: ~/talks/consolidation-talk
```

## How It Works

The workflow (`/generate` slash command) automatically:

1. **Clones the repository** to a temporary location
2. **Reads paper sources** - Extracts title, findings, and methodology from `.tex` files
3. **Lists available figures** - Finds PDFs in `graphics/` or `figures/` directory
4. **Selects key figures** - Intelligently picks 4-8 important figures, avoiding redundant regional variants
5. **Converts to PNG** - Uses PyMuPDF to convert PDF figures at 3x resolution
6. **Generates presentation** - Creates Marp markdown with real content from the paper
7. **Compiles to PDF** - Uses Marp CLI to generate final presentation
8. **Opens result** - Displays the PDF
9. **Cleans up** - Removes cloned repository, keeping only figures and presentation

## Output Structure

```
<output-directory>/
├── figures/                  # Converted PNG figures
├── <presentation-name>.md    # Marp markdown source
└── <presentation-name>.pdf   # Final presentation
```

## Style Guidelines

Presentations automatically follow these conventions:
- Capitalize "Internet" (never lowercase)
- Use "Method" not "Methodology"
- Use "Summary" instead of "Conclusions"
- Include QR code to feamster.github.io on final slide
- 700px figure width
- 3-4 bullets per slide
- One figure per slide

## Manual Script Usage

If you prefer to use the Python script directly:

```bash
# List available figures
python3 generate_presentation.py --repo URL --output DIR --list-figures

# Generate with auto-selected figures
python3 generate_presentation.py --repo URL --output DIR

# Generate with specific figures
python3 generate_presentation.py --repo URL --output DIR --figures pipeline.pdf results.pdf
```

## Configuration

Edit `config.json` to customize:
- Default output directory
- Figure width
- QR code settings
- Marp theme

## Example Output

From the consolidation paper (arXiv:2110.15345):
- 17 slides total
- 6 carefully selected figures
- Real findings: "Cloudflare and Amazon each host over 30%..."
- Proper authors extracted from paper
- Clean, professional formatting

## Troubleshooting

**Figures not showing in PDF:**
- Ensure PNG conversion completed successfully
- Check that `--allow-local-files` flag is used with Marp

**Wrong or placeholder authors:**
- Script attempts to extract real authors from arXiv or published version
- You can manually specify: "Make presentation, authors are: John Doe, Jane Smith"

**Too many figures selected:**
- Guide Claude: "Use only main consolidation figures, skip regional breakdowns"

## Requirements

- Python 3.x
- Node.js
- Git
- Claude Code

## License

Public domain - use however you want.
