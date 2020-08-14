def main():
    large_number_file = open("large_number", "r")
    large_number = ""
    for line in large_number_file:
        large_number += line.replace('\n', '')
    large_number_file.close()

    adjacent = 13
    max_product = float('-inf')
    for i in range(len(large_number)-adjacent+1):
        series = large_number[i:i+adjacent]
        product = 1
        for digit in series:
            product *= int(digit)
        max_product = max(max_product, product)
    print('The maximum product of the 13 digits in the number is: {}'.format(max_product))


if __name__ == '__main__':
    main()
