def main():
    # read in grid from text file
    grid_file = open("grid", "r")
    grid = []
    for line in grid_file:
        row = []
        line = line.replace(' ', '')  # remove spaces between numbers
        line = line.replace('\n', '')
        for i in range(0, len(line), 2):
            row.append(int(line[i] + line[i+1]))
        grid.append(row)
    grid_file.close()

    limit = 4  # number of adjacent values to consider
    max_product = float('-inf')
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # if col >= limit then BACKWARDS
            if col >= limit:
                curr_product = 1
                for i in range(limit):
                    curr_product *= grid[row][col - i]
                max_product = max(max_product, curr_product)
            # if col <= len(row)-limit then FORWARDS
            if col <= len(grid)-limit:
                curr_product = 1
                for i in range(limit):
                    curr_product *= grid[row][col + i]
                max_product = max(max_product, curr_product)
            # if row >= limit then UPWARDS
            if row >= limit:
                curr_product = 1
                for i in range(limit):
                    curr_product *= grid[row - i][col]
                max_product = max(max_product, curr_product)
            # if row <= len(col)-limit then DOWNWARDS
            if row <= len(grid[col])-limit:
                curr_product = 1
                for i in range(limit):
                    curr_product *= grid[row + i][col]
                max_product = max(max_product, curr_product)
            # if col >= limit & row <= len(col)-limit then DIAGONAL-DOWN-LEFT
            if col >= limit and row <= len(grid[col])-limit:
                curr_product = 1
                for i in range(limit):
                    curr_product *= grid[row + i][col - i]
                max_product = max(max_product, curr_product)
            # if col <= len(row)-limit & row <= len(col)-limit then DIAGONAL-DOWN-RIGHT
            if col <= len(grid)-limit and row <= len(grid[col])-limit:
                curr_product = 1
                for i in range(limit):
                    curr_product *= grid[row + i][col + i]
                max_product = max(max_product, curr_product)
    print('The largest product of {} numbers from the grid is: {}'.format(limit, max_product))


if __name__ == '__main__':
    main()
