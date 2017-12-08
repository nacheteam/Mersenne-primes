import os

MAX_NUMBER_TO_CHECK = 1299821

# Generate primes with eratostenes method.
def genPrimesEratostenes():
    real_primes=[]
    primes = dict()
    for i in range(2,MAX_NUMBER_TO_CHECK):
        primes[i]=True
    for i in range(2,MAX_NUMBER_TO_CHECK):
        if(i%2500==0):
            os.system("clear")
            print(str(int((i/MAX_NUMBER_TO_CHECK)*100))+"% completado")
        for j in range(i+i,MAX_NUMBER_TO_CHECK,i):
            primes[j]=False
    for i in range(2,MAX_NUMBER_TO_CHECK):
        if primes[i]:
            real_primes.append(i)
    #return real_primes
    f = open("prime_list.txt", "w")
    for prime in real_primes:
        f.write(str(prime) + ",")
    f.close()
    f = open("prime_list.txt", "r")
    prime_line = f.read()
    f.close()
    f = open("prime_list.txt", "w")
    f.write(prime_line[:-2])
    f.close()


# Method to generate small primes in a file.
def genPrimes():
    primes = []
    for i in range(2,MAX_NUMBER_TO_CHECK):
        if(i%2500==0):
            os.system("clear")
            print(str(int((i/MAX_NUMBER_TO_CHECK)*100))+"% completado")
        prime=True
        for j in range(2,int(i/2+1)):
            if i%j==0:
                prime=False
                break
        if prime:
            primes.append(i)
    f = open("prime_list.txt", "w")
    for i in range(len(primes)-2):
        f.write(str(primes[i]) + ",")
    f.write(str(primes[-1]))

# Obtain prime list from txt.
def readPrimes():
    f = open("prime_list.txt", "r")
    prime_line = f.read()
    primes_str = prime_line.split(",")
    primes=[]
    for prime_str in primes_str:
        primes.append(int(prime_str))
    return primes


# Filter primes that are 1 or 7 modulus 8.
def checkModulus(factors):
    new_factors=[]
    for factor in factors:
        if factor%8==1 or factor%8==7:
            new_factors.append(factor)
    return new_factors
