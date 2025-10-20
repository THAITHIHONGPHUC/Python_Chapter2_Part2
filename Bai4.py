num1 = float(input('Nhập số thứ 1: '))
num2 = float(input('Nhập số thứ 2: '))
num3 = float(input('Nhập số thứ 3: '))

if num1 >= num2 and num1 >= num3:
    print('Số lớn nhất là', num1)
elif num2 >= num1 and num2 >= num3:
    print('Số lớn nhất là', num2)
else:
    print('Số lớn nhất là', num3)