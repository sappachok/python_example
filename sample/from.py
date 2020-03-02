from datetime import datetime

# ดึงข้อมูลวันที่ของวันที่จากไลบรารี่ datetime
now = datetime.now()
print(now)
# แปลงข้อมูลวันที่ให้อยู่ในรูปแบบข้อความตามรูปแบบที่กำหนดไว้ข้างต้น
date = now.strftime("%Y %B %d")
print("date:", date)

time = now.strftime("%H:%M:%S")
print("time:", time)