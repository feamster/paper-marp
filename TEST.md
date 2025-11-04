# Quick Test

To verify the workflow works, run this test:

```bash
# From any directory, tell Claude:
Make me a marp presentation from https://github.com/synwww/consolidation-paper-2023
Output to: /tmp/test-paper-marp
```

Expected result:
```
/tmp/test-paper-marp/
├── figures/                      # 6 PNG files
├── dns-consolidation.md          # ~3KB markdown
└── dns-consolidation.pdf         # ~740KB PDF
```

The cloned repo should be automatically removed.

## What to Check

1. ✅ PDF opens automatically
2. ✅ 17 slides total
3. ✅ Authors: "Synthia Wang, Kyle MacMillan, Brennan Schaffner, Nick Feamster, Marshini Chetty"
4. ✅ Real findings: "Cloudflare and Amazon each host over 30%..."
5. ✅ 6 figures (pipeline + 5 consolidation charts)
6. ✅ No cloned repo directory left behind

## Cleanup After Test

```bash
rm -rf /tmp/test-paper-marp
```
