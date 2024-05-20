def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = max_of_two(num1, num2)
print(f"The maximum of {num1} and {num2} is {result}.")
