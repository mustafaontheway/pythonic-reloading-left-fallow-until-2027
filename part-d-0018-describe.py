import polars as pl

def main():

    profit_or_loss = pl.read_csv("proorlo.csv", schema_overrides={"profit_or_loss": pl.Int8}).to_series()

    print(profit_or_loss.describe()) 


if __name__ == "__main__":
    main()

"""
shape: (9, 2)
┌────────────┬───────────┐
│ statistic  ┆ value     │
│ ---        ┆ ---       │
│ str        ┆ f64       │
╞════════════╪═══════════╡
│ count      ┆ 500.0     │
│ null_count ┆ 7.0       │
│ mean       ┆ -1.076    │
│ std        ┆ 57.719818 │
│ min        ┆ -100.0    │
│ 25%        ┆ -53.0     │
│ 50%        ┆ -3.0      │
│ 75%        ┆ 50.0      │
│ max        ┆ 99.0      │
└────────────┴───────────┘

"""
