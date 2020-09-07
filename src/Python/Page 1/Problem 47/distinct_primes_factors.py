import math
import time


def get_primes(n):
    numbers = [True] * n
    numbers[0] = numbers[1] = False
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if numbers[i]:
            for j in range(i**2, n, i):
                if numbers[j]:
                    numbers[j] = False
    primes = []
    for i in range(n):
        if numbers[i]:
            primes.append(i)
    return primes


def get_prime_factors(n, primes):
    i = 0
    factors = []
    while n > 1:
        if n % primes[i] == 0:
            n /= primes[i]
            factors.append(primes[i])
        else:
            i += 1
    return factors


def main():
    c = 4
    primes = get_primes(1000000)
    i = 4
    first_value = i
    counter = 0
    start = time.time()
    while True:
        factors = list(dict.fromkeys(get_prime_factors(i, primes)))
        if len(factors) == c and counter == 0:
            first_value = i
            counter += 1
        elif len(factors) == c:
            counter += 1
        else:
            counter = 0
        if counter == c:
            print('Answer: {}'.format(first_value))
            print('Time taken = {}s'.format(time.time()-start))
            break
        i += 1


if __name__ == '__main__':
    main()
