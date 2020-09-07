import math
from itertools import permutations
from itertools import combinations


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
    primes = list(filter(lambda x: x >= 1000, primes))
    return primes


def find_combo(p):
    r = 3
    combo = list(combinations(p, r))
    for c in combo:
        diff1 = abs(c[0] - c[1])
        diff2 = abs(c[1] - c[2])
        if diff1 == diff2:
            return c
    return ()


def main():
    stop = 10000
    primes = get_primes(stop)
    must_remove = [1487, 4817, 8147]
    for must in must_remove:
        primes.remove(must)
    for prime in primes:
        perm = list(filter(lambda x: 1000 <= x <= 9999, map(lambda x: int(''.join(x)), permutations(str(prime)))))
        perm_primes = list(dict.fromkeys(filter(lambda x: x in primes, perm)))
        if len(perm_primes) < 3:
            continue
        valid_combo = find_combo(perm_primes)
        if valid_combo:
            answer = ''
            for c in valid_combo:
                answer += str(c)
            print('Answer: {}'.format(answer))
            break


if __name__ == '__main__':
    main()
