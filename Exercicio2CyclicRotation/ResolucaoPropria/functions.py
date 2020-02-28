class CyclicRotation:
    def __init__(self, number_of_numbers, numbers_of_rotation):
        self.list_with_values = []
        self.number_of_numbers = number_of_numbers
        self.numbers_of_rotation = numbers_of_rotation

    def create_list_with_values(self):
        for i in range(self.number_of_numbers):
            i = input(f"Informe o {i+1} número")
            self.list_with_values.append(i)
        return self.list_with_values

    def rotation_list(self):
        for i in range(self.numbers_of_rotation):
            previous_list = self.list_with_values[:]
            self.list_with_values.insert(0, self.list_with_values[-1])
            self.list_with_values.pop()
            print(f"{previous_list}--->{self.list_with_values}")
