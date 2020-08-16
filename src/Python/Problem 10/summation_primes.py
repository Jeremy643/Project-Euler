import random


def miller_rabin_test(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


def main():
    limit = 2000000
    prime_sum = 5
    for i in range(5, limit, 2):
        if miller_rabin_test(i):
            prime_sum += i
    print('The sum of all primes below {} is: {}'.format(limit, prime_sum))


if __name__ == '__main__':
    main()
