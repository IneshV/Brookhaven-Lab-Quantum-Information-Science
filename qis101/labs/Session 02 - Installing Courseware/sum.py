import pandas as pd

# closed-form definition of f(n)
def f(n):
    return 4 / (n + 1) if n % 2 == 1 else -2 / n

# build the DataFrame
df = pd.DataFrame({'n': range(1, 1001)})
df['f(n)'] = df['n'].apply(f)

# inspect a few rows
print(df.head())       # first 5 rows
print(df.tail())       # last 5 rows

# compute the sum
total = df['f(n)'].sum()
print("\nSum of f(n) from 1 to 1000:", total)
