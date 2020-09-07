import math


def go_right(index, direction):
    if direction == (0, 1):  # NORTH
        new_direction = (1, 0)
        new_index = (index[0]+1, index[1])
    elif direction == (1, 0):  # EAST
        new_direction = (0, -1)
        new_index = (index[0], index[1]+1)
    elif direction == (0, -1):  # SOUTH
        new_direction = (-1, 0)
        new_index = (index[0]-1, index[1])
    else:  # WEST
        new_direction = (0, 1)
        new_index = (index[0], index[1]-1)
    return new_index, new_direction


def go_forward(index, direction):
    if direction == (0, 1):  # NORTH
        new_index = (index[0], index[1]-1)
    elif direction == (1, 0):  # EAST
        new_index = (index[0]+1, index[1])
    elif direction == (0, -1):  # SOUTH
        new_index = (index[0], index[1]+1)
    else:  # WEST
        new_index = (index[0]-1, index[1])
    return new_index


def create_spiral(size):
    index = (math.floor(size/2), math.floor(size/2))
    direction = (0, 1)
    spiral = [[0 for i in range(size)] for j in range(size)]
    for i in range(1, (size*size)+1):
        x = index[0]
        y = index[1]
        spiral[y][x] = i
        new_index, new_direction = go_right(index, direction)
        if spiral[new_index[1]][new_index[0]] == 0:
            index = new_index
            direction = new_direction
        else:
            index = go_forward(index, direction)
    return spiral


def main():
    spiral_size = 1001
    spiral = create_spiral(spiral_size)
    diagonal_sum = 0
    for i in range(spiral_size):
        diagonal_sum += spiral[i][i]
        if i != (spiral_size-1)/2:
            diagonal_sum += spiral[i][-(i+1)]
    print('The sum of the diagonal of the spiral of size {}x{} is: {}'.format(spiral_size, spiral_size, diagonal_sum))


if __name__ == '__main__':
    main()
