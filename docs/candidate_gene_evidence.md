# Candidate Gene Evidence Review

## Project context

This project investigates genetic associations with estimated glomerular filtration rate (eGFR) using summary statistics from Wuttke et al. (2019).

The lead variant selected for regional investigation is rs1145077, located on chromosome 15 at GRCh37 position 45,683,795, with a reported P-value of 6.85e-142.

A regional analysis using Ensembl GRCh37 gene annotations identified 12 gene records within a 100 kb window on either side of the lead variant.

**Important:** This dataset measures creatinine-derived eGFR associations. It is not a direct GWAS of clinical CKD diagnosis, and genetic associations with creatinine-derived eGFR do not always reflect changes in kidney filtration.

## Candidate genes

### 1. GATM

**Positional evidence**
- The lead variant rs1145077 falls within the annotated GATM gene body.
- GATM is therefore a strong positional candidate for further investigation.

**Biological evidence**
- GATM encodes glycine amidinotransferase, an enzyme involved in creatine biosynthesis.
- Genetic variation affecting creatine and creatinine production can influence serum creatinine and consequently creatinine-derived eGFR.

**Interpretation and limitations**
- Previous studies have associated this region with eGFR based on serum creatinine.
- The association may reflect creatinine metabolism rather than impaired kidney filtration.
- The positional overlap does not establish that rs1145077 is causal or that GATM is the causal gene.

**Current assessment:** Strong positional evidence; biological interpretation requires further investigation.

### 2. SPATA5L1

**Positional evidence**
- SPATA5L1 is approximately 10.7 kb from the lead variant, outside the annotated GATM gene body.

**Biological and genetic evidence**
- Previous kidney-related genetic studies have reported associations involving the GATM-SPATA5L1 region.
- A study integrating kidney expression data reported evidence supporting SPATA5L1 expression as a potential mediator of an eGFR association.
- The mechanism linking SPATA5L1 to kidney function remains incompletely understood.
- A kidney-expression analysis reported colocalization evidence for SPATA5L1 and an eGFR association signal at this broader locus.
- A 2023 transcriptome- and proteome-wide study reported no association of GATM and SPATA5L1 with cystatin C-based eGFR or blood urea nitrogen in its analyses, supporting a possible creatinine-metabolism explanation.
References:
- https://www.nature.com/articles/s41467-019-11704-w
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10291807/
**Interpretation and limitations**
- Evidence from other variants and studies cannot automatically be attributed to rs1145077.
- Fine-mapping and variant-specific regulatory evidence are needed to assess this candidate.

**Current assessment:** Important regional candidate requiring further evaluation.

### 3. C15orf48

**Positional evidence**
- C15orf48 is approximately 38.9 kb from the lead variant.

**Biological evidence**
- It is annotated as a protein-coding gene in the Ensembl GRCh37 dataset.

**Interpretation and limitations**
- Proximity and protein-coding status alone do not establish a role in kidney function.
- Independent GWAS, expression, regulatory, and functional evidence must be investigated.

**Current assessment:** Provisional candidate; insufficient evidence assessed so far.

### 4. SLC30A4

**Positional evidence**
- SLC30A4 is approximately 88.0 kb from the lead variant.

**Biological evidence**
- It is annotated as a protein-coding gene in the regional gene dataset.

**Interpretation and limitations**
- The current analysis establishes proximity, not a causal relationship with the eGFR association.
- Additional evidence is required before assigning priority.

**Current assessment:** Provisional candidate; insufficient evidence assessed so far.

## Current conclusions

1. GATM has the strongest positional evidence because the lead variant falls within its annotated gene body.
2. SPATA5L1 deserves investigation because published kidney-expression analyses provide additional evidence for this regional candidate.
3. C15orf48 and SLC30A4 remain provisional candidates based on their location in the selected region.
4. The lead variant and nearby significant variants may represent a shared linkage disequilibrium signal rather than independent associations.
5. No causal gene has been established by this regional overlap analysis.

## Planned follow-up analyses

- Verify variant identifiers and coordinates against the source GWAS and genome build.
- Investigate fine-mapping results and credible sets for the associated locus.
- Examine kidney-tissue eQTL and colocalization evidence.
- Compare associations across creatinine-based eGFR, cystatin C-based eGFR, blood urea nitrogen, measured GFR, and clinical CKD where suitable data are available.
- Record evidence sources, limitations, and confidence separately for each candidate.
- Avoid assigning a causal gene based on proximity alone.

## References

1. Wuttke et al. (2019). A catalog of genetic loci associated with kidney function from analyses of a million individuals. Nature Genetics.
   https://doi.org/10.1038/s41588-019-0407-x

2. Köttgen et al. (2009). Multiple Novel Loci Are Associated with Indices of Renal Function and Chronic Kidney Disease.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC3039280/

3. Mapping eGFR loci to the renal transcriptome and phenome in the VA Million Veteran Program.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC6710266/

4. Transcriptome- and proteome-wide association studies nominate determinants of kidney function and damage.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC10291807/
