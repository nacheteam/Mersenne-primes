import primes
import time
import prime_list

def main():
    prime_list = []
    factors = prime_list.readPrimes()
    for i in range(10000,10100):
        print(str(i))
        if primes.isPrimeLL(int(i),factors):
            primes.append(primes.mersennePrime(i))
    for prime in prime_list:
        print(str(prime) + " is a Mersenne prime.\n")

start = time.clock()
main()
end = time.clock()
print("Time elapsed: " + str(end-start))
