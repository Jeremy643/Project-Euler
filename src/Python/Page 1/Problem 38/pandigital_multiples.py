def next_product_size(n, number, product):
    p = n * number
    return len(product) + len(str(p))


def main():
    number = 1
    limit = 10  # the most digits a number can have
    max_pandigital = float('-inf')
    while len(str(number)) + len(str(number * 2)) < limit:
        n = 1
        product = ''
        while True:
            product += str(number * n)
            n += 1
            if next_product_size(n, number, product) >= limit:
                break
        pandigital = True
        digits = list(map(lambda x: int(x), [*product]))
        for i in range(1, 10):
            if i in digits and digits.count(i) == 1:
                continue
            else:
                pandigital = False
                break
        if pandigital and int(product) > max_pandigital:
            max_pandigital = int(product)
        number += 1
    print('Answer: {}'.format(max_pandigital))


if __name__ == '__main__':
    main()
