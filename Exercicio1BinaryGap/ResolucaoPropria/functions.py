class BinaryGap:
    def typed_number_converted_to_binary(self, typed_number):
        converted_number_to_binary = bin(int(typed_number))
        return converted_number_to_binary[2:]

    def spliting_number_one_from_converted_number(self, converted_number):
        real_converted_number_to_split_in_list = converted_number.split('1')
        real_converted_number_to_split_in_list.pop()
        return real_converted_number_to_split_in_list


    def looking_for_maximum_binary_spaces(self, real_converted_number):
        list_max_binary_space = []
        for split in real_converted_number:
            list_max_binary_space.append(len(split))

        return f"O maior número de zeros entre dois números um é: {max(list_max_binary_space)}"