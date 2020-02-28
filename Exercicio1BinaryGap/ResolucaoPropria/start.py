#---- Feito em conjunto com Renan Berti e Keunan Carvalho

from Aula49.BinaryGap.functions import BinaryGap

binary_gap = BinaryGap()

number = input('Informe um número: ')
converted_number = binary_gap.typed_number_converted_to_binary(number)
real_converted_number = binary_gap.spliting_number_one_from_converted_number(converted_number)
result = binary_gap.looking_for_maximum_binary_spaces(real_converted_number)
print(result)

