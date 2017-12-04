import primes
import time

def main():
    prime_list = []
    for i in range(10000,10100):
        print(str(i))
        if primes.isPrimeLL(int(i)):
            primes.append(primes.mersennePrime(i))
    for prime in prime_list:
        print(str(prime) + " is a Mersenne prime.\n")

start = time.clock()
main()
end = time.clock()
print("Time elapsed: " + str(end-start))
