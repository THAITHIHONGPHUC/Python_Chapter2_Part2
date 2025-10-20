my_str = input('Nhập chuỗi: ')

danh_sach = my_str.split()
danh_sach.sort()

print('Các từ sau khi sắp xếp là', danh_sach)
for word in danh_sach:
    print(word)