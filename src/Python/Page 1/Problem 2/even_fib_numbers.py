def find_even_fib_sum(limit):
    seq = [1, 2]
    even_sum = 2
    while seq[-1] + seq[-2] <= limit:
        new_value = seq[-1] + seq[-2]
        seq.append(new_value)
        if new_value % 2 == 0:
            even_sum += new_value
    return even_sum


def main():
    limit = 4000000
    even_sum = find_even_fib_sum(limit)
    print('The sum of all even fibonacci numbers, that don\'t exceed {}, is: {}'.format(limit, even_sum))


if __name__ == '__main__':
    main()
