def main():
    # get numbers to sum
    numbers_file = open("numbers", "r")
    numbers = []
    for line in numbers_file:
        line = line.replace('\n', '')
        numbers.append(line)
    numbers_file.close()

    remainder = 0
    number_length = len(numbers[0])
    numbers_sum = [0] * number_length
    for digit in reversed(range(number_length)):
        for number in numbers:
            remainder += int(number[digit])
        numbers_sum[digit] = remainder % 10
        remainder //= 10
        if digit == 0:
            for i in reversed(str(remainder)):
                numbers_sum.insert(0, int(i))
    first_ten = ''
    for d in numbers_sum[:10]:
        first_ten += str(d)
    print('The first 10 digits of the sum are: {}'.format(first_ten))


if __name__ == '__main__':
    main()
