# Project Euler Problem1


def sum_multiples(x):
    total_sum = sum(x for x in range(x) if (x % 3 == 0 or x % 5 == 0))
    return total_sum


try:
    multiples_range = int(input('Please enter a range to compute the multiples of 3 and 5:'))
    total_multiples = sum_multiples(multiples_range)
    print(total_multiples)
except ValueError:
    print("Invalid input, please introduce only integers and below 1 000 000")
    quit()
