def solution(N):
    # def typed_number_converted_to_binary
    converted_number_to_binary = bin(int(N))[2:]

     # def spliting_number_one_from_converted_number
    real_converted_number_to_split_in_list = converted_number_to_binary.split('1')
    real_converted_number_to_split_in_list.pop()

    # def looking_for_maximum_binary_spaces
    list_max_binary_space = []
    for split in real_converted_number_to_split_in_list:
        list_max_binary_space.append(len(split))

    return max(list_max_binary_space)
