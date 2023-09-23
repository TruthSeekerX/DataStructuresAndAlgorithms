import random

def quick_sort(s):
    n = len(s)
    if n<2: return
    p = s.pop(0)     # pivot is the 1st element of s
    L,G = [],[]
    E = [p]
    while len(s):
        x = s.pop()     # remove the last element of s
        if x > p: L.append(x)
        elif x < p: G.append(x)
        else: E.append(x)
    quick_sort(L)
    quick_sort(G)
    s.extend(L)
    s.extend(E)
    s.extend(G)

if __name__ == '__main__':
    s = []
    for i in range(0,9):
        s.append(random.randint(0,20))
    
    print(s)
    quick_sort(s)
    print(s)