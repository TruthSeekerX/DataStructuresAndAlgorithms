import time
st = time.time()

N = 1000
eratos = [True]*(N+1)
d = 2
while d*d <= N+1:
    if eratos[d] == True:
        for i in range(d*d, N+1, d):
            eratos[i] = False
    d = d+1

prime_list = []
for i in range(2, N+1):
    if eratos[i]:
        prime_list.append(i)

print(prime_list)
print(len(prime_list))

et = time.time()

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')