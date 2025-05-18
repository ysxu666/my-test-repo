# buggy_code.py
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [1, 2, 3, 4, 5]
result = calculate_sum(numbers)
print(f"The sum is: {result}")

# Introduce a bug
print("This line will cause an error")
print(undefined_variable)