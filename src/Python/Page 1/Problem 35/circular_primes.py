import time
import itertools


def get_primes(limit):
    numbers = [True] * limit
    numbers[0] = numbers[1] = False
    primes = []
    for (i, prime) in enumerate(numbers):
        if prime:
            primes.append(i)
            for j in range(i**2, limit, i):
                numbers[j] = False
    return primes


def main():
    limit = 1000000

    start = time.time()
    primes = get_primes(limit)

    print('Stage 1: {}s'.format(time.time()-start))
    start = time.time()

    total_circular_primes = 13
    lst = []
    for i in range(3, 7):
        for j in itertools.product(['1', '3', '5', '7', '9'], repeat=i):
            lst.append(''.join(j))

    for value in lst:
        if sum(list(map(int, [*value]))) % 3 == 0:
            continue
        else:
            tmp = [*value]
            roll_i = int(value)
            flg = True
            for j in range(len(value)):
                if roll_i in primes:
                    t = tmp.pop(0)
                    tmp.append(t)
                    roll_i = int("".join(tmp))
                else:
                    flg = False
                    break
            if flg:
                total_circular_primes += 1

    print('Stage 2: {}s'.format(time.time()-start))
    print('Answer: {}'.format(total_circular_primes))


if __name__ == '__main__':
    main()
