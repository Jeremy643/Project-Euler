def main():
    for m in range(2, 101):
        for n in range(1, m):
            a = (m ** 2) - (n ** 2)
            b = 2 * m * n
            c = (m ** 2) + (n ** 2)
            sum_abc = a + b + c
            if sum_abc == 1000:
                product = a * b * c
                print('a = {}, b = {}, c = {} | abc = {}'.format(a, b, c, product))


if __name__ == '__main__':
    main()
