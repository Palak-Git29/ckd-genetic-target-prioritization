# CKD Genetic Target Prioritization

## Project Overview

A reproducible bioinformatics project exploring genetic associations with kidney function and prioritizing candidate genes for further investigation in chronic kidney disease (CKD) research.

The project analyzes public genome-wide association study (GWAS) summary statistics, performs genomic quality checks, visualizes association patterns, and connects variants to nearby genes.

## Research Questions

- Which genetic variants are associated with estimated glomerular filtration rate (eGFR)?
- How can variant-level evidence be connected to candidate genes?
- Which genes warrant further investigation, and what are the limitations of positional prioritization?

## Data Source

**Wuttke et al. (2019)** — *A catalog of genetic loci associated with kidney function from analyses of a million individuals.*

- Publication: https://doi.org/10.1038/s41588-019-0407-x
- Phenotype: creatinine-derived eGFR
- Genome assembly: GRCh37
- Data type: GWAS summary statistics

**Important:** Creatinine-derived eGFR associations may reflect creatinine metabolism as well as kidney filtration. These associations are not equivalent to associations with a clinical CKD diagnosis.

## Workflow and Current Results

1. **GWAS summary statistics:** Processed 8,276,454 variant records and identified 26,442 variants meeting the significance threshold of P < 5 × 10⁻⁸.
2. **Quality checks:** Validated variant coordinates and gene annotation records during variant-to-gene overlap analysis.
3. **Visualization:** Generated chromosome-level summaries and a Manhattan plot of significant associations.
4. **Variant-to-gene mapping:** Compared significant variant positions with annotated gene boundaries.
5. **Regional analysis:** Extracted 339 variants within ±100 kb of lead variant rs1145077 on chromosome 15.
6. **Candidate-gene review:** Examined nearby genes and documented the evidence and limitations for prioritizing candidates.

### Regional Association Finding

The lead variant identified in the selected region is **rs1145077**, at chromosome 15 position 45,683,795 (GRCh37), with P = 6.85 × 10⁻¹⁴².

The variant overlaps the annotated boundaries of **GATM**, making it a strong positional candidate for follow-up. **SPATA5L1** is another candidate for further investigation based on its proximity and previously reported region-level evidence.

These findings do not establish either gene as causal.

## Repository Structure

- `data/raw/` — source GWAS statistics and gene annotations
- `data/processed/` — intermediate analysis outputs
- `src/` — Python analysis scripts
- `results/figures/` — generated visualizations
- `docs/` — candidate-gene evidence and methodological notes
- `notebooks/` — exploratory analysis
- `tests/` — project tests

Raw and generated data files are excluded from Git where configured in `.gitignore`. Follow the source publication and data-provider terms when obtaining the data.

## Tools

Python, pandas, NumPy, Matplotlib, Git, Linux, and Ubuntu on Windows Subsystem for Linux (WSL).

## Limitations and Next Steps

- Nearby variants may be correlated through linkage disequilibrium (LD); they should not be treated as independent signals without further analysis.
- Positional overlap does not prove that a variant regulates or affects a particular gene.
- Formal fine-mapping requires appropriate linkage disequilibrium information and statistical analysis.
- Candidate-gene prioritization should be strengthened with fine-mapping, kidney-relevant expression quantitative trait loci (eQTLs), colocalization, and independent phenotype evidence.
- Creatinine-derived eGFR findings should be compared with complementary kidney-function phenotypes where suitable data are available.

## Project Status

**Completed:** Initial GWAS processing, significance filtering, chromosome-level visualization, variant-to-gene overlap analysis, regional extraction, and preliminary candidate-gene evidence review.

**Planned:** Formal fine-mapping, integration of functional evidence, and improved candidate-gene prioritization.


## Candidate-gene evidence and data validation

The project includes two structured reports for the chromosome 15 eGFR association region:

- `reports/candidate_gene_prioritization.csv` summarizes four candidate genes, their distances from the lead variant, current priorities, and key limitations.
- `reports/variant_gene_evidence.csv` separates positional evidence from genetic and functional evidence, explicitly marking evidence that has not yet been assessed.

GATM has the strongest positional evidence because the lead variant rs1145077 falls within its annotated gene boundaries. SPATA5L1 is a follow-up candidate based on evidence described in the literature review. These assessments do not establish a causal gene.

### Data validation and tests

The validation script checks the candidate-gene prioritization table:

```bash
python src/validate_candidate_genes.py
```

Run the automated tests with:

```bash
python -m pytest -v
```

The test suite checks gene-name uniqueness, non-negative distances, documented evidence fields, expected gene coverage, and completeness of the variant-to-gene evidence table.
