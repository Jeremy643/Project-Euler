import math


def is_prime(number):
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True


def main():
    limit = 10001
    counter = 0
    number = 2
    while counter < limit:
        if is_prime(number):
            counter += 1
        if counter == limit:
            break
        elif number == 2:
            number += 1
        else:
            number += 2
    print('The 10001st prime number is: {}'.format(number))


if __name__ == '__main__':
    main()
