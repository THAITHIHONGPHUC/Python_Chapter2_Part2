def tao_TD(max):
    d = dict()
    for i in range(1, max + 1):
        d[i] = i**2
    return d

def print_item(TD):
    for k, v in TD.items():
        print(k, ':', v)

def print_key(TD):
    for k in TD.keys():
        print(k)

def print_value(TD):
    for v in TD.values():
        print(v)