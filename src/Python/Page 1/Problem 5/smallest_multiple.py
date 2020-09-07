import math


def get_prime_factors(i):
    primes = list(range(2, i+1))
    j = 2
    while j <= math.sqrt(i):
        if j in primes:
            for k in range(j*2, i+1, j):
                if k in primes:
                    primes.remove(k)
        j += 1
    prime_factors = []
    while i > 1:
        if i % primes[0] == 0:
            i /= primes[0]
            prime_factors.append(primes[0])
        else:
            primes.remove(primes[0])
    return prime_factors


def main():
    limit = 20
    primes_count = {2: 1, 3: 1}
    for i in range(4, limit+1):
        primes = get_prime_factors(i)
        for prime in primes:
            if prime in primes_count:
                primes_count[prime] = max(primes_count[prime], primes.count(prime))
                primes = list(filter(lambda p: p != prime, primes))
            else:
                primes_count[prime] = primes.count(prime)
                primes = list(filter(lambda p: p != prime, primes))
    lowest_multiple = 1
    for prime in primes_count:
        lowest_multiple *= prime ** primes_count[prime]
    print('The lowest multiple is: {}'.format(lowest_multiple))


if __name__ == '__main__':
    main()
