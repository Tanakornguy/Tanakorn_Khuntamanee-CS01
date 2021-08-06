num = int(input('กำหนดจำนวนตัวเลขทั้งหมดที่ต้องการใส่ : '))
numtotal = []
for i in range(num):
    data = int(input('ใส่ตัวเลย : '))
    numtotal += [data]
numtotal.sort()
print(numtotal)
print('min',numtotal[0])
print('max',numtotal[-1])