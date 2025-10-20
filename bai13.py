lines = []

while (True):
    line = input('Nhập chuỗi (Nhấn Enter để kết thúc): ')
    if line:
        lines.append(line.upper())
    else:
        break
for st in lines:
    print(st)