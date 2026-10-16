import pandas as pd

from src.score_candidate_genes import calculate_positional_score


def test_overlapping_gene_gets_score_2():
    row = pd.Series({
        "lead_variant_overlaps_gene": "yes",
        "distance_from_lead_bp": 0,
    })
    assert calculate_positional_score(row) == 2


def test_gene_within_20kb_gets_score_1():
    row = pd.Series({
        "lead_variant_overlaps_gene": "no",
        "distance_from_lead_bp": 10734,
    })
    assert calculate_positional_score(row) == 1


def test_gene_beyond_20kb_gets_score_0():
    row = pd.Series({
        "lead_variant_overlaps_gene": "no",
        "distance_from_lead_bp": 38932,
    })
    assert calculate_positional_score(row) == 0
