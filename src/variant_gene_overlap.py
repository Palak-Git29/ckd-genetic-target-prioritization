from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
VARIANT_FILE = (
    PROJECT_ROOT / "data" / "processed" / "significant_variants.csv"
)
GENE_FILE = PROJECT_ROOT / "data" / "raw" / "ensembl_grch37_genes.tsv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"

STANDARD_CHROMOSOMES = [str(i) for i in range(1, 23)] + ["X", "Y"]
TOP_N = 10


def main():
    if not VARIANT_FILE.exists():
        raise FileNotFoundError(f"Variant file not found: {VARIANT_FILE}")
    if not GENE_FILE.exists():
        raise FileNotFoundError(f"Gene annotation not found: {GENE_FILE}")

    # Load the strongest genome-wide significant variants.
    variants = pd.read_csv(
        VARIANT_FILE,
        usecols=["Chr", "Pos_b37", "RSID", "P-value"],
    )

    variants["Chr"] = pd.to_numeric(variants["Chr"], errors="coerce")
    variants["Pos_b37"] = pd.to_numeric(
        variants["Pos_b37"], errors="coerce"
    )
    variants["P-value"] = pd.to_numeric(
        variants["P-value"], errors="coerce"
    )

    # Quality control: validate variant IDs and genomic coordinates.
    rows_before_qc = len(variants)
    variants["RSID"] = variants["RSID"].astype("string").str.strip()

    valid_rows = (
        variants["Chr"].between(1, 22)
        & (variants["Chr"] % 1 == 0)
        & (variants["Pos_b37"] > 0)
        & (variants["Pos_b37"] % 1 == 0)
        & (variants["P-value"] > 0)
        & (variants["P-value"] <= 1)
        & variants["RSID"].notna()
        & variants["RSID"].ne("")
    )

    variants = variants.loc[valid_rows].copy()
    rows_after_qc = len(variants)

    print("\nVariant QC")
    print(f"Rows before QC: {rows_before_qc:,}")
    print(f"Rows passing QC: {rows_after_qc:,}")
    print(
        f"Rows excluded by QC: "
        f"{rows_before_qc - rows_after_qc:,}"
    )

    variants["Chr"] = variants["Chr"].astype(int).astype(str)
    variants["Pos_b37"] = variants["Pos_b37"].astype(int)

    top_variants = (
        variants.sort_values("P-value")
        .drop_duplicates(subset=["RSID"])
        .head(TOP_N)
        .copy()
    )

    # Load Ensembl GRCh37 gene annotations.
    genes = pd.read_csv(GENE_FILE, sep="\t")
    genes = genes.rename(
        columns={
            "Gene stable ID": "gene_id",
            "Gene name": "gene_name",
            "Chromosome/scaffold name": "chromosome",
            "Gene start (bp)": "start",
            "Gene end (bp)": "end",
            "Gene type": "gene_biotype",
        }
    )

    genes["chromosome"] = genes["chromosome"].astype(str)
    genes["start"] = pd.to_numeric(genes["start"], errors="coerce")
    genes["end"] = pd.to_numeric(genes["end"], errors="coerce")
    # Quality control for gene annotation coordinates.
    genes_before_qc = len(genes)

    valid_gene_rows = (
        genes["gene_id"].notna()
        & genes["gene_id"].astype(str).str.strip().ne("")
        & genes["start"].notna()
        & genes["end"].notna()
        & (genes["start"] > 0)
        & (genes["end"] > 0)
        & (genes["start"] <= genes["end"])
    )

    genes = genes.loc[valid_gene_rows].copy()

    print("\nGene annotation QC")
    print(f"Records before coordinate QC: {genes_before_qc:,}")
    print(f"Records passing coordinate QC: {len(genes):,}")
    print(
        "Records excluded by coordinate QC: "
        f"{genes_before_qc - len(genes):,}"
    )

    genes = genes[
        genes["chromosome"].isin(STANDARD_CHROMOSOMES)
    ].dropna(subset=["start", "end"]).copy()

    genes["start"] = genes["start"].astype(int)
    genes["end"] = genes["end"].astype(int)

    # Match each variant to every gene whose interval contains its position.
    results = []

    for _, variant in top_variants.iterrows():
        matching_genes = genes[
            (genes["chromosome"] == variant["Chr"])
            & (genes["start"] <= variant["Pos_b37"])
            & (genes["end"] >= variant["Pos_b37"])
        ]

        if matching_genes.empty:
            results.append(
                {
                    "RSID": variant["RSID"],
                    "chromosome": variant["Chr"],
                    "position_grch37": variant["Pos_b37"],
                    "p_value": variant["P-value"],
                    "gene_id": "",
                    "gene_name": "",
                    "gene_biotype": "",
                }
            )
        else:
            for _, gene in matching_genes.iterrows():
                results.append(
                    {
                        "RSID": variant["RSID"],
                        "chromosome": variant["Chr"],
                        "position_grch37": variant["Pos_b37"],
                        "p_value": variant["P-value"],
                        "gene_id": gene["gene_id"],
                        "gene_name": gene["gene_name"],
                        "gene_biotype": gene["gene_biotype"],
                    }
                )

    results_df = pd.DataFrame(results)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / "top_variant_gene_overlap.csv"
    results_df.to_csv(output_file, index=False)

    print(f"Top variants analysed: {len(top_variants)}")
    print(f"Standard-chromosome gene records loaded: {len(genes)}")
    print(f"Variant–gene overlap rows: {len(results_df)}")
    print(f"Variants with at least one overlapping gene: "
          f"{results_df.loc[results_df['gene_id'] != '', 'RSID'].nunique()}")
    print(f"Saved results to: {output_file}")
    print(
        "\nCaution: positional overlap does not establish a causal gene. "
        "Variants without overlap may still affect genes through regulatory "
        "mechanisms or other pathways."
    )


if __name__ == "__main__":
    main()
