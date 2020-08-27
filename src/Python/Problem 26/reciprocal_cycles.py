import math


def prime_factorisation(d, limit):
    primes = [i for i in range(2, limit)]
    for i in range(2, math.ceil(math.sqrt(limit))):
        if i in primes:
            for j in range(i**2, limit, i):
                if j in primes:
                    primes.remove(j)
    prime_factors = []
    while d > 1:
        if d % primes[0] == 0:
            prime_factors.append(primes[0])
            d /= primes[0]
        else:
            primes.remove(primes[0])
    return prime_factors


def main():
    limit = 1000
    max_digits = float('-inf')
    number = 2
    for d in range(2, limit):
        if math.log10(d).is_integer():
            continue
        prime_factors = prime_factorisation(d, limit)
        if prime_factors.count(2) + prime_factors.count(5) == len(prime_factors):
            # d is not recurring
            continue
        else:
            i = 0
            prev = 1
            remainders = set()
            while i < d:
                r = (prev % d) * 10
                remainders.add(r)
                prev = r
                i += 1
            r_len = len(remainders)
            if r_len > max_digits:
                max_digits = r_len
                number = d
    print('The number with the most digits in a recurring cycle is: {} with {} digits.'.format(number, max_digits))


if __name__ == '__main__':
    main()
