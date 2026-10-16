"""Calculate a transparent, preliminary positional-priority score."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "reports" / "candidate_gene_prioritization.csv"
OUTPUT_FILE = PROJECT_ROOT / "reports" / "candidate_gene_scored.csv"


def calculate_positional_score(row):
    """Score proximity to the lead variant using project-defined rules."""
    if str(row["lead_variant_overlaps_gene"]).strip().lower() == "yes":
        return 2

    distance = float(row["distance_from_lead_bp"])

    if distance <= 20_000:
        return 1

    return 0


def main():
    candidates = pd.read_csv(INPUT_FILE)
    candidates.columns = candidates.columns.str.strip()

    candidates["positional_score"] = candidates.apply(
        calculate_positional_score, axis=1
    )

    candidates["score_interpretation"] = candidates["positional_score"].map(
        {
            2: "Lead variant overlaps gene",
            1: "Within 20 kb; proximity-based follow-up",
            0: "More than 20 kb away; lower positional priority",
        }
    )

    candidates = candidates.sort_values(
        ["positional_score", "distance_from_lead_bp"],
        ascending=[False, True],
    )

    candidates.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved scored candidates to: {OUTPUT_FILE}")
    print(
        candidates[
            [
                "gene",
                "distance_from_lead_bp",
                "positional_score",
                "score_interpretation",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
