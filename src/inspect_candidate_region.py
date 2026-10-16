from pathlib import Path
import pandas as pd


# Lead eGFR-associated variant (GRCh37 coordinates)
LEAD_CHROMOSOME = "15"
LEAD_POSITION = 45683795
WINDOW_BP = 100_000


def main():
    genes_file = Path("data/raw/ensembl_grch37_genes.tsv")
    output_file = Path("data/processed/nearby_candidate_genes.csv")

    if not genes_file.exists():
        raise FileNotFoundError(
            f"Gene annotation file not found: {genes_file}"
        )

    genes = pd.read_csv(genes_file, sep="\t")

    required_columns = [
        "Gene name",
        "Gene stable ID",
        "Chromosome/scaffold name",
        "Gene start (bp)",
        "Gene end (bp)",
        "Gene type",
    ]

    missing = [column for column in required_columns if column not in genes.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Basic coordinate quality checks
    genes["Chromosome/scaffold name"] = (
        genes["Chromosome/scaffold name"].astype(str)
    )

    genes = genes.dropna(
        subset=["Gene start (bp)", "Gene end (bp)"]
    ).copy()

    invalid_coordinates = (
        (genes["Gene start (bp)"] <= 0)
        | (genes["Gene end (bp)"] < genes["Gene start (bp)"])
    )

    print("Gene records loaded:", len(genes))
    print("Invalid coordinate records excluded:", int(invalid_coordinates.sum()))

    genes = genes.loc[~invalid_coordinates].copy()

    # Select genes overlapping the lead variant's +/- 100 kb region
    region_start = LEAD_POSITION - WINDOW_BP
    region_end = LEAD_POSITION + WINDOW_BP

    nearby = genes[
        (genes["Chromosome/scaffold name"] == LEAD_CHROMOSOME)
        & (genes["Gene start (bp)"] <= region_end)
        & (genes["Gene end (bp)"] >= region_start)
    ].copy()

    # Distance is zero when the variant lies within the gene body
    nearby["distance_bp"] = (
        nearby["Gene start (bp)"].sub(LEAD_POSITION)
        .where(nearby["Gene start (bp)"] > LEAD_POSITION, 0)
    )

    outside_gene = (
        (nearby["Gene start (bp)"] > LEAD_POSITION)
        | (nearby["Gene end (bp)"] < LEAD_POSITION)
    )

    nearby.loc[outside_gene, "distance_bp"] = nearby.loc[
        outside_gene
    ].apply(
        lambda row: min(
            abs(row["Gene start (bp)"] - LEAD_POSITION),
            abs(row["Gene end (bp)"] - LEAD_POSITION),
        ),
        axis=1,
    )

    nearby = nearby.sort_values(
        ["distance_bp", "Gene name"], na_position="last"
    )

    output_file.parent.mkdir(parents=True, exist_ok=True)
    nearby.to_csv(output_file, index=False)

    print("Lead variant: chr15:", LEAD_POSITION, "(GRCh37)")
    print(f"Search window: {region_start:,}–{region_end:,}")
    print("Nearby gene records:", len(nearby))
    print("Saved regional candidates to:", output_file)

    display_columns = [
        "Gene name",
        "Gene stable ID",
        "Gene type",
        "Gene start (bp)",
        "Gene end (bp)",
        "distance_bp",
    ]

    print(nearby[display_columns].to_string(index=False))


if __name__ == "__main__":
    main()
