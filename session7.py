def print_number(number):
    print(number)

    if number<11:
        print_number(number+1)

print_number(1)