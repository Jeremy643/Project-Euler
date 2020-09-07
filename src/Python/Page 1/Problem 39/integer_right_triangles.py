import math


def get_c(a, b):
    return math.sqrt(a**2 + b**2)


def main():
    a = 1
    b = 2
    limit = 1000
    p_count = {}
    while True:
        while a + b + get_c(a, b) <= limit:
            c = get_c(a, b)
            p = a + b + c
            if p in p_count:
                p_count[p] += 1
            else:
                p_count[p] = 1
            b += 1
        a += 1
        b = a + 1
        if a + b + get_c(a, b) > limit:
            break
    max_p = 0
    max_p_count = 0
    for p in p_count:
        if p_count[p] > max_p_count:
            max_p_count = p_count[p]
            max_p = p
    print('Answer: {}'.format(int(max_p)))


if __name__ == '__main__':
    main()
