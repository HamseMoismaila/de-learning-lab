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


# name =  input("Enter your name here: ")

# result = len(name)
# result1 = name.rfind("h")

# print(result)
# print(result1)


# all about string in python 

# 


# Variables & Data Types









########################################################################

# """
# ========================================
# 📦 PYTHON DATA TYPES (DATA ENGINEERING)
# ========================================
# """

# # Basic data types
# user_id = 101            # int
# price = 9.99            # float
# name = "hamze"          # str
# is_active = True        # bool
# missing_value = None    # None (similar to NULL in SQL)


# """
# ========================================
# 🔍 TYPE CHECKING (VALIDATION)
# ========================================
# """

# # Always validate types before processing data
# value = 100
# print(type(value))

# # WHY?
# # Prevent pipeline errors when handling messy data


# """
# ========================================
# 🔄 TYPE CONVERSION (VERY IMPORTANT)
# ========================================
# """

# # Example: Data from CSV / API
# row = {
#     "name": "hamse",
#     "age": 25,
#     "salary": "3000.50"   # string (common in CSV)
# }

# # Convert before using
# age = int(row["age"])
# salary = float(row["salary"])

# for key, value in row.items():
#     print(key, value)

# # NOTE:
# # CSV → everything is STRING → must convert before analysis


# """
# ========================================
# ➕ OPERATORS (DATA TRANSFORMATION)
# ========================================
# """

# price = 99.99
# tax = 0.3

# final_price = price + (price * tax)

# print(f"The price after tax is {final_price}")

# # Use cases:
# # - Feature engineering
# # - Aggregations
# # - Calculated fields


# """
# ========================================
# 🔁 FILTERING DATA (LIST COMPREHENSION)
# ========================================
# """

# users = [
#     {"name": "Ali", "age": 17},
#     {"name": "Sara", "age": 22}
# ]

# # Get adults
# adults = [u for u in users if u["age"] > 18]
# print(adults)

# # Get only names
# names = [u["name"] for u in users if u["age"] > 18]
# print(names)

# # Equivalent (classic loop)
# adult = []
# for u in users:
#     if u["age"] > 18:
#         adult.append(u)

# print(adult)


# users = [
#     {"name": "Ali", "age": 17},
#     {"name": "Sara", "age": 22},
#     {"name": "John", "age": 19}
# ]


# # young = [u for u in users if u["age"] < 20]

# # print(young)


# # younger = []

# # for u in users:
# #     if u["age"] < 20:
# #        younger.append(u)

# # print(younger)


# count = 0

# for u in users:
#     if u["age"] >= 18:
#         count = count + 1

# print(count)  

# products = [
#     {"name": "Laptop", "price": 3000},
#     {"name": "Mouse", "price": 50},
#     {"name": "Keyboard", "price": 150}
# ]



# less_200 = [u for u in products if u["price"] < 200]

# print(less_200)

# sum = 0

# for u in products:
#     sum = sum + u["price"]

# print(sum)



# transactions = [
#     {"user": "Ali", "amount": "RM200"},
#     {"user": "Sara", "amount": "RM150"},
#     {"user": "John", "amount": "RM300"}
# ]


# for tran in transactions:

#        user = tran["user"]
#        amount = tran["amount"]

#        amount = amount.replace("RM","")

#        print(user, amount)




users = [
    {"name": "Ali", "age": 17, "active": True},
    {"name": "Sara", "age": 22, "active": False},
    {"name": "John", "age": 25, "active": True}
]


# get names of users who are active and older than 18


# young_active = [ u["name"] for u in users if u["age"] > 18 and u["active"] == True]


# print(young_active)


# orders = [
#     {"id": 1, "user": "Ali", "amount": 200},
#     {"id": 2, "user": "Sara", "amount": 500},
#     {"id": 3, "user": "Ali", "amount": 300}
# ]

# result = {}


# for order in orders:
#     user = order["user"]
#     amount = order["amount"]

#     print(user, order)








# """
# ========================================
# 🧠 BOOLEAN LOGIC (DATA CLEANING RULES)
# ========================================
# """

# # Validate realistic ages
# for u in users:
#     if u["age"] > 0 and u["age"] < 120:
#         print("Valid age:", u["age"])

# # Best practice (safe validation)
# valid_users = [
#     u for u in users
#     if "age" in u and isinstance(u["age"], int) and 0 < u["age"] < 120
# ]

# print(valid_users)

# # Use cases:
# # - Data validation rules
# # - Filtering bad records


# """
# ========================================
# 🧾 F-STRINGS (LOGGING & DEBUGGING)
# ========================================
# """

# user_id = 102
# print(f"Processing user {user_id}")

# # Use cases:
# # - Logs
# # - Debug messages
# # - Dynamic file paths


# """
# ========================================
# 🧹 STRING METHODS (DATA CLEANING)
# ========================================
# """

# # Uppercase
# country = "malaysia"
# print(country.upper())

# # Remove whitespace
# name = " Hamse  "
# print(name.strip())

# # Split raw data (CSV-like)
# line = "Ali, 25, Engineer"
# data = line.split(",")
# print(data)

# # Fix dirty data
# text = "RM100"
# clean = text.replace("RM", "")
# print(clean)

# # Old formatting
# file_name = "data_{}.csv".format(2026)
# print(file_name)

# # Modern (recommended)
# file_name1 = f"data_{2026}.csv"
# print(file_name1)







# Mini Data Pipeline 


# row_data = [
#     "Ali,25,RM3000",
#     "Sara, 30 ,RM4000",
#     "John,17,RM2000"
# ]

# clean_data = []

# for row in row_data:
#     name, age, salary = row.split(",")

#     name = name.strip().upper()
#     age = int(age.strip())
#     salary = float(salary.replace("RM", " ").strip())

#     if age > 18:
#         clean_data.append({
#             "name" : name,
#             "age" : age,
#             "salary" : salary
#         })
# print(clean_data)



transactions = [
    " 1001 , Ali , RM250.50 , success ",
    "1002,Sara,RM300.00,FAILED",
    "1003 , John , RM-50 , success",
    "1004, Aisha , RM400 , success ",
    "1005, , RM500 , success",
    "1006, Mike, RMabc , success"
]

clean_data = []

for tran in transactions:
    try:
        parts = tran.split(",")

        id = int(parts[0].strip())
        name = parts[1].strip().upper()
        amount_str = parts[2].strip()
        status = parts[3].strip().lower()

        # remove RM
        amount_str = amount_str.replace("RM", "")

        # convert safely
        amount = float(amount_str)

        # validation
        if status == "success" and name != "" and amount > 0:
            clean_data.append({
                "id": id,
                "name": name,
                "amount": amount,
                "status": status
            })

    except ValueError:
        continue

print(clean_data)