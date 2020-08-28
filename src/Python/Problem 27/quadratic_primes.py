import math


def get_primes(n=10000):
    primes = [i for i in range(2, n)]
    for i in range(2, math.ceil(math.sqrt(n))):
        if i in primes:
            for j in range(i**2, n, i):
                if j in primes:
                    primes.remove(j)
    return primes


def is_prime(p):
    if p == 2 or p == 3:
        return True
    elif p % 2 == 0:
        return False
    else:
        for i in range(3, p, 2):
            if p % i == 0:
                return False
        return True


def main():
    prime_limit = 20000
    primes = get_primes(prime_limit)

    limit = 1000
    max_n = float('-inf')
    max_a = 0
    max_b = 0
    for a in range(-limit+1, limit):
        for b in range(2, limit+1):
            n = 0
            while True:
                p = (n ** 2) + (a * n) + b
                if p < 2 or p not in primes and not is_prime(p):
                    break
                else:
                    n += 1
            if n > max_n:
                max_n = n
                max_a = a
                max_b = b
    product_ab = max_a * max_b
    print('The product of a ({}) and b ({}) that gives us the most consecutive primes is: {}'
          .format(max_a, max_b, product_ab))


if __name__ == '__main__':
    main()
