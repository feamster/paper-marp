# Paper-to-Marp Workflow Summary

## What This Is

A fully automated workflow for generating Marp presentations from academic paper repositories. Claude reads the paper, selects figures intelligently, and generates slides with real content.

## Complete File List

```
~/src/paper-marp/
├── README.md                    # Complete documentation (start here)
├── QUICKSTART.md               # 2-minute quick start
├── CLAUDE_WORKFLOW.md          # Step-by-step instructions for Claude
├── CLAUDE_INSTRUCTIONS.md      # Detailed implementation notes
├── generate_presentation.py    # Optional helper script
├── config.json                 # Configuration defaults
├── .claude-workflow            # Auto-detection for Claude
└── SUMMARY.md                  # This file
```

## How To Use

From **anywhere**, tell Claude:

```
Make me a marp presentation from https://github.com/USER/REPO
Output to: ~/talks/my-talk
```

Claude automatically follows `CLAUDE_WORKFLOW.md` to:
1. Clone repo
2. Read paper sources (.tex files)
3. Select 4-8 key figures (avoids redundancy)
4. Convert PDFs to PNGs
5. Generate markdown with real content
6. Compile to PDF
7. Open result
8. Clean up (remove cloned repo)

## Key Features

✅ **Fully automated** - No manual figure selection or content entry
✅ **Intelligent** - Reads paper to extract real findings
✅ **Smart figure selection** - Picks important figures, skips redundant ones
✅ **Location independent** - Run from any directory
✅ **Real content** - Uses actual numbers and conclusions from paper

## Example Output

From consolidation paper repo:
- 17 slides total
- 6 carefully selected figures
- Real findings: "Cloudflare and Amazon each host over 30%..."
- Proper authors: "Synthia Wang, Kyle MacMillan, Brennan Schaffner, Nick Feamster, Marshini Chetty"
- Clean, professional formatting

## Dependencies

- Python 3 + PyMuPDF
- Node.js + Marp CLI
- Git
- Claude Code

## Created

November 3, 2025
Session with Nick Feamster
Testing paper: arXiv:2110.15345 (DNS/Web Hosting Consolidation)
