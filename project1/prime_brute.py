import math

import time
st = time.time()

N = 100000000
prime_list = []

for k in range(2,N):
    s = math.floor(math.sqrt(k))
    if s*s == k: continue
    flag = True
    for i in range(2,s+1):
        if k%i == 0: 
            flag = False
            break
    if flag == True: 
        prime_list.append(k)

print(prime_list)
print(len(prime_list))

et = time.time()

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')