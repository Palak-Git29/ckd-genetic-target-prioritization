
from pathlib import Path
import math

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data/processed/lead_region_variants.csv"
GENE_FILE = PROJECT_ROOT / "data/processed/nearby_candidate_genes.csv"
OUTPUT_FILE = PROJECT_ROOT / "results/figures/lead_region_association.png"

LEAD_POSITION = 45683795

# Selected protein-coding genes in the region
GENES_TO_PLOT = ["GATM", "SPATA5L1", "C15orf48", "SLC30A4"]


def main():
    df = pd.read_csv(INPUT_FILE)
    genes = pd.read_csv(GENE_FILE)

    df["Pos_b37"] = pd.to_numeric(df["Pos_b37"], errors="coerce")
    df["P-value"] = pd.to_numeric(df["P-value"], errors="coerce")
    genes["Gene start (bp)"] = pd.to_numeric(
        genes["Gene start (bp)"], errors="coerce"
    )
    genes["Gene end (bp)"] = pd.to_numeric(
        genes["Gene end (bp)"], errors="coerce"
    )

    df = df.dropna(subset=["Pos_b37", "P-value"])
    df = df[df["P-value"] > 0].copy()
    genes = genes.dropna(
        subset=["Gene name", "Gene start (bp)", "Gene end (bp)"]
    )
    genes = genes[genes["Gene name"].isin(GENES_TO_PLOT)].copy()
    genes = genes.drop_duplicates(subset=["Gene name"])

    df["minus_log10_p"] = df["P-value"].map(lambda p: -math.log10(p))

    # Two aligned panels: association signal and gene locations
    fig, (ax, gene_ax) = plt.subplots(
        2,
        1,
        figsize=(12, 7),
        sharex=True,
        gridspec_kw={"height_ratios": [4, 1.5]},
    )

    ax.scatter(
        df["Pos_b37"],
        df["minus_log10_p"],
        s=14,
        alpha=0.7,
    )
    ax.axvline(
        LEAD_POSITION,
        linestyle="--",
        label="Lead variant: rs1145077",
    )
    ax.set_ylabel("-log10(p-value)")
    ax.set_title("Regional eGFR GWAS associations on chromosome 15")
    ax.legend()

    for row, (_, gene) in enumerate(genes.iterrows()):
        start = gene["Gene start (bp)"]
        end = gene["Gene end (bp)"]
        center = (start + end) / 2

        gene_ax.plot(
            [start, end],
            [row, row],
            linewidth=6,
            solid_capstyle="butt",
        )
        gene_ax.text(
            center,
            row + 0.16,
            gene["Gene name"],
            ha="center",
            va="bottom",
            fontsize=9,
        )

    gene_ax.axvline(LEAD_POSITION, linestyle="--", alpha=0.7)
    gene_ax.set_yticks([])
    gene_ax.set_ylabel("Genes")
    gene_ax.set_xlabel("Genomic position (GRCh37)")
    gene_ax.set_ylim(-0.5, len(genes) + 0.8)

    fig.tight_layout()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Variants plotted: {len(df)}")
    print(f"Genes annotated: {len(genes)}")
    print(f"Figure saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
