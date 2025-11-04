# Claude Instructions: Generate Marp Presentation from Academic Paper

## Task Overview
Generate a Marp presentation summarizing an academic paper with actual figures from the paper's repository.

## Input Requirements
1. **arXiv URL** - Paper identifier (e.g., https://arxiv.org/abs/2110.15345)
2. **GitHub Repository** - Paper's source repository containing figures
3. **Output Directory** - Where to save the presentation

## Step-by-Step Process

### 1. Fetch Paper Information
```
Use WebFetch to get paper details from arXiv URL:
- Title
- Authors
- Main research questions
- Methodology
- Key findings
- Contributions
- Conclusions
```

### 2. Clone Repository
```bash
cd <output_directory>
git clone <github_repo_url>
```

### 3. Identify Key Figures
```bash
# List figures in the repo
find <repo_dir>/graphics -name "*.pdf" -o -name "*.png"

# Key figures typically include:
# - pipeline/methodology diagram
# - Main results charts (stacked bars, line graphs)
# - Consolidation/concentration metrics
# - Geographic distribution (if applicable)
```

### 4. Convert PDF Figures to PNG
```python
# Use PyMuPDF to convert PDF figures to PNG at 3x resolution
import fitz
import os

graphics_dir = "<repo>/graphics"
output_dir = "<output>/figures"
os.makedirs(output_dir, exist_ok=True)

# List of key figures to convert
figures_to_convert = [
    "pipeline.pdf",
    "main_results.pdf",
    # ... add others
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

### 5. Generate Marp Presentation Structure

**Template:**
```markdown
---
marp: true
theme: default
paginate: true
---

# <Paper Title>

**Authors:** <Author List>

**arXiv:<ID>**

---

## Research Question

**<Main Question>**

- <Key point 1>
- <Key point 2>
- <Key point 3>

---

## Methodology

**Dataset:** <Description>

**Analysis:**
- <Method 1>
- <Method 2>
- <Method 3>

---

## Key Findings: <Summary Title>

**<Key finding 1 title>:**
- <Detail>
- <Detail>

**<Key finding 2 title>:**
- <List items>

---

## <Figure Title (no "Figure N:")>

![width:700px](figures/<figure_name>.png)

---

[Repeat for each figure]

---

## Geographic Distribution

[If applicable]

---

## Implications

**<Category 1>:**
- <Point 1>
- <Point 2>

**<Category 2>:**
- <Point 1>
- <Point 2>

---

## Contributions

**<Summary>:**
- <Contribution 1>
- <Contribution 2>

**Impact:**
- <Impact 1>
- <Impact 2>

---

## Conclusions

**<Summary statement>:**

1. <Conclusion 1>
2. <Conclusion 2>
3. <Conclusion 3>

**Future work needed on:**
- <Area 1>
- <Area 2>

---

## Thank You

**Paper:** arXiv:<ID>

Questions?
```

### 6. Compile to PDF

```bash
marp "<presentation>.md" --pdf --output "<presentation>.pdf" --allow-local-files
open "<presentation>.pdf"
```

### 7. Clean Up Temporary Files

```bash
# Remove conversion scripts and intermediate files
rm -f convert_figures.py extract_*.py paper-*.pdf
```

## Design Guidelines

1. **Keep it simple** - Use basic markdown, no complex HTML/CSS
2. **Figure sizing** - 700px width works well
3. **No figure numbers in titles** - Use descriptive titles only
4. **One figure per slide** - Don't crowd slides
5. **Bullet points** - Keep to 3-4 per slide
6. **Clean structure** - Title → Content → Figures → Implications → Conclusions

## Common Figures to Include

For infrastructure/measurement papers:
- Measurement pipeline/architecture
- Market share/concentration charts
- Time series or ranking plots
- Geographic distribution maps
- Comparison charts

For systems papers:
- Architecture diagrams
- Performance benchmarks
- Scalability charts
- Comparison with baselines

## Troubleshooting

- **Figures not showing**: Ensure PNG conversion completed, use `--allow-local-files` flag
- **Layout issues**: Stick to basic markdown, avoid HTML divs
- **Size problems**: Adjust figure width (try 600px, 700px, or 800px)
- **Missing figures**: Check graphics directory path, verify PDF exists

## Example Command Sequence

```bash
# 1. Fetch paper info via WebFetch
WebFetch(url="https://arxiv.org/abs/2110.15345", prompt="summarize paper")

# 2. Clone repo
git clone https://github.com/synwww/consolidation-paper-2023

# 3. Create and run conversion script
python3 convert_figures.py

# 4. Create presentation markdown
# (Write the .md file)

# 5. Generate PDF
marp presentation.md --pdf --allow-local-files

# 6. Clean up
rm convert_figures.py
```
