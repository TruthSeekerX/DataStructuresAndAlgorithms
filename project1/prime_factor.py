def PrimeSieve(N):
    eratos = [True]*(N+1)
    d = 2
    while d*d <= N+1:
        if eratos[d] == True:
            for i in range(d*d, N+1, d):
                eratos[i] = False
        d = d+1

    primeList = []
    for i in range(2, N+1):
        if eratos[i]:
            primeList.append(i)
    return primeList

def PrimeFactor(N):
    primeList = PrimeSieve(N)
    primeFactorList = []
    for i in primeList:
        while N%i == 0 and N > 2:
            primeFactorList.append(i)
            N = N / i
    return primeFactorList

def DistinctPrimeFactors(N):
    factorList = PrimeFactor(N)
    return set(primeFactorList)


user_input = input("Please enter an positive interger number: ")

# Convert the user input to a number (assuming it's valid)
try:
    number = int(user_input)  # Use float for both integer and decimal input
except ValueError:
    print("Invalid input. Please enter a valid number.")

print("Please input a number:")

primeFactorList = PrimeFactor(number)
print(f"Prime factors of {number}: ", PrimeFactor(number))
print(f"Distinct Prime Factors of {number}: ", DistinctPrimeFactors(number))
