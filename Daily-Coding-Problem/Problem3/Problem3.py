import numpy as np  # Import numpy


def product(entrancelist):
    if len(entrancelist) < 2:  # If list contains less than 2 elements an alert pop out
        print("It is needed at least two numbers")
    before_element = []  # List that contains the product of all the integers before element "i"
    for i in entrancelist:
        if before_element:
            before_element.append(np.prod(before_element[-1] * i))
        else:
            before_element.append(i)

    after_element = []  # List that contains the product of all the integers after element "i"
    for i in reversed(entrancelist):
        if after_element:
            after_element.append(np.prod(after_element[-1] * i))
        else:
            after_element.append(i)
    after_element = list(reversed(after_element))

    final_result = []  # Storing the total product of all other integers
    for i in range(len(entrancelist)):
        if i == 0:
            final_result.append(after_element[i + 1])
        elif i == len(entrancelist) - 1:
            final_result.append(before_element[i - 1])
        else:
            final_result.append(np.prod(before_element[i - 1] * after_element[i + 1]))
    return final_result


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
