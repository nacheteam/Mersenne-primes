import primes
import time

def main():
    prime_list = []
    factors = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]
    for i in range(10000,10100):
        if primes.trialFactoring(factors,i):
            print(str(i))
            if primes.isPrimeLL(int(i)):
                primes.append(primes.mersennePrime(i))
    for prime in prime_list:
        print(str(prime) + " is a Mersenne prime.\n")

start = time.clock()
main()
end = time.clock()
print("Time elapsed: " + str(end-start))
