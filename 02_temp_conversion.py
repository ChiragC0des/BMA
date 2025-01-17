# Description: This program converts temperature from Celsius to Fahrenheit.
# The program prompts the user to enter the temperature in Celsius and then calculates and displays the temperature in Fahrenheit.
temp = float(input("Enter the temperature in Celsius: "))

# Formula to convert Celsius to Fahrenheit: F = (C * 9/5) + 32
fahrenheit = (temp * 9/5) + 32

# Display the result with two decimal places
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f} °F")