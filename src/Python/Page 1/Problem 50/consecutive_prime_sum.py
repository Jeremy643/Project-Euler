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


def main():
    limit = 1000000
    start_time = time.time()
    primes = get_primes(limit)
    max_len = 1
    max_p = float('-inf')
    for i in range(len(primes)-1):
        for j in range(i+max_len, len(primes)):
            i_sum = sum(primes[i:j])
            if i_sum > primes[-1]:
                break
            if i_sum in primes and (j - i) > max_len:
                max_len = j - i
                max_p = i_sum
    print('Answer: {}'.format(max_p))
    print('Time taken = {}s'.format(time.time()-start_time))


if __name__ == '__main__':
    main()
