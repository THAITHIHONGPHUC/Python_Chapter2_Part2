n = int(input('Nhập số: '))

n_str = str(n)
bac_n = len(n_str)

total = 0
for num in n_str:
    s = int(num) ** bac_n
    total = total + s
if total == n:
    print(n, 'là số Armstrong')
else:
    print(n, 'không phải số Armstrong')