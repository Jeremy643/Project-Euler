def main():
    numbers_found = set()
    for a in range(1, 100):
        b = a
        while len(str(a)) + len(str(b)) + len(str(a * b)) <= 9:
            ab_product = a * b
            if len(str(a)) + len(str(b)) + len(str(ab_product)) < 9 or '0' in str(a) + str(b) + str(ab_product):
                b += 1
            else:
                values = [a, b, ab_product]
                digits = set()
                exit_loop = False
                for value in values:
                    for digit in str(value):
                        if digit in digits:
                            exit_loop = True
                            break
                        else:
                            digits.add(digit)
                    if exit_loop:
                        break
                if not exit_loop and ab_product not in numbers_found:
                    numbers_found.add(ab_product)
                b += 1

    product_sum = 0
    for number in numbers_found:
        product_sum += number
    print('The sum of all products is: {}'.format(product_sum))


if __name__ == '__main__':
    main()
