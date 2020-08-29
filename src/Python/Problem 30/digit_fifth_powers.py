def main():
    n_power = 5
    total_sum = 0
    for i in range(2, 200000):
        value = 0
        for digit in str(i):
            value += (int(digit) ** n_power)
        if i == value:
            total_sum += i
    print('The sum is: {}'.format(total_sum))


if __name__ == '__main__':
    main()
