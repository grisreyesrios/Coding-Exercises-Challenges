# Python programming that returns the weight of the maximum weight path in a triangle

def triangle_max_weight(arrs, level=0, index=0):
    if level == len(arrs) - 1:
        return arrs[level][index]
    else:
        return arrs[level][index] + max(
            triangle_max_weight(arrs, level + 1, index), triangle_max_weight(arrs, level + 1, index + 1)
        )

if __name__ == "__main__":  # Driver function
    arrs1 =[[1], [2, 3], [1, 5, 1]]
    print(triangle_max_weight(arrs1))
