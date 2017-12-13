################################################################################
##                            IMPORTED MODULES                                ##
################################################################################

import prime_list

################################################################################
##                          PRIMES CHECKING FUNCTIONS                         ##
################################################################################

# Gives the corresponding Mersenne prime with the given exponent.
def mersennePrime(exponent):
    return int(pow(2,exponent)-1)

# True if the number is a Sophie's Germaine prime.
def sophieGermainePrime(number):
    return isPrime(2*number+1)

# Simple primality test.
def isPrime(number):
    i = 2
    while i <= number/2:
        if number%i==0:
            return False
    return True

# Test wether the Mersenne prime candidate is prime with Lucas-Lehmer primality test.
# Lucas Lehmer only works with even exponents.
def isPrimeLL(exponent,factors):
    if not trialFactoring(factors,exponent):
        return  False;
    if exponent%2==0:
        return exponent==2

    s=4
    number = mersennePrime(exponent)
    while exponent>2:
        s=int((s*s - 2)%number)
        exponent-=1

    return s==0;

# Trial factoring to discard exponents.
# Returns false if not prime.
def trialFactoring(factors, exponent):
    for factor in factors:
        if factor%(2*exponent)==1:
            if exponent%factor==0:
                return False
    return True

################################################################################
##                            AUXILIARY FUNCTIONS                             ##
################################################################################

# Obtain bit string from a number.ss
def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)
