# Mersenne-primes
Approach to calculating big Mersenne primes with arbitrary precision numbers.  
I'll try to do so in Python using as first approach the Lucas-Lehmer primality test for Mersenne primes.

## How to run it
I recommend you byte-compile it first by using:
``` bash
    python3.5 -m compileall
    python3.5 main.py
```

## Tips

- If 2^p-1 is prime then p is prime (so if p is not prime you should not check that number).  
- Use Trial Factoring to check for small factors:

23 = 10111

| Square | top | bit | mul by 2 | mod 47 |
|--------|-----|-----|----------|--------|
| 1*1=1  | 1   | 0111 | 1*2=2   |  2 |
| 2*2=4  | 0   | 111  | no      |  4  |
| 4*4=16 | 1   | 11   | 16*2=32 | 32  |
| 32*32=1024 | 1 | 11 | 1024*2=2048 | 27 |
| 27*27=729 | 1 |     | 729*2=1458 | 1  |

Thus 2^(23)=1 mod 47 and our Mersenne candidate isn't prime.

- Any factor q of 2^p-1 must be of the form 2kp+1 and q = 1 mod 8 or q = 7 mod 8.
