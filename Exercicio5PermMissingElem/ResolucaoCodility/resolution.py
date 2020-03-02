def solution(A):
    list_range = len(A)
    xor_sum = 0

    for n in range(0, list_range):
        sum_number = xor_sum ^ A[n]
        xor_sum = sum_number ^ (n + 1)
    return xor_sum ^ (list_range + 1)

