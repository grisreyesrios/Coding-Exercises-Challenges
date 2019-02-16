import Problem5

def test_permutation():
    original_array1 = ['a', 'b', 'c']
    permutation_array1 = [2,1,0]
    original_array2 = ['a', 'b', 'c', 'd']
    permutation_array2 = [3,0,2,1]
    assert Problem5.permutation(original_array1, permutation_array1) == ['c', 'b', 'a']
    assert Problem5.permutation(original_array2, permutation_array2) == ['d', 'b', 'c', 'a']
