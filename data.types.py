# =========================================================
# 🐍 PYTHON BASICS PRACTICE FILE
# =========================================================


# =========================================================
# 1. VARIABLES & DATA TYPES
# =========================================================

# x = 10
# name = "Hamze"
# price = 9.99
# is_ready = True

# print(x)
# print(name)
# print(price)
# print(is_ready)

# age = 24
# print(age)

# name = "Hamse Mohamed"
# print(name)

# isStudent = False
# print(isStudent)


# =========================================================
# 2. TYPE CONVERSION
# =========================================================

# print(int("123"))


# =========================================================
# 3. COMMENTS
# =========================================================

# This is a comment


# =========================================================
# 4. INPUT & OUTPUT (BASICS)
# =========================================================

# name = input("What is your name? ")
# print("Hello " + name + "! Welcome to Python programming.")

# age = input("How old are you?")
# print("You are " + age + " Years old.")


# =========================================================
# 5. BMI CALCULATOR
# =========================================================

# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kilograms: "))

# bmi = weight / (height ** 2)

# print(f"Your BMI is: {bmi:.2f}")


# =========================================================
# 6. CONDITIONALS (IF / ELSE)
# =========================================================

# number = 23

# if number % 2 == 0:
#     print("the number is even")
# else:
#     print("the number is odd")


# grade = int(input("Enter your grade: "))

# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# else:
#     print(f"Your grade is {grade}. You need to work harder.")


# =========================================================
# 7. MATH MODULE (CIRCLE CALCULATIONS)
# =========================================================

# import math

# radius = float(input("Enter the radius of the circle: "))

# circumference = 2 * math.pi * radius
# area = math.pi * radius ** 2

# print(f"The circumference of the circle is: {circumference:.2f}")
# print(f"The area of the circle is: {area:.2f}")


# =========================================================
# 8. CONVERTERS (WEIGHT & TEMPERATURE)
# =========================================================

# -------------------------
# Weight Converter
# -------------------------

# weight = float(input("Enter your weight in kilograms: "))
# unit = input("Enter unit (K for kg, P for pounds): ")

# if unit == "K" or unit == "k":
#     weight_in_pounds = weight * 2.20462
#     print(f"Your weight in pounds is: {weight_in_pounds:.2f}")
# elif unit == "P" or unit == "p":
#     weight_in_kilograms = weight / 2.20462
#     print(f"Your weight in kilograms is: {weight_in_kilograms:.2f}")
# else:
#     print("Invalid unit. Please enter 'K' or 'P'.")


# -------------------------
# Temperature Converter
# -------------------------

# temp = float(input("Enter the temperature: "))
# unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")

# if unit == "C" or unit == "c":
#     temp_in_fahrenheit = (temp * 9/5) + 32
#     print(f"Temperature in Fahrenheit: {temp_in_fahrenheit:.2f} F")
# elif unit == "F" or unit == "f":
#     temp_in_celsius = (temp - 32) * 5 / 9
#     print(f"Temperature in Celsius: {temp_in_celsius:.2f} C")
# else:
#     print("Invalid unit. Please enter 'C' or 'F'.")


# =========================================================
# 9. LOGICAL OPERATORS
# =========================================================

# age = int(input("Enter your age here: "))

# if age >= 18 and age < 65:
#     print("You are an adult.")
# elif age >= 65:
#     print("You are a senior citizen.")
# else:
#     print("You are a minor.")




# =========================================================
# ternarry operator

 # use this formula for ternary operator  
# result = "Yes" if condition else "No"


# age = int(input("Enter your age here: "))

# result  = "Adult" if age >= 18 else "Minor"

# print(result)


# temperature = float(input("Enter the temperature: "))

# result = "Hot" if temperature > 30 else "Cold"

# print(result)



# grade = int(input("Enter your grade here: "))

# result  = "Pass" if grade > 50 else "Fail"

# print(result)





## String in Python


name =  input("Enter your name here: ")

result = len(name)
result1 = name.rfind("h")

print(result)
print(result1)



