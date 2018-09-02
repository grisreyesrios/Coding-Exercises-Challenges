def fiboeven(limit):
    if limit < 2:       # Start with recursion
        return 0

    even_f0 = 0          # Initial values of  the first two fibonacci numbers
    even_f1 = 2
    total = even_f0 + even_f1

    while even_f1 <= limit:       # Calculate sum of even Fibonacci under the limit
        even_f2 = 4 * even_f1 + even_f0

        if even_f2 > limit:        # Stop the loop beyond the limit
            break

        even_f0 = even_f1         # Update the next even number
        even_f1 = even_f2
        total = total + even_f1
    return total


if __name__ == "__main__":  # Driver function
    limit_ex = 4000000
    print("The total sum of all the even terms in the Fibonacci sequence no higher than 4,000,000 is:",
          fiboeven(limit_ex))
