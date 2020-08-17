def collatz_seq(number_steps, n, counter):
    # n even: n = n / 2
    # n odd: n = 3n + 1
    if n == 1:
        return counter+1
    elif n in number_steps:
        return number_steps[n]
    else:
        if n % 2 == 0:
            new_counter = collatz_seq(number_steps, n/2, counter+1)
        else:
            new_counter = collatz_seq(number_steps, (3*n)+1, counter+1) + 1
        number_steps[n] = new_counter
        return new_counter


def main():
    limit = 1000000
    number_steps = {2: 2}
    for i in range(3, limit):
        if i not in number_steps:
            collatz_seq(number_steps, i, 0)
    max_val = float('-inf')
    longest_starter = 2
    for key in number_steps:
        if number_steps[key] > max_val:
            max_val = number_steps[key]
            longest_starter = key
    print('The start value that gives us the longest sequence is: {}'.format(longest_starter))


if __name__ == '__main__':
    main()
