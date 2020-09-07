def get_prod(i):
    limit = 10
    digits = list(map(int, [*str(i)]))
    total_prod = 1
    for j in range(i):
        prod = 0
        pw = 0
        for digit in reversed(digits):
            p = (total_prod * digit) * 10**pw
            prod += p
            pw += 1
        if len(str(prod)) < limit:
            total_prod = prod
        else:
            total_prod = int(str(prod)[-limit:])
    return total_prod


def main():
    limit = 1000
    total_sum = 0
    for i in range(1, limit+1):
        prod = get_prod(i)
        total_sum += prod
    print('Answer: {}'.format(int(str(total_sum)[-10:])))


if __name__ == '__main__':
    main()
