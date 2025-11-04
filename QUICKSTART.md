# Quick Start Guide

## Setup (One Time)

```bash
# Install dependencies
pip3 install PyMuPDF
npm install -g @marp-team/marp-cli
```

## Usage (Every Time)

### Option 1: Use Claude (Recommended)

Open Claude Code from **any directory** and say:

```
Make me a marp presentation from https://github.com/USER/REPO
Output to: ~/talks/my-talk
```

Claude will automatically:
- Clone repo
- Read paper
- Select figures
- Generate presentation
- Open PDF

### Option 2: Manual (If you want control)

```bash
# 1. Clone paper repo
cd ~/talks/my-talk
git clone https://github.com/USER/REPO

# 2. Ask Claude to analyze it
# Open Claude and say: "Read REPO/paper.tex and sections/*.tex,
# tell me the key findings and which figures to use"

# 3. Follow remaining steps in CLAUDE_WORKFLOW.md
```

## That's It!

The workflow is location-independent. You can:
- Run from any directory
- Clone repos anywhere
- Output presentations anywhere

Claude follows `CLAUDE_WORKFLOW.md` automatically when you ask for a presentation.
