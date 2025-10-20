canh1 = int(input('Nhập cạnh 1: '))
canh2 = int(input('Nhập cạnh 2: '))
canh3 = int(input('Nhập cạnh 3: '))
if canh1 == canh2 and canh1 != canh3 or canh1 == canh3 and canh1 != canh2 or canh2 == canh3 and canh2 != canh1:
    print('Đây là tam giác cân')
elif canh1 == canh2 == canh3:
    print('Đây là tam giác đều')
else:
    print('Đây là tam giác thường')