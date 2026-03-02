import polars as pl

def main():

    interest_rates = pl.read_csv("interests.csv").to_series()

    print(interest_rates.head(5))

    print("-------------------------------------------------")

    rounded = interest_rates.round(3)

    print(rounded.head(5))

if __name__ == "__main__":
    main()

"""
shape: (5,)
Series: 'rates' [f64]
[
        5.357143
        5.785714
        null
        4.714286
        null
]
-------------------------------------------------
shape: (5,)
Series: 'rates' [f64]
[
        5.357
        5.786
        null
        4.714
        null
]

"""
