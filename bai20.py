num = int(input('Nhập số: '))

result = 1
for i in range(1, num + 1):
    result = result * i
print(str(num) + '! = ', result)