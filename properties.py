# Module to test properties of the Mersenne primes obtained.

################################################################################
##                         GENERAL PROPERTIES FUNCTIONS                       ##
################################################################################

# Returns a list with the divisors of a given number.
def divisors(number):
    div = []
    i = 0
    while i < number/2:
        if number%i==0:
            div.append(i)
        i+=1
    return div
