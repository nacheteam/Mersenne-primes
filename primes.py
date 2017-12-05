# Auxiliary functions

# Gives the corresponding Mersenne prime with the given exponent.

def mersennePrime(exponent):
    return int(pow(2,exponent)-1)

# Test wether the Mersenne prime candidate is prime with Lucas-Lehmer primality test.
# Lucas Lehmer only works with even exponents.

def isPrimeLL(exponent):
    if exponent%2==0:
        return exponent==2

    s=4
    number = mersennePrime(exponent)
    while exponent>2:
        s=int((s*s - mersennePrime(2))%number)
        exponent-=1

    return s==0;

# Obtain bit string from a number.

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

# Trial factoring to discard exponents.
# Returns false if not prime.

def trialFactoring(factors, exponent):
    previous=1
    for factor in factors:
        bits = bin(factor)
        for i in range(0,len(bits)-1):
            square = previous*previous
            if bits[i]=="1":
                square*=2
                previous = square%factor
        if previous==1:
            return False
    return True
