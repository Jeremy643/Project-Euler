def is_palindrome(number):
    reversed_number = ''.join(list(reversed([*str(number)])))
    if str(number) == reversed_number:
        return True
    else:
        return False


def to_binary(number):
    binary = bin(number)
    return binary.split('b')[1]


def main():
    limit = 1000000
    pal_sum = 0
    for i in range(limit):
        binary_i = to_binary(i)
        if is_palindrome(i) and is_palindrome(binary_i):
            pal_sum += i
    print('Answer: {}'.format(pal_sum))


if __name__ == '__main__':
    main()
