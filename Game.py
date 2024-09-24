input_data = open('input.txt', 'r')
data = input_data.read()

K = int(data) # преобразование строки в число
out = K * 100 + 90 + (9 - K) # получение трехзначного числа

output_data = open('output.txt', 'w')
output_data.write(str(out))

input_data.close()
output_data.close()