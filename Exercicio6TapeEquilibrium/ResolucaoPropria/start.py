def solution(A):
    list_range = len(A)

    difference_list = []

    for p in range(1, list_range):
        post_sum = sum(A[p:])
        behind_sum = sum(A[:p])

        difference = behind_sum - post_sum

        if difference < 0:
            difference *= -1

        difference_list.append(difference)

    return min(difference_list)

print(solution([3, 1, 2, 4, 3]))
