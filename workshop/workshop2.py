start='y'

while start != 'n':
    print('กรุณาใส่ค่า a')
    a = input()

    print('กรุณาใส่ค่า b')
    b = input()

    print("=" * 30)
    if b > a:
        print(">> b มีค่ามากกว่า a")
    elif a == b:
        print(">> a และ b มีค่าเท่ากัน")
    else:
        print(">> b มีค่าน้อย a")

    print("=" * 30)

    print('ต้องการทำงานต่อไปหรือไม่? [y/n]')
    start = input()