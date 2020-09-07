def main():
    # get names from file
    name_file = open("p022_names.txt", "r")
    names = name_file.read().replace('"', '').split(',')
    name_file.close()

    # sort names alphabetically
    names = sorted(names)

    # calculate alphabetical value for each name
    name_alphabetical_value = []
    position_constant = 64
    for name in names:
        name_sum = 0
        for letter in name:
            name_sum += ord(letter) - position_constant
        name_alphabetical_value.append(name_sum)

    # calculate name score by multiplying the alphabetical value with the index
    index = 1
    name_score = []
    for alphabetical_value in name_alphabetical_value:
        name_score.append(alphabetical_value * index)
        index += 1

    # calculate the sum of all name scores
    name_score_sum = sum(name_score)
    print('The sum of all name scores for the given names is: {}'.format(name_score_sum))


if __name__ == '__main__':
    main()
