
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"

# Coordinates are GRCh37, matching the GWAS summary statistics.
variants = pd.DataFrame(
    [
        ("rs1145077", 45683795, 6.85e-142),
        ("rs1153855", 45660758, 7.64e-142),
        ("rs1145080", 45681338, 7.75e-142),
        ("rs1145076", 45684508, 8.04e-142),
        ("rs1145084", 45675440, 9.93e-142),
        ("rs2467862", 45643843, 2.61e-141),
        ("rs1049518", 45653367, 2.80e-141),
        ("rs2486274", 45666228, 3.27e-141),
        ("rs1426932", 45687256, 3.40e-141),
        ("rs1153860", 45636584, 3.41e-141),
    ],
    columns=["RSID", "position", "p_value"],
)

# Preliminary gene annotations retrieved from Ensembl.
genes = pd.DataFrame(
    [
        ("GATM", 45653322, 45694525),
        ("SPATA5L1", 45694529, 45713617),
        ("C15orf48", 45722727, 45740959),
    ],
    columns=["gene", "start", "end"],
)

results = []

for _, variant in variants.iterrows():
    overlapping = genes.loc[
        (genes["start"] <= variant["position"])
        & (genes["end"] >= variant["position"]),
        "gene",
    ].tolist()

    results.append(
        {
            "RSID": variant["RSID"],
            "chromosome": 15,
            "position_grch37": variant["position"],
            "p_value": variant["p_value"],
            "overlapping_genes": ";".join(overlapping),
        }
    )

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

output_file = OUTPUT_DIR / "top_variant_gene_overlap.csv"
pd.DataFrame(results).to_csv(output_file, index=False)

print(pd.DataFrame(results).to_string(index=False))
print(f"\nSaved results to: {output_file}")
print(
    "\nNote: this is a preliminary overlap check using only "
    "three selected genes, not a complete variant-to-gene analysis."
)
