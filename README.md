# Paper to Marp Presentation Automation

Fully automated workflow for generating Marp presentations from academic paper repositories using Claude.

## Overview

This workflow uses Claude to read paper sources, intelligently select figures, and generate high-quality presentation slides with real content extracted from the paper - no manual intervention required.

## Prerequisites

- Python 3 with PyMuPDF: `pip3 install PyMuPDF`
- Node.js with Marp CLI: `npm install -g @marp-team/marp-cli`
- Git
- Claude Code (you're using it now!)

## Usage

You can run this from **anywhere** - the workflow is not directory-dependent.

### In Claude Code

Simply tell Claude:

```
Make me a marp presentation from this paper repo: https://github.com/USER/REPO
Output to: ~/talks/my-talk
```

or

```
Make me a marp presentation from https://github.com/synwww/consolidation-paper-2023
Put it in ~/Dropbox/Talks/censorship
```

That's it! Claude will:
1. Clone the repository
2. Read the paper LaTeX sources
3. Intelligently select 4-8 key figures
4. Convert figures to PNG
5. Generate presentation with real content from the paper
6. Compile to PDF
7. Open the result
8. Clean up (remove cloned repo)

### What Claude Does (Automatically)

Following the instructions in `CLAUDE_WORKFLOW.md`, Claude will:

- **Read paper sources** - Extract title, findings, methodology from .tex files
- **Smart figure selection** - Pick 4-8 most important figures, avoid redundant regional variants
- **Real content** - Use actual numbers, findings, and conclusions from the paper
- **Proper authors** - Get real author names (may look up arXiv if needed)
- **Clean presentation** - Basic markdown, 700px figures, 3-4 bullets per slide

## Files in This Directory

- **`CLAUDE_WORKFLOW.md`** - Complete step-by-step instructions for Claude (the main file)
- **`README.md`** - This file (for humans)
- **`generate_presentation.py`** - Optional helper script (Claude can do everything without it)
- **`config.json`** - Configuration defaults

## Output Structure

After running, you'll have:

```
<output-directory>/
├── figures/                  # Converted PNG figures
├── <presentation-name>.md    # Marp markdown source
└── <presentation-name>.pdf   # Final presentation
```

Note: The cloned repository is automatically removed after figure conversion.

## Key Features

### Intelligent Figure Selection
Claude reads paper content and figure names to select:
- Pipeline/methodology diagrams
- Main result charts
- Key consolidation/comparison figures
- **Avoids:** Regional variants, redundant figures, non-essential plots

### Real Content Extraction
- Extracts actual findings with specific numbers from paper
- Uses real conclusions and implications
- No placeholder text or "[EDIT: ...]" templates

### Simple Formatting
- Clean, basic markdown (no complex HTML/CSS)
- 700px figure width (works well for most projectors)
- 3-4 bullets per slide
- One figure per slide

## Example

```
User: Make me a marp presentation from https://github.com/synwww/consolidation-paper-2023
      Output to: ~/talks/consolidation-talk

Claude:
[Clones repo]
[Reads paper.tex, abstract.tex, introduction.tex]
[Selects 6 key figures: pipeline, as_count, ns_as_stacked_org, ns_as_stacked, index_stacked_org, as_stacked]
[Converts PDFs to PNGs]
[Generates presentation with real findings: "Cloudflare and Amazon each host over 30%..."]
[Compiles to PDF]
[Opens result]
```

Result: 17-slide presentation with actual content, proper authors, and key figures.

## Customization

If you want to modify the presentation structure or style:
1. Edit the markdown template in `CLAUDE_WORKFLOW.md` (Step 6)
2. Change figure width (currently 700px)
3. Modify slide structure (currently: intro → methods → findings → figures → implications → conclusions)

## Troubleshooting

### "Authors are wrong"
- Paper .tex files often have placeholder authors
- Claude will try to look up real authors from arXiv or published version
- You can manually provide: "Make presentation, authors are: John Doe, Jane Smith"

### "Too many/wrong figures"
- Claude selects based on paper content and figure names
- You can guide: "Make presentation but only use the main consolidation figures, skip regional breakdowns"

### "Content is generic"
- Should not happen! Claude reads actual paper content
- If it does, ask Claude to re-read the paper sections and regenerate

## Advanced Usage

If you want to use the helper script directly:

```bash
cd ~/src/paper-marp

# This is just for manual testing - Claude does all this automatically!
python3 generate_presentation.py --repo <URL> --output <DIR> --list-figures
```

But normally you don't need to do this - just tell Claude what you want!

## Location

This directory can be anywhere on your system. The workflow is self-contained and location-independent.

- Current location: `~/src/paper-marp/`
- Can be moved anywhere
- Claude follows `CLAUDE_WORKFLOW.md` regardless of location

## License

Public domain / Use however you want
