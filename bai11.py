num_list = list()

while (True):
    num = input('Nhập số: ')
    if num == 'end':
        break
    value = float(num)
    num_list.append(value)
    trung_binh = sum(num_list) / len(num_list)
print('Giá trị trung bình là', trung_binh)