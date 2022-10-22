# === HÀM TỔ HỢP ===

import random

def list_Tổ_hợp(listElements,length):
    số_tổ_hợp = giai_thừa(len(listElements)) // ( giai_thừa(length) * giai_thừa(len(listElements)-length) )
    list_Tổ_hợp = []
    while len(list_Tổ_hợp) < số_tổ_hợp:
        tổ_hợp = set()
        for i in range(length):
            while True:
                x = listElements[random.randint(0,len(listElements)-1)]
                if x not in tổ_hợp:
                    tổ_hợp.add(x)
                    break
                else:
                    continue
        if tổ_hợp not in list_Tổ_hợp:
            list_Tổ_hợp.append(tổ_hợp)
        else:
            continue
    for i in range(len(list_Tổ_hợp)):
        list_Tổ_hợp[i] = tuple(list_Tổ_hợp[i])

    return list_Tổ_hợp

def giai_thừa(number):
    if number <= 1:
        return 1
    return number*giai_thừa(number-1)

# === END OF HÀM TỔ HỢP ===

# === DÙNG THƯ VIỆN:
from itertools import combinations
comb = combinations(listElements,length)
for k in comb:
    print(k)
# ===

if __name__ == '__main__':
    print(list_Tổ_hợp([1,2,3,5],3))