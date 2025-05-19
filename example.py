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

# 测试代码
if __name__ == "__main__":
    result = add_numbers(5, 3)
    print(f"The sum of 5 and 3 is: {result}")
    result_multiply = multiply_numbers(5, 3)
    print(f"The product of 5 and 3 is: {result_multiply}")

    result_divide = divide_numbers(10, 2)
    print(f"The quotient of 10 and 2 is: {result_divide}")