month = input('Nhập tháng: ')
if month in ['tháng một', 'tháng ba', 'tháng năm', 'tháng bảy', 'tháng tám', 'tháng mười', 'tháng 12']:
    print(month, 'có 31 ngày')
elif month == 'tháng hai':
    print('tháng hai có 28 hoặc 29 ngày')
else:
    print(month, 'có 30 ngày')