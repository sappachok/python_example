import pandas as pd

df = pd.read_excel("province.xlsx")

print(df.head(10))
print(df.tail(10))

print(df.info())
print(df.shape)

print("sum:", df['area'].sum())

area_min = df['area'].min()
area_max = df['area'].max()

print("area min:", area_min)
print("area max:", area_max)

print(df[df['area']>15000])
