import math


def is_composite(n):
    n_sum = sum(map(int, [*str(n)]))
    if n_sum % 3:
        return True
    for i in range(5, math.ceil(math.sqrt(n))+1, 2):
        if n % i == 0:
            return True
    return False


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


def main():
    i = 35
    primes = get_primes(1000000)
    while True:
        if is_composite(i):
            found = False
            for prime in primes:
                if prime > i:
                    break
                else:
                    diff = i - prime
                    for j in range(math.ceil(math.sqrt(diff))+1):
                        if (2 * (j ** 2)) == diff:
                            found = True
                            break
                    if found:
                        break
            if not found:
                print('Answer: {}'.format(i))
                break
        i += 2


if __name__ == '__main__':
    main()
