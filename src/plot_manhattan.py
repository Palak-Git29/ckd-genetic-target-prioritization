
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "ckdgen_2019_egfr_transancestry.txt.gz"
)
OUTPUT_DIR = PROJECT_ROOT / "results" / "figures"
GWAS_THRESHOLD = 5e-8


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"GWAS file not found: {INPUT_FILE}")

    print("Reading GWAS summary statistics...")
    gwas = pd.read_csv(
        INPUT_FILE,
        sep=r"\s+",
        usecols=["Chr", "Pos_b37", "P-value", "RSID"],
    )

    for column in ["Chr", "Pos_b37", "P-value"]:
        gwas[column] = pd.to_numeric(gwas[column], errors="coerce")

    gwas = gwas.dropna(subset=["Chr", "Pos_b37", "P-value"])
    gwas = gwas[
        gwas["Chr"].between(1, 22)
        & (gwas["Chr"] % 1 == 0)
        & (gwas["Pos_b37"] > 0)
        & (gwas["P-value"] > 0)
        & (gwas["P-value"] <= 1)
    ].copy()

    gwas["Chr"] = gwas["Chr"].astype(int)
    gwas["minus_log10_p"] = -np.log10(gwas["P-value"])
    gwas = gwas.sort_values(["Chr", "Pos_b37"])

    # Place chromosomes consecutively on the x-axis.
    chromosome_offsets = {}
    tick_positions = []
    tick_labels = []
    cumulative_position = 0

    for chromosome in range(1, 23):
        chr_data = gwas[gwas["Chr"] == chromosome]
        if chr_data.empty:
            continue

        chromosome_offsets[chromosome] = cumulative_position
        chr_min = chr_data["Pos_b37"].min()
        chr_max = chr_data["Pos_b37"].max()

        tick_positions.append(
            cumulative_position + (chr_min + chr_max) / 2
        )
        tick_labels.append(str(chromosome))
        cumulative_position += chr_max + 1

    gwas["cumulative_position"] = (
        gwas["Pos_b37"] + gwas["Chr"].map(chromosome_offsets)
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(16, 6))

    colors = ["#315A9E", "#D17A32"]

    for chromosome in range(1, 23):
        subset = gwas[gwas["Chr"] == chromosome]
        if subset.empty:
            continue

        ax.scatter(
            subset["cumulative_position"],
            subset["minus_log10_p"],
            s=2,
            color=colors[(chromosome - 1) % 2],
            alpha=0.75,
            linewidths=0,
            rasterized=True,
        )

    threshold_y = -np.log10(GWAS_THRESHOLD)
    ax.axhline(
        threshold_y,
        color="#B22222",
        linestyle="--",
        linewidth=1.2,
        label=r"Genome-wide significance ($P = 5 \times 10^{-8}$)",
    )

    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels)
    ax.set_xlabel("Chromosome (GRCh37)")
    ax.set_ylabel(r"$-\log_{10}(P)$")
    ax.set_title("CKDGen eGFR GWAS: Manhattan Plot")
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    ax.grid(axis="y", linestyle=":", alpha=0.25)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(frameon=False, loc="upper right")

    fig.tight_layout()
    output_file = OUTPUT_DIR / "egfr_gwas_manhattan.png"
    fig.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Rows plotted: {len(gwas):,}")
    print(f"Chromosomes plotted: {len(tick_labels)}")
    print(f"Significance threshold: P < {GWAS_THRESHOLD:g}")
    print(f"Saved Manhattan plot to: {output_file}")


if __name__ == "__main__":
    main()
