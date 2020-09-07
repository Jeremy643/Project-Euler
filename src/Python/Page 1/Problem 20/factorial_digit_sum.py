import math


def main():
    number = 100
    number_factorial = math.factorial(number)
    fact_sum = 0
    for digit in str(number_factorial):
        fact_sum += int(digit)
    print('The sum of all of the digits of the result of doing {}! is: {}'.format(number, fact_sum))


if __name__ == '__main__':
    main()
