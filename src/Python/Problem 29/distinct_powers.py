def main():
    limit = 101
    numbers = set()
    for a in range(2, limit):
        for b in range(2, limit):
            result = a ** b
            numbers.add(result)
    number_terms = len(numbers)
    print('The total number of distinct terms is: {}'.format(number_terms))


if __name__ == '__main__':
    main()
