"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def find_multiple_sum(limit):
    multiple_sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            multiple_sum += i
    return multiple_sum


def main():
    limit = 1000
    multiple_sum = find_multiple_sum(limit)
    print('The sum of all of the multiples of 3 and 5 up to {} is: {}'.format(limit, multiple_sum))


if __name__ == '__main__':
    main()
