import polars as pl

df = pl.DataFrame({"Name": ["Aykan", "Ayhan", "Aybuke", "Aybilge", "Aygun", "Aysel", "Aysu", "Ayaz", "Ayazhan", "Aygeldi", "Ayses"], 
                   "Age": [96, 17, 24, 45, 65, 77, 4, 44, 66, 55, 77]})

print(df.head(4) == df.limit(4))

print("---------------------------------")

print(df.head(-7))

"""
shape: (4, 2)
┌──────┬──────┐
│ Name ┆ Age  │
│ ---  ┆ ---  │
│ bool ┆ bool │
╞══════╪══════╡
│ true ┆ true │
│ true ┆ true │
│ true ┆ true │
│ true ┆ true │
└──────┴──────┘
---------------------------------
shape: (4, 2)
┌─────────┬─────┐
│ Name    ┆ Age │
│ ---     ┆ --- │
│ str     ┆ i64 │
╞═════════╪═════╡
│ Aykan   ┆ 96  │
│ Ayhan   ┆ 17  │
│ Aybuke  ┆ 24  │
│ Aybilge ┆ 45  │

"""
