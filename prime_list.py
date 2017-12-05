import os

# Method to generate small primes in a list.
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
    primes = prime_line.split(",")
    return primes
