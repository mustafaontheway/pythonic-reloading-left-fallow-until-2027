import polars as pl

def main():

    profit_or_loss1 = pl.int_range(-100, 100, dtype=pl.Int8, eager=True).sample(500, with_replacement=True, seed=100)

    print("Bytes in memory: ", profit_or_loss1.estimated_size())

    profit_or_loss2 = pl.int_range(-100, 100, dtype=pl.Int128, eager=True).sample(500, with_replacement=True, seed=100)

    print("Bytes in memory: ", profit_or_loss2.estimated_size())

# 1 byte is equal to 8 bits

# Bytes in memory:  500
# Bytes in memory:  8000


if __name__ == "__main__":
    main()
