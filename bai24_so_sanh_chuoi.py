def chuoi(st1, st2):
    len1 = len(st1)
    len2 = len(st2)
    if len1 > len2:
        print('Chuỗi có độ dài lớn hơn là:', st1)
    elif len2 > len1:
        print('Chuỗi có độ dài lớn hơn là:', st2)
    else:
        print('2 chuỗi có độ dài bằng nhau')
        print(st1)
        print(st2)