def main():
    goal = 200
    coins = {1, 2, 5, 10, 20, 50, 100, 200}
    ways = [0] * (goal+1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, goal+1):
            ways[i] += ways[i - coin]
    print('The total number of ways we can make {}p out of the available coins is: {}'.format(goal, ways[-1]))


if __name__ == '__main__':
    main()
