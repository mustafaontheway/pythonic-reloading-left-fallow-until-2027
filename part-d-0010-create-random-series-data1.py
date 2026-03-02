import polars as pl

def main():

    profit_or_loss = pl.int_range(-100, 100, dtype=pl.Int8, eager=True).sample(500, with_replacement=True, seed=100)

    print(profit_or_loss.head(5))


if __name__ == "__main__":
    main()


"""
shape: (5,)
Series: 'literal' [i8]
[
        75
        81
        66
        -32
        75
]

"""
