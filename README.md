# Mersenne-primes
Approach to calculating big Mersenne primes with arbitrary precision numbers.  
I'll try to do so in Python using as first approach the Lucas-Lehmer primality test for Mersenne primes.

## How it works
It makes as the first step a list of small primes allocated in `prime_list.txt` file. To generate these primes again there are two ways:  
```bash
    python3.5 -m compileall
    python3.5
```  

```python
    import prime_list
    prime_list.genPrimesEratostenes()
    prime_list.genPrimes()
```

So the two ways of generating the primes are Eratostenes and the conventional method. I recommend using Eratostenes as the normal method takes more than 20 minutes and Eratostenes just 10 seconds or less.  
After doing so you should run it as mentioned in the next section.  
What this will do is check the primes with the tips said at the bottom.  

**DISCLAIMER:** Eratostenes works really fast but it does consumes a lot of RAM as it needs an array with the same number of candidates to be prime filled with booleans for my implemmentation. This means it will take (in the best case) 32 bits * number_of_candidates (32 bits is the standard implementation in python). So that for 1.000.000.000 candidates it will be 32 bits * 1.000.000.000 = 3814 MB just for the boolean array.


## How to run it
I recommend you byte-compile it first and then run it by using:
``` bash
    python3.5 -m compileall
    python3.5 main.py
```

## Tips

- If 2^p-1 is prime then p is prime (so if p is not prime you should not check that number).  
- Use Trial Factoring to look for small factors:

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

## Contributing

**__CHECK CONTRIBUTING.md FILE__**
