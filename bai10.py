total = 0
dem = 0
while (True):
    num = input('Nhập số: ')
    if num == 'end':
        break
    total = total + int(num)
    dem = dem + 1
    trung_binh = total / dem
print('Giá trị trung bình là', trung_binh)