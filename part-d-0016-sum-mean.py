import polars as pl

def main():

    profit_or_loss = pl.read_csv("proorlo.csv", schema_overrides={"profit_or_loss": pl.Int8}).to_series()

    print(profit_or_loss.sum()) # 7

    print(profit_or_loss.mean())

# -538
# -1.076

if __name__ == "__main__":
    main()
