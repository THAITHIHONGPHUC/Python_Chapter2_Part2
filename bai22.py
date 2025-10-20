def danh_sach():
    ds = list()
    for i in range(1, 21):
        ds.append(i**2)
    print('5 phần tử đầu tiên là', ds[:5])
    print('5 phần tử cuối cùng là', ds[-5:])
danh_sach()