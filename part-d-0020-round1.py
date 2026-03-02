import polars as pl

def main():

    interest_rates = pl.read_csv("interests.csv").to_series()

    print(interest_rates.dtype) # Float64

    print(interest_rates.head(5))

    ceiled = interest_rates.ceil()

    print(ceiled.head(5))

    print(ceiled.dtype)

if __name__ == "__main__":
    main()

"""
Float64

shape: (5,)
Series: 'rates' [f64]
[
        5.357143
        5.785714
        null
        4.714286
        null
]

shape: (5,)
Series: 'rates' [f64]
[
        6.0
        6.0
        null
        5.0
        null
]

Float64

"""
