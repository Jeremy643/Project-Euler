def main():
    limit = 100
    sum_squares = 0
    square_sum = 0
    for i in range(1, limit+1):
        sum_squares += i ** 2
        square_sum += i
    square_sum **= 2
    diff = square_sum - sum_squares
    print('The difference between the sum of the squares and the square of the sum is: {}'.format(diff))


if __name__ == '__main__':
    main()
