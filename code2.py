# 示例有问题的 Python 代码文件：example_buggy_code.py


def add(a, b):
    return a + b

# 逻辑错误：错误的变量名
result = add(3, 5)
print(f"The result is: {reslt}")

# 运行时错误：除以零
def divide(a, b):
    return a / b

print(divide(10, 0))

# 类型错误：字符串和整数相加
print("The answer is " + 42)