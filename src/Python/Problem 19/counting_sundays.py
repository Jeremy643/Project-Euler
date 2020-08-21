def main():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sunday = 6
    number_of_sundays = 0
    start_century_day = 0
    start_year = 1901
    end_year = 2001

    current_day = start_century_day + 365
    while start_year < end_year:
        if (start_year % 100 == 0 and start_year % 400 == 0) or (start_year % 100 != 0 and start_year % 4 == 0):
            days_in_month[1] = 29  # leap year
        else:
            days_in_month[1] = 28  # non-leap year
        for days in days_in_month:
            day = current_day % 7
            if day == sunday:
                number_of_sundays += 1
            current_day += days
        start_year += 1

    print('The number of Sundays that was the first day of the month during the 20th century was: {}'
          .format(number_of_sundays))


if __name__ == '__main__':
    main()
