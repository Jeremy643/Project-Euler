def get_tri_number(i):
    tri_number = 0
    for j in range(1, i + 1):
        tri_number += j
    return tri_number


def get_tri_factors(number):
    tri_factors = []
    i = 1
    while i ** 2 <= number:
        if number % i == 0:
            tri_factors.append(i)
            if number // i != i:
                tri_factors.append(number//i)
        i += 1
    return tri_factors


def main():
    factor_limit = 500
    i = 1
    while True:
        tri_number = get_tri_number(i)
        tri_factors = get_tri_factors(tri_number)
        if len(tri_factors) > factor_limit:
            break
        i += 1
    print('The first triangular number to have more than {} factors is: {}'.format(factor_limit, tri_number))


if __name__ == '__main__':
    main()
