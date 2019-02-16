## Problem 5: This problem was asked by Twitter

A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation.
For example, **[2, 1, 0]** represents the permutation where elements at the index **0** and **2** are swapped.

Given an array and a permutation, apply the permutation to the array. For example, given the array **["a", "b", "c"]** and 
the permutation **[2, 1, 0]**, return **["c", "b", "a"]**.

**Output**

Driver function implemented in the algorithm:
```
if __name__ == "__main__":  # Driver function
    original_array1 = ['a', 'b', 'c']
    permutation_array1 = [2,1,0]
    original_array2 = ['a', 'b', 'c', 'd']
    permutation_array2 = [3,0,2,1]
    print('The original array was:', original_array1)
    print('It will be swapping with the following order', permutation_array1)
    print('After swapping', permutation(original_array1, permutation_array1))
    print('The original array was:', original_array2)
    print('It will be swapping with the following order', permutation_array2)
    print('After swapping', permutation(original_array2, permutation_array2))
```
The output when  you run it on the terminal is:
```
C:\>python3 Problem5.py
The original array was: ['a', 'b', 'c']
It will be swapping with the following order [2, 1, 0]
After swapping ['c', 'b', 'a']
The original array was: ['a', 'b', 'c', 'd']
It will be swapping with the following order [3, 0, 2, 1]
After swapping ['b', 'd', 'c', 'a']
```
