def main():
    limit = 1000
    number = str(2 ** limit)
    number_sum = 0
    for digit in number:
        number_sum += int(digit)
    print('The sum is: {}'.format(number_sum))


if __name__ == '__main__':
    main()
