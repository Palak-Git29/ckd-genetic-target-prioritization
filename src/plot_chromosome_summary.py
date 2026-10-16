
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = (
    PROJECT_ROOT / "data" / "processed" / "chromosome_summary.csv"
)
OUTPUT_DIR = PROJECT_ROOT / "results" / "figures"


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Summary file not found: {INPUT_FILE}\n"
            "Run src/analyze_gwas.py first."
        )

    summary = pd.read_csv(INPUT_FILE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    summary = summary.sort_values("Chr")

    plt.figure(figsize=(12, 6))
    plt.bar(
        summary["Chr"].astype(str),
        summary["significant_rows"],
    )
    plt.xlabel("Chromosome (GRCh37)")
    plt.ylabel("Genome-wide significant rows")
    plt.title("Genome-wide Significant eGFR GWAS Rows by Chromosome")
    plt.tight_layout()

    output_file = OUTPUT_DIR / "significant_rows_by_chromosome.png"
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Saved plot to: {output_file}")


if __name__ == "__main__":
    main()
