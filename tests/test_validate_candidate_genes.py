
import pandas as pd


def test_candidate_gene_table_has_unique_gene_names():
    df = pd.read_csv("reports/candidate_gene_prioritization.csv")
    df.columns = df.columns.str.strip()

    assert df["gene"].notna().all()
    assert df["gene"].is_unique


def test_candidate_gene_distances_are_nonnegative():
    df = pd.read_csv("reports/candidate_gene_prioritization.csv")
    df.columns = df.columns.str.strip()

    distances = pd.to_numeric(
        df["distance_from_lead_bp"], errors="raise"
    )

    assert distances.notna().all()
    assert (distances >= 0).all()


def test_candidate_gene_evidence_is_documented():
    df = pd.read_csv("reports/candidate_gene_prioritization.csv")
    df.columns = df.columns.str.strip()

    required_fields = [
        "evidence_summary",
        "current_priority",
        "key_limitation",
    ]

    assert df[required_fields].notna().all().all()
    assert df[required_fields].apply(
        lambda column: column.astype(str).str.strip().ne("")
    ).all().all()
