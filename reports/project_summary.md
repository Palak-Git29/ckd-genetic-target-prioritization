
# CKD Genetic Target Prioritization

## Project overview

This project analyzes genetic associations with creatinine-derived estimated glomerular filtration rate (eGFR) to investigate a genomic region and prioritize nearby candidate genes for further study.

**GWAS source:** Wuttke et al. (2019), *Nature Genetics*  
https://doi.org/10.1038/s41588-019-0407-x

## Research question

Can GWAS association signals and gene-level evidence be combined into a transparent, reproducible framework for prioritizing candidate genes relevant to kidney function?

## Key findings

- The source dataset contains 8,276,454 variant records.
- 26,442 variants meet the genome-wide significance threshold of P < 5 × 10⁻⁸.
- The lead variant examined is rs1145077 on chromosome 15 (GRCh37 position 45,683,795; P = 6.85 × 10⁻¹⁴²).
- The selected region spans 100 kb on either side of the lead variant and contains 339 variants.
- GATM has the strongest positional evidence among the four prioritized candidates because the lead variant falls within its annotated gene boundaries.
- SPATA5L1 is a follow-up candidate based on evidence discussed in the project literature review.
- C15orf48 and SLC30A4 remain provisional candidates.

## Candidate-gene prioritization

| Gene | Distance from lead variant | Current assessment |
|---|---:|---|
| GATM | 0 bp; variant overlaps gene | High positional priority |
| SPATA5L1 | 10,734 bp | Follow-up candidate |
| C15orf48 | 38,932 bp | Provisional |
| SLC30A4 | 88,014 bp | Provisional |

## Interpretation and limitations

The source GWAS examines creatinine-derived eGFR, not clinical CKD diagnosis directly. Because GATM is involved in creatine production, the association may partly reflect creatinine metabolism rather than kidney filtration alone.

Positional overlap and proximity do not prove that a gene causes the association. Nearby variants may be correlated through linkage disequilibrium, and this analysis does not establish a causal variant or gene.

Further work should include fine-mapping, kidney-relevant eQTL and colocalization analyses, and comparison with cystatin C-based eGFR, blood urea nitrogen, measured GFR, or clinical CKD outcomes.

## Reproducibility

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run candidate-gene validation:

```bash
python src/validate_candidate_genes.py
```

Run automated tests:

```bash
python -m pytest -v
```

## Outputs

- `reports/candidate_gene_prioritization.csv` — candidate genes, priorities, and limitations.
- `reports/variant_gene_evidence.csv` — structured positional, genetic, and functional evidence.
- `results/figures/lead_region_association.png` — regional association plot with nearby candidate genes.
