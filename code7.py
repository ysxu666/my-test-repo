
# 缺少冒号的语法错误
def add(a, b)
    return a + b

# 错误的变量名（逻辑错误）
result = add(3, 5)
print(f"The result is: {reslt}")

# 运行时错误：除以零
def divide(a, b):
    return a / b

print(divide(10, 0))

# 类型错误：字符串和整数相加
print("The answer is " + 42)
