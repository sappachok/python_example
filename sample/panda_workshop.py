import pandas as pd

df = pd.read_excel("province.xlsx")

area_min = df['area'].min()
area_max = df['area'].max()

print("area min:", area_min)
print("area max:", area_max)

print("จังหวัดที่มีพื้นที่น้อยที่สุด", df[df['area']==area_min])
print("จังหวัดที่มีพื้นที่มากที่สุด", df[df['area']==area_max])