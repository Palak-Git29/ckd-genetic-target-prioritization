# Candidate Gene Evidence Review

## Project overview

This project looks at genetic variants associated with estimated glomerular filtration rate (eGFR), using the summary statistics published by Wuttke et al. (2019).

For a closer look at one associated region, I selected rs1145077 on chromosome 15. The variant is at position 45,683,795 on the GRCh37 reference genome and has a reported P-value of 6.85e-142.

To identify genes near this variant, I compared its position with Ensembl gene annotations for GRCh37. This identified 12 gene records within 100 kb on either side of the variant.

One important point is that the GWAS measures eGFR estimated from serum creatinine. It does not directly test for clinical CKD, and changes in creatinine-based eGFR can sometimes reflect creatinine production or metabolism rather than kidney filtration itself.

## Candidate genes

### 1. GATM

**Why it stands out**

The lead variant, rs1145077, falls within the annotated boundaries of GATM, making it the strongest candidate based on physical location.

**What the biology suggests**

GATM encodes glycine amidinotransferase, an enzyme involved in creatine production. Creatine breaks down to creatinine, which is measured in blood and used to estimate eGFR. As a result, genetic differences affecting this pathway can influence creatinine-based eGFR without necessarily indicating a change in kidney filtration.

**What remains uncertain**

Previous studies have linked this region to eGFR, but the association could partly reflect creatinine metabolism. The fact that rs1145077 falls inside GATM does not prove that the variant is causal or that GATM explains the entire association.

**Current assessment:** GATM is the leading positional candidate, but its role in this association needs further investigation.

### 2. SPATA5L1

**Why it stands out**

SPATA5L1 is located approximately 10.7 kb from the lead variant, just outside the annotated GATM gene body.

**What previous studies suggest**

Studies of kidney function have reported associations involving the GATM–SPATA5L1 region. A 2019 study also reported kidney gene-expression evidence supporting SPATA5L1 as a possible mediator of an eGFR association at the broader locus.

A later transcriptome- and proteome-wide study reported that GATM and SPATA5L1 were associated with creatinine-based eGFR, but not with cystatin C-based eGFR or blood urea nitrogen in its analyses. This raises the possibility that the signal partly reflects creatinine biology rather than kidney filtration alone.

These findings concern the broader region and do not establish that rs1145077 is responsible for the association. The precise mechanism remains unclear.

**Current assessment:** SPATA5L1 is worth investigating alongside GATM because previous studies provide additional evidence beyond physical proximity.

### 3. C15orf48

**Why it was included**

C15orf48 is approximately 38.9 kb from the lead variant and is annotated as a protein-coding gene in the Ensembl GRCh37 dataset.

**What we know so far**

The current analysis establishes that C15orf48 lies within the selected region. I have not yet assessed enough independent genetic or functional evidence to determine whether it contributes to the eGFR association.

Being nearby and protein-coding is not, on its own, enough to establish a role in kidney function.

**Current assessment:** A provisional candidate that needs more evidence before it can be prioritised.

### 4. SLC30A4

**Why it was included**

SLC30A4 is approximately 88.0 kb from the lead variant and is annotated as a protein-coding gene in the regional dataset.

**What we know so far**

Its location makes it part of the region worth examining, but the current analysis does not establish a link between SLC30A4 and this eGFR association. Additional genetic, expression, or functional evidence would be needed to assess its relevance.

**Current assessment:** A provisional candidate; its role in this association has not yet been established.

## What the analysis tells us

GATM is the strongest candidate based on location because the lead variant falls within its annotated gene body. SPATA5L1 is also worth investigating because previous kidney-expression studies provide additional evidence for the broader region.

C15orf48 and SLC30A4 were included because they lie within the selected window, but their relevance to this association remains uncertain.

The next question is whether the nearby variants represent one shared association signal, potentially due to linkage disequilibrium, and which gene or biological mechanism best explains it. The regional overlap analysis alone cannot answer that question, so I have not assigned a causal gene.

## Next steps

- Check the variant identifier, genomic position, and genome build against the original GWAS data.
- Look for fine-mapping results and credible sets to identify variants more likely to explain the association.
- Examine kidney-tissue eQTL and colocalization results to see whether the GWAS signal shares a genetic cause with changes in gene expression.
- Where suitable datasets are available, compare results for creatinine-based eGFR with cystatin C-based eGFR, blood urea nitrogen, measured GFR, and clinical CKD.
- Keep the evidence, its source, and its limitations documented for each candidate gene.
- Avoid prioritising a gene solely because it is close to the lead variant.

## References

1. Wuttke et al. (2019). A catalog of genetic loci associated with kidney function from analyses of a million individuals. *Nature Genetics*.
   https://doi.org/10.1038/s41588-019-0407-x

2. Köttgen et al. (2009). Multiple Novel Loci Are Associated with Indices of Renal Function and Chronic Kidney Disease.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC3039280/

3. Mapping eGFR loci to the renal transcriptome and phenome in the VA Million Veteran Program.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC6710266/

4. Transcriptome- and proteome-wide association studies nominate determinants of kidney function and damage.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC10291807/
