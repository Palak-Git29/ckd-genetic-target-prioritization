from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent

PIPELINE_STEPS = [
    ("GWAS analysis", "src/analyze_gwas.py"),
    ("Manhattan plot", "src/plot_manhattan.py"),
    ("Chromosome summary plot", "src/plot_chromosome_summary.py"),
    ("Lead-region analysis", "src/analyze_lead_region.py"),
    ("Candidate-region gene inspection", "src/inspect_candidate_region.py"),
    ("Variant-to-gene overlap", "src/variant_gene_overlap.py"),
    ("Candidate-gene validation", "src/validate_candidate_genes.py"),
    ("Candidate-gene scoring", "src/score_candidate_genes.py"),
    ("Lead-region plot", "src/plot_lead_region.py"),
    ("Candidate-score plot", "src/plot_candidate_scores.py"),
]


def main():
    for step_name, script_path in PIPELINE_STEPS:
        print(f"\n{'=' * 60}", flush=True)
        print(f"STEP: {step_name}", flush=True)
        print(f"Running: {script_path}", flush=True)
        print("=" * 60, flush=True)

        result = subprocess.run(
            [sys.executable, str(PROJECT_ROOT / script_path)],
            cwd=PROJECT_ROOT,
            check=False,
        )

        if result.returncode != 0:
            print(
                f"\nPipeline stopped: {step_name} failed "
                f"(exit code {result.returncode}).",
                file=sys.stderr,
                flush=True,
            )
            return result.returncode

    print("\nPipeline completed successfully.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
