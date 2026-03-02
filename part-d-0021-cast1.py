import polars as pl

def main():

    interest_rates = pl.read_csv("interests.csv").to_series()

    #print(interest_rates.dtype) 

    print(interest_rates.head(5))

    print("-------------------------------------------------")

    ceiled = interest_rates.ceil().cast(pl.Int8)

    print(ceiled.head(5))

    #print(ceiled.dtype)

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
Series: 'rates' [i8]
[
        6
        6
        null
        5
        null
]

"""
