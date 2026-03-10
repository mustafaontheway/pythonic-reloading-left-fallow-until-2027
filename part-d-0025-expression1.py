import polars as pl

def main():

    # The expression is lazy. It has no knowledge of a specific `DataFrame` 
    # It also doesn't know the data type of its column

    employees = pl.read_csv("employees.csv")

    #print(employees.columns) # ['name', 'department', 'email', 'salary', 'years_at_company', 'start_date']

    #print(pl.col("salary")) # col("salary")

    #print(type(pl.col("salary"))) # <class 'polars.expr.expr.Expr'>

    #print(pl.col("salary").max()) # col("salary").max()

    print(type(pl.col("salary").max())) # <class 'polars.expr.expr.Expr'>

if __name__ == "__main__":
    main()



# python main.py
