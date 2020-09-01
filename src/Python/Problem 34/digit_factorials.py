import math


def main():
    dict_fac = {}
    for i in range(10):
        dict_fac[i] = math.factorial(i)
    limit = int(math.pow(10, math.log10(math.factorial(9))))
    i = 3
    total_sum = 0
    while i < limit:
        i_str = str(i)
        i_sum = 0
        for digit in i_str:
            digit_fac = dict_fac[int(digit)]
            i_sum += digit_fac
        if i_sum == i:
            total_sum += i
        i += 1
    print('Answer: {}'.format(total_sum))


if __name__ == '__main__':
    main()
