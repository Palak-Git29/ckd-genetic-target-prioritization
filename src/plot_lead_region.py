from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data/processed/lead_region_variants.csv"
OUTPUT_FILE = PROJECT_ROOT / "results/figures/lead_region_association.png"

LEAD_POSITION = 45683795


def main():
    df = pd.read_csv(INPUT_FILE)

    df["Pos_b37"] = pd.to_numeric(df["Pos_b37"], errors="coerce")
    df["P-value"] = pd.to_numeric(df["P-value"], errors="coerce")

    df = df.dropna(subset=["Pos_b37", "P-value"])
    df = df[df["P-value"] > 0].copy()

    df["minus_log10_p"] = -df["P-value"].map(lambda p: __import__("math").log10(p))

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.scatter(
        df["Pos_b37"],
        df["minus_log10_p"],
        s=14,
        alpha=0.7,
    )
    plt.axvline(LEAD_POSITION, linestyle="--", label="Lead variant: rs1145077")

    plt.xlabel("Genomic position (GRCh37)")
    plt.ylabel("-log10(p-value)")
    plt.title("Regional eGFR GWAS associations on chromosome 15")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=300)
    plt.close()

    print(f"Variants plotted: {len(df)}")
    print(f"Figure saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
