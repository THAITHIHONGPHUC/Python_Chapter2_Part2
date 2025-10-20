word = input('Nhập chữ cái: ')
if word in ['u', 'e', 'o', 'a', 'i']:
    print('Chữ cái', word, 'là nguyên âm')
elif word == 'y':
    print('Chữ cái y có thể là nguyên âm hoặc phụ âm')
else:
    print('Chữ cái', word, 'là phụ âm')