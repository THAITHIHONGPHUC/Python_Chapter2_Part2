st = input('Nhập văn bản: ')

tach_tu = st.split()

d = dict()
for ch in tach_tu:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
sap_xep = sorted(d.items(), key= lambda x: x[1], reverse= True)
top_10 = sap_xep[:10]
print('10 từ phổ biến nhất là:')
for word, count in top_10:
    print(word, ':', count)