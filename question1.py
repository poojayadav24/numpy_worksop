def check_odd_or_even(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


number = int(input("Enter a number: "))
result = check_odd_or_even(number)
print(result)
