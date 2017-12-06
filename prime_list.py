import os

# Method to generate small primes in a file.
def genPrimes():
    primes = []
    for i in range(2,1299827):
        if(i%2500==0):
            os.system("clear")
            print(str(int((i/1299827)*100))+"% completado")
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
