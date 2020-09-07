def main():
    # get triangle from file
    tri_file = open("triangle", "r")
    numbers = []
    for line in tri_file:
        row = list(map(lambda x: int(x), line.split()))
        numbers.append(row)
    tri_file.close()

    max_sums = [[numbers[0][0]]]
    for i in range(1, len(numbers)):
        row_sum = []
        for j in range(len(numbers[i])):
            if j == 0:
                row_sum.append(max_sums[i-1][0] + numbers[i][j])
            elif j == len(numbers[i])-1:
                row_sum.append(max_sums[i-1][-1] + numbers[i][j])
            else:
                row_sum.append(max(max_sums[i-1][j-1]+numbers[i][j], max_sums[i-1][j]+numbers[i][j]))
        max_sums.append(row_sum)
    print('The maximum total from top to bottom is: {}'.format(max(max_sums[-1])))


if __name__ == '__main__':
    main()
