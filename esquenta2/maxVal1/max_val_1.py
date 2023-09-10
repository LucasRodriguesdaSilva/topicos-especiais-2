def maxVal1(a, n):
    max_value = a[0]
    for i in range(1, n):
        if a[i] > max_value:
            max_value = a[i]
    
    return max_value