str = input('Nhập chuỗi: ')
str_search = input('Nhập chuỗi cần tìm: ')

if str_search in str:
    print('Đã tìm thấy chuỗi cần tìm, tại vị trí', str.find(str_search))
else:
    print('Không tìm thấy chuỗi!')