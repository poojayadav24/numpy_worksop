def sum_of_digits(number):
    number = abs(number)
    
    total_sum = 0
    
    while number > 0:
        digit = number % 10  # Get the last digit
        total_sum += digit   # Add the digit to the sum
        number //= 10        # Remove the last digit from the number
    
    return total_sum

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is {result}.")
