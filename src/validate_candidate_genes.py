
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "reports/candidate_gene_prioritization.csv"

REQUIRED_COLUMNS = [
    "gene",
    "distance_from_lead_bp",
    "lead_variant_overlaps_gene",
    "evidence_summary",
    "current_priority",
    "key_limitation",
]


def main():
    df = pd.read_csv(INPUT_FILE)
    df.columns = df.columns.str.strip()
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing columns: {sorted(missing_columns)}")

    if df["gene"].isna().any() or df["gene"].duplicated().any():
        raise ValueError("Gene names must be present and unique.")

    if df["distance_from_lead_bp"].isna().any():
        raise ValueError("Gene distances must not be missing.")

    if (df["distance_from_lead_bp"] < 0).any():
        raise ValueError("Gene distances cannot be negative.")

    if not df["lead_variant_overlaps_gene"].isin(["yes", "no"]).all():
        raise ValueError("Overlap values must be 'yes' or 'no'.")

    if df[["evidence_summary", "current_priority", "key_limitation"]].isna().any().any():
        raise ValueError("Evidence fields must not be empty.")

    print("Candidate-gene validation passed.")
    print(f"Genes checked: {len(df)}")
    print("Genes:", ", ".join(df["gene"]))


if __name__ == "__main__":
    main()
