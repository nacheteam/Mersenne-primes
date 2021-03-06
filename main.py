################################################################################
##                            IMPORTED MODULES                                ##
################################################################################

import primes
import time
import prime_list
import threading
import properties

################################################################################
##                              GLOBAL VARIABLES                              ##
################################################################################

THREAD_NUMBER = 4
lock = threading.Lock()
prime_array = []
threads = []

################################################################################
##                             AUXILIARY FUNCTIONS                            ##
################################################################################

def checkPrime(exponent,factors):
    if primes.isPrimeLL(int(exponent),factors):
        with lock:
            prime_array.append(primes.mersennePrime(exponent))

def printPrimes(prime_list):
    print(str(len(prime_list)) + " primes were found.\n")
    for prime in prime_list:
        print(str(prime) + " is a Mersenne prime.\n")
        if primes.sophieGermainePrime(prime):
            print("It is also a Sophie's Germaine prime.\n")

################################################################################
##                                MAIN PROGRAM                                ##
################################################################################

def main():
    factors = prime_list.readPrimes()
    good_factors = prime_list.checkModulus(factors)
    for i in range(1,3500,THREAD_NUMBER):
        print(str(i))
        threads = []
        for j in range(THREAD_NUMBER):
            threads.append(threading.Thread(target = checkPrime, args = (i+j,good_factors)))
        for j in range(THREAD_NUMBER):
            threads[j].start()
        for j in range(THREAD_NUMBER):
            threads[j].join()
    printPrimes(prime_array)

start = time.clock()
main()
end = time.clock()
print("Time elapsed: " + str(end-start))
