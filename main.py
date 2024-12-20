# Solving problems for the lesson "Basic data structures"

# task 1: Arithmetic
# 1st program
print(9 ** 0.5 * 5)

# task 2: Logic
# 2st program
print(9.99 > 9.98 and 1000 != 1000.1)

# task 3: A school riddle
# 3rd program
print(2 * 2 + 2)
print(2 * (2 + 2))

print(2 * 2 + 2 == 2 * (2 + 2))
# this is also correct but clearer
print((2 * 2 + 2) == (2 * (2 + 2)))

# task 4: The first one after the dot
# 4th program
number_string: str = '123.456'
print(int((float(number_string) * 10) % 10))
# alternative variant
print(number_string[number_string.find('.') + 1])

