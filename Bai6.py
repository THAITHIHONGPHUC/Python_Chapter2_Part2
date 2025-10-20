str = input('Nhập câu: ')

capital_letter = 0
normal_letter = 0

for ch in str:
    if ch.isupper():
        capital_letter = capital_letter + 1
    elif ch.islower():
        normal_letter = normal_letter + 1
    else:
        pass
print('Tổng số chữ hoa là', capital_letter)
print('Tổng số chữ thường là', normal_letter)