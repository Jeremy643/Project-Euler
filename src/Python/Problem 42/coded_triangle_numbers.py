def is_triangle_number(number, triangle_numbers):
    if number in triangle_numbers:
        return True
    else:
        n = len(triangle_numbers) + 1
        while True:
            t = 0.5 * n * (n + 1)
            triangle_numbers.append(t)
            n += 1
            if number == t:
                return True
            elif number < t:
                return False


def main():
    # read text file
    word_file = open("p042_words.txt", "r")
    words = word_file.read().replace('"', '').split(',')
    word_file.close()

    # get word scores
    digit_const = 96
    triangle_numbers = []
    counter = 0
    for word in words:
        score = 0
        for digit in word:
            score += ord(digit.lower()) - digit_const
        if is_triangle_number(score, triangle_numbers):
            counter += 1
    print('Answer: {}'.format(counter))


if __name__ == '__main__':
    main()
