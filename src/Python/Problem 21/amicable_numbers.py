def sum_divisors(n):
    sum_n = 0
    for i in range(1, n):
        if n % i == 0:
            sum_n += i
    return sum_n


def main():
    limit = 10000
    i = 3
    amicable_sum = 0
    visited = []
    while True:
        if i in visited:
            i += 1
            continue
        x = sum_divisors(i)
        y = sum_divisors(x)
        if i == y and i != x:
            amicable_sum += y
            visited.extend([i, x])
            if x < limit:
                amicable_sum += x
        i += 1
        if i == limit:
            break
    print('The sum of all amicable numbers below {} is: {}'.format(limit, amicable_sum))


if __name__ == '__main__':
    main()
