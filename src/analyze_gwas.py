
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "ckdgen_2019_egfr_transancestry.txt.gz"
)
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"

GWAS_THRESHOLD = 5e-8

REQUIRED_COLUMNS = [
    "Chr",
    "Pos_b37",
    "RSID",
    "Allele1",
    "Allele2",
    "Freq1",
    "Effect",
    "StdErr",
    "P-value",
    "n_total_sum",
]


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"GWAS file not found: {INPUT_FILE}\n"
            "Download the dataset before running this script."
        )

    print("Reading GWAS summary statistics...")
    gwas = pd.read_csv(INPUT_FILE, sep=r"\s+")

    missing_columns = set(REQUIRED_COLUMNS) - set(gwas.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    gwas["P-value"] = pd.to_numeric(
        gwas["P-value"], errors="coerce"
    )

    valid_p = gwas["P-value"].between(0, 1)
    significant = gwas.loc[
        valid_p & (gwas["P-value"] < GWAS_THRESHOLD)
    ].copy()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / "significant_variants.csv"
    significant.to_csv(output_file, index=False)

    print(f"Total variants/rows: {len(gwas):,}")
    print(f"Rows with valid P-values: {valid_p.sum():,}")
    print(
        "Rows below GWAS significance threshold "
        f"({GWAS_THRESHOLD:g}): {len(significant):,}"
    )
    print(f"Saved significant rows to: {output_file}")
    
    # Summarize significant GWAS rows by chromosome
    chromosome_summary = (
        significant.groupby("Chr")
        .agg(
            significant_rows=("RSID", "size"),
            unique_rsids=("RSID", "nunique"),
            strongest_p_value=("P-value", "min"),
        )
        .reset_index()
        .sort_values("Chr")
    )

    summary_file = OUTPUT_DIR / "chromosome_summary.csv"
    chromosome_summary.to_csv(summary_file, index=False)

    print(f"Saved chromosome summary to: {summary_file}")


if __name__ == "__main__":
    main()
