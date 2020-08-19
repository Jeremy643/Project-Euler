from num2words import num2words


def main():
    limit = 1001
    word_sum = 0
    for i in range(1, limit):
        word = num2words(i).replace('-', '').replace(' ', '')
        word_len = len(word)
        word_sum += word_len
    print('The sum of all written number lengths from 1 to {} is: {}'.format(limit-1, word_sum))


if __name__ == '__main__':
    main()
