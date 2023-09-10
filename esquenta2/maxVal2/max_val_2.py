def maxVal2(A, init, end):
    if end - init <= 1:
        return max(A[init], A[end])
    else:
        m = (init + end) // 2
        v1 = maxVal2(A, init, m)
        v2 = maxVal2(A, m + 1, end)
        return max(v1, v2)