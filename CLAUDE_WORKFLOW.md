# Claude Workflow: Fully Automated Marp Presentation Generation

## User Request Format
```
User: Make me a marp presentation from this paper repo: <GITHUB_URL>
      Output to: <OUTPUT_DIR>
```

## Style Guidelines

**IMPORTANT: Apply these style rules to ALL presentations:**

1. **Capitalize "Internet" always** - Never use lowercase "internet"
2. **Use "Method" not "Methodology"** - Methodology slide should be titled "Method"
3. **Use "Summary" instead of "Conclusions"** - Final content slide should be titled "Summary"
4. **Add QR code on final slide** - Generate QR code for `feamster.github.io` and place on Thank You slide
   - QR code width: 200px
   - Include text: **feamster.github.io** below QR code

## Automated Workflow (Claude Does Everything)

### Step 1: Clone Repository
```bash
cd <OUTPUT_DIR>
git clone <GITHUB_URL>
```

### Step 2: Read Paper Content
Read the paper source files to understand content:
- Read `paper.tex` or `main.tex` for title
- Read `sections/abstract.tex` for abstract
- Read `sections/introduction.tex` for context and key findings
- Identify actual authors (will need to look at arXiv or published version if not in tex)

### Step 3: List Available Figures
```bash
ls <REPO_DIR>/graphics/
```
or
```bash
ls <REPO_DIR>/figures/
```

### Step 4: Analyze Paper and Select Figures
Based on reading the paper content:

**Determine key figures by looking for:**
- Pipeline/methodology diagram (usually `pipeline.pdf` or similar)
- Main results (look for terms like "stacked", "comparison", "results" in filenames)
- Avoid regional variants (e.g., if there's `index_stacked.pdf` and `tokyo_index_stacked.pdf`, just use the main one)
- Typically need 4-8 figures total

**For this consolidation paper example:**
- `pipeline.drawio.pdf` - methodology
- `as_count.pdf` - shows concentration
- `ns_as_stacked_org.pdf` - DNS nameserver consolidation by org
- `ns_as_stacked.pdf` - DNS nameserver consolidation by AS
- `index_stacked_org.pdf` - web hosting consolidation by org
- `as_stacked.pdf` - web hosting consolidation by AS

### Step 5: Convert Selected Figures
Use Python to convert PDFs to PNGs:

```python
import fitz
import os

graphics_dir = "<REPO_DIR>/graphics"
output_dir = "<OUTPUT_DIR>/figures"
os.makedirs(output_dir, exist_ok=True)

figures_to_convert = [
    "pipeline.drawio.pdf",
    "as_count.pdf",
    # ... selected figures
]

for pdf_file in figures_to_convert:
    pdf_path = os.path.join(graphics_dir, pdf_file)
    png_file = pdf_file.replace('.pdf', '.png')
    png_path = os.path.join(output_dir, png_file)

    doc = fitz.open(pdf_path)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
    pix.save(png_path)
    doc.close()
```

### Step 6: Generate Presentation with Real Content
Write the markdown file with actual content extracted from the paper:

```markdown
---
marp: true
theme: default
paginate: true
---

# <Title from paper.tex>

**Authors:** <Real authors - from arXiv or published version>

**arXiv:<ID if known>**

---

## Research Question

**<Main question from introduction>**

- <Key point from paper>
- <Key point from paper>
- <Key point from paper>

---

## Method

**Dataset:** <From methods section>

**Analysis:**
- <From methods section>
- <From methods section>

---

## Key Findings: <From abstract>

**<Finding with actual numbers>:**
- <Specific data from paper>

**<Finding with actual numbers>:**
- <Specific data from paper>

---

## <Descriptive Figure Title>

![width:700px](figures/<figure>.png)

---

[Repeat for each figure]

---

## Implications

**<From paper>:**
- <Actual implications>

---

## Contributions

**<From paper>:**
- <Actual contributions>

---

## Summary

**<From discussion/conclusion>:**

1. <Actual conclusion>
2. <Actual conclusion>
3. <Actual conclusion>

---

## Thank You

**Paper:** arXiv:<ID>

Questions?
```

### Step 7: Compile to PDF
```bash
marp <presentation>.md --pdf --output <presentation>.pdf --allow-local-files
open <presentation>.pdf
```

### Step 8: Cleanup
Remove the cloned repository (no longer needed):
```bash
rm -rf <OUTPUT_DIR>/<REPO_NAME>
```

Keep only:
- `figures/` directory with converted PNGs
- `<presentation>.md` markdown source
- `<presentation>.pdf` final presentation

## Key Principles

1. **NO USER INPUT NEEDED** - Claude reads paper, selects figures, generates content
2. **REAL CONTENT** - Extract actual findings, numbers, and conclusions from paper
3. **SMART FIGURE SELECTION** - 4-8 most important figures, avoid redundancy
4. **PROPER AUTHORS** - Get real author names (may need arXiv lookup if not in tex)
5. **CLEAN UP** - Remove cloned repo after conversion, keep only figures and presentation

## Example for Consolidation Paper

**What Claude should extract:**
- Title: "Measuring the Consolidation of DNS and Web Hosting Providers"
- Authors: "Synthia Wang, Kyle MacMillan, Brennan Schaffner, Nick Feamster, Marshini Chetty"
- Key finding: "Cloudflare and Amazon hosting over 30% of domains"
- Key finding: "Top 5 organizations host 60% of index pages in Tranco top 10K"
- Figures: pipeline, main consolidation charts (6 figures total)

**What to avoid:**
- Generic placeholders like "[EDIT: ...]"
- All 24 figures from repo
- Regional variants (va_, tokyo_, india_, etc.)
- Template authors like "Paper #150"
