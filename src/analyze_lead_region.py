from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
GWAS_FILE = PROJECT_ROOT / "data/raw/ckdgen_2019_egfr_transancestry.txt.gz"
OUTPUT_FILE = PROJECT_ROOT / "data/processed/lead_region_variants.csv"

LEAD_CHROMOSOME = "15"
LEAD_POSITION = 45683795
WINDOW_BP = 100_000


def main():
    print("Loading GWAS summary statistics...")

    df = pd.read_csv(
        GWAS_FILE,
        sep=r"\s+",
        compression="gzip",
        low_memory=False,
    )

    df["Chr"] = df["Chr"].astype(str)
    df["Pos_b37"] = pd.to_numeric(df["Pos_b37"], errors="coerce")
    df["P-value"] = pd.to_numeric(df["P-value"], errors="coerce")

    start = LEAD_POSITION - WINDOW_BP
    end = LEAD_POSITION + WINDOW_BP

    region = df[
        (df["Chr"] == LEAD_CHROMOSOME)
        & df["Pos_b37"].between(start, end)
    ].copy()

    region = region.sort_values("P-value")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    region.to_csv(OUTPUT_FILE, index=False)

    print(f"Region: chr{LEAD_CHROMOSOME}:{start}-{end} (GRCh37)")
    print(f"Variants found: {len(region)}")
    print(f"Output saved to: {OUTPUT_FILE}")

    if not region.empty:
        print("\nTop 5 variants:")
        print(
            region[
                ["Chr", "Pos_b37", "RSID", "Effect", "StdErr", "P-value"]
            ].head(5).to_string(index=False)
        )


if __name__ == "__main__":
    main()
