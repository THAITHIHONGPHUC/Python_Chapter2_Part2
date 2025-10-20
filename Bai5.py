n = int(input('Nhập số nguyên n (n > 0): '))

total = 0
for i in range(1, n+1):
    total = total + (i / (i+1))
print('Tổng là', round(total, 2))