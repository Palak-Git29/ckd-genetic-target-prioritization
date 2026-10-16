
import pandas as pd

from src.plot_candidate_scores import main


def test_plot_script_creates_png(tmp_path, monkeypatch):
    input_file = tmp_path / "candidate_gene_scored.csv"
    output_file = tmp_path / "candidate_gene_positional_scores.png"

    pd.DataFrame({
        "gene": ["GATM", "SPATA5L1"],
        "distance_from_lead_bp": [0, 10734],
        "positional_score": [2, 1],
    }).to_csv(input_file, index=False)

    monkeypatch.setattr(
        "src.plot_candidate_scores.INPUT_FILE", input_file
    )
    monkeypatch.setattr(
        "src.plot_candidate_scores.OUTPUT_FILE", output_file
    )

    main()

    assert output_file.exists()
    assert output_file.stat().st_size > 0
