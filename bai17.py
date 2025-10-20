st = input('Nhập câu: ')

d = {'words': 0, 'nums': 0}

for ch in st:
    if ch.isalpha() == True:
        d['words'] += 1
    elif ch.isdigit() == True:
        d['nums'] +=1
    else:
        continue
print('Số chữ cái là', d['words'])
print('Số chữ số là', d['nums'])