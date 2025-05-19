# 文件名: example.py

def add_numbers(a, b):
    """返回两个数字的和"""
    return a + b
def multiply_numbers(a, b):
    """返回两个数字的乘积"""
    return a * b

def divide_numbers(a, b):
    """返回两个数字的商"""
    return a / b

def subtract_numbers(a, b):
    """返回两个数字的差"""
    return a - b

def power_numbers(a, b):
    """返回 a 的 b 次方"""
    return a ** b

def modulo_numbers(a, b):
    """返回两个数字的模"""
    return a % b

def square_root(a):
    """返回数字的平方根"""
    return a ** 0.5

# 测试代码
if __name__ == "__main__":
    result = add_numbers(5, 3)
    print(f"The sum of 5 and 3 is: {result}")
    result_multiply = multiply_numbers(5, 3)
    print(f"The product of 5 and 3 is: {result_multiply}")

    result_divide = divide_numbers(10, 2)
    print(f"The quotient of 10 and 2 is: {result_divide}")

    result_subtract = subtract_numbers(10, 5)
    print(f"The difference between 10 and 5 is: {result_subtract}")

    result_power = power_numbers(2, 3)
    print(f"2 to the power of 3 is: {result_power}")

    result_modulo = modulo_numbers(10, 3)
    print(f"The remainder of 10 divided by 3 is: {result_modulo}")

    result_sqrt = square_root(16)
    print(f"The square root of 16 is: {result_sqrt}")