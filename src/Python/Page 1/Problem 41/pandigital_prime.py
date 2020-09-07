from itertools import permutations
import math


def is_prime(p):
    if p <= 1:
        return False
    if p <= 3:
        return True
    for i in range(2, math.ceil(math.sqrt(p))+1):
        if p % i == 0:
            return False
    return True


def main():
    n = 10
    for i in reversed(range(1, n)):
        digits = list(map(lambda x: str(x), [j for j in range(1, i+1)]))
        perm = list(map(lambda x: int(''.join(x)), list(permutations(digits))))
        found = False
        max_p = float('-inf')
        for p in perm:
            if is_prime(p):
                found = True
                max_p = max(max_p, p)
        if found:
            print('Answer: {}'.format(max_p))
            break


if __name__ == '__main__':
    main()
