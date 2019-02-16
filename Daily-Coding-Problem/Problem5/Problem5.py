# A permutation can be specified by an array P, where P[i] represents the
# location of the element at i in the permutation.
# For example, [2, 1, 0] represents the permutation where elements at
# the index 0 and 2 are swapped.

def permutation(original_array, permutation_array):
    for i in range(len(original_array)):
        element, j = original_array[i], permutation_array[i]

        while j != i:
            original_array[j], element = element, original_array[j]
            permutation_array[j], j = j, permutation_array[j]
            original_array[i], permutation_array[i] = element, j
            return original_array
