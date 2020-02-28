def solution(A, K):
    
    if not A:
        return A
    
    number_of_rotation = K

    for i in range(K):
        A.insert(0, A[-1])
        A.pop()
    return A