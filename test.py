def arithmetic_sequence(start, step, length):
    current = start
    for _ in range(length):
        yield current
        current += step

sequence_length = 9999999999
with open('arithmetic_sequence.txt', 'w') as file:
    for num in arithmetic_sequence(60000000000, 1, sequence_length):
        file.write(str(num) + '\n')

print("Arithmetic sequence saved to 'arithmetic_sequence.txt'.")
