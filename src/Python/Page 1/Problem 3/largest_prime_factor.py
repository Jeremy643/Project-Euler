from math import sqrt

primes = {2}
value = 3
number = 600851475143
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            number /= value
print(int(number))
