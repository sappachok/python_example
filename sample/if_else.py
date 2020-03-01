a = 33
b = 200
if b > a:
    print("b มีค่ามากกว่า a")


a = 200
b = 33
if b > a:
  print("b มีค่ามากกว่า a")
elif a == b:
  print("a และ b มีค่าเท่ากัน")
else:
  print("b มีค่าน้อย a")

a = 6
b = [1,2,3,4,5]

if a not in b:
    print("ไม่มีอยู่ในรายการ")
else:
    print("มีอยู่ในรายการ")