import pandas as pd

df = pd.read_excel("province.xlsx")
#data.head()
#print(data.head(10))
#print(data.tail(10))

#print(data.info())
#print(data.shape)

print('กรุณาใส่ชื่อจังหวัดในประเทศไทย:')
x = input()

province = df['province'].values.tolist()

if x in province:
    print("จังหวัด", x, "อยู่ในประเทศไทย")
else:
    print("จังหวัด", x, "ไม่อยู่ในประเทศไทย")