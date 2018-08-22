## Problem 3: This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in
the original array except the one at i.

For example, if our input was **[1, 2, 3, 4, 5]**, the expected output would be **[120, 60, 40, 30, 24]**.
If our input was **[3, 2, 1]**, the expected output would be **[2, 3, 6]**.

You cannot use division

**Output**

With the driver function implemented in the algorithm:
```
if __name__ == "__main__":  # Driver function
    example_list1 = [1, 2, 3, 4, 5]
    example_list2 = [3, 2, 1]
    example_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
    examples1 = product(example_list1)
    examples2 = product(example_list2)
    examples3 = product(example_list3)
    print(examples1)
    print(examples2)
    print(examples3)
```
The output when  you run it on the terminal is:
```
C:\>python Problem3.py
[120, 60, 40, 30, 24]
[2, 3, 6]
[362880000, 181440000, 120960000, 90720000, 72576000, 60480000, 51840000, 45360000, 40320000, 36288000, 3628800]
```
