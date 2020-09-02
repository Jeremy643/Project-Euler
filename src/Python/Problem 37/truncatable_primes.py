import math


def is_prime(p):
    if p <= 1:
        return False
    if p <= 3:
        return True
    if (p % 2 == 0) or (p % 3 == 0):
        return False
    for i in range(2, math.ceil(math.sqrt(p))+1):
        if p % i == 0:
            return False
    return True


def next_prime(n):
    number = n + 1
    while True:
        if is_prime(number):
            return number
        else:
            number += 1


def is_truncatable(n):
    for i in range(1, len(str(n))):
        # left to right
        ltr = int(str(n)[i:])
        if not is_prime(ltr):
            return False

        # right to left
        rtl = int(str(n)[:-i])
        if not is_prime(rtl):
            return False
    return True


def main():
    found = 0
    limit = 11
    prime = 11
    trunc_sum = 0
    while found < limit:
        if is_truncatable(prime):
            print(prime)
            found += 1
            trunc_sum += prime
            prime = next_prime(prime)
        else:
            prime = next_prime(prime)
    print('Answer: {}'.format(trunc_sum))


if __name__ == '__main__':
    main()
