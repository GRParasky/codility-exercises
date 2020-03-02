def solution(X, Y, D):
#   X = Frog first position
#   Y = Frog position greater or equals to frog first position
#   D = Fixed distance jumped by the frog
    
    if X == Y:
        return 0

    number_of_jumps = Y / D
    distance = X // D
    real_number_of_jumps = (X - Y) // D

    if real_number_of_jumps < 0:
        real_number_of_jumps *= -1

    return real_number_of_jumps.__round__()