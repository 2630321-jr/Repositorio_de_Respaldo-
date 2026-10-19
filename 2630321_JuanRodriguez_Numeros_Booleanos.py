# ============================================================
# NUMERIC TYPES AND BOOLEAN LOGIC IN PYTHON
# ============================================================
#
# STUDENT: Juan Rodriguez
# ENROLLMENT: 2630321
# GROUP: IM 1-1
# SUBJECT: Python Programming
# ASSIGNMENT: Numeric Types and Boolean Logic
#
# ============================================================
# EXECUTIVE SUMMARY
# ============================================================
#
# The int type stores whole numbers, while the float type stores
# numbers that can include decimal places.
# Boolean values are True and False, and comparisons produce
# these values to help programs make decisions.
# Input validation helps prevent invalid data from being used.
# Checking reasonable ranges improves the reliability of results.
# Division by zero must be avoided because it causes an error.
# This assignment contains six problems involving numeric values,
# arithmetic operations, comparisons, and logical conditions.
# Each problem includes inputs, outputs, validations, and three
# documented test cases: normal, border, and error.
#
# ============================================================
# PRINCIPLES AND GOOD PRACTICES
# ============================================================
#
# - Use int for whole-number quantities and float for decimals.
# - Store intermediate results in descriptive variables.
# - Validate user input before performing calculations.
# - Reject invalid ranges, such as negative work hours.
# - Use descriptive variable names and clear output messages.
# - Explain what True and False mean in each situation.
# - Avoid division by zero and handle conversion errors.
#
# ============================================================
# PROBLEMS 1-6 WILL BE ADDED BELOW
# ============================================================
# ============================================================
# PROBLEM 1: TEMPERATURE CONVERTER AND RANGE FLAG
# ============================================================
#
# Description:
# Converts a temperature from Celsius to Fahrenheit and Kelvin.
# It also determines whether the Celsius temperature is high.
#
# Inputs:
# - temp_c: Temperature in degrees Celsius (float).
#
# Outputs:
# - Fahrenheit: Converted temperature in Fahrenheit.
# - Kelvin: Converted temperature in Kelvin.
# - High temperature: True if temp_c >= 30.0, otherwise False.
#
# Validations:
# - The input must be convertible to float.
# - The temperature cannot be below absolute zero (-273.15 C).
# - Invalid input displays "Error: invalid input".
#
# Test cases:
# 1) Normal: temp_c = 25.0
#    Expected: Fahrenheit = 77.0, Kelvin = 298.15,
#    High temperature = False.
# 2) Border: temp_c = -273.15
#    Expected: Fahrenheit = -459.67, Kelvin = 0.0,
#    High temperature = False.
# 3) Error: temp_c = "hello"
#    Expected: "Error: invalid input".
#
def temperature_converter():
    try:
        temp_c = float(input("Enter temperature in Celsius: "))

        if temp_c < -273.15:
            print("Error: invalid input")
            return

        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", str(is_high_temperature).lower())

    except ValueError:
        print("Error: invalid input")

# ============================================================
# PROBLEM 2: WORK HOURS AND OVERTIME PAYMENT
# ============================================================
#
# Description:
# Calculates weekly pay using regular hours and overtime hours.
# Overtime hours are paid at 150% of the normal hourly rate.
#
# Inputs:
# - hours_worked: Total weekly hours worked (float).
# - hourly_rate: Payment per hour (float).
#
# Outputs:
# - Regular pay
# - Overtime pay
# - Total pay
# - Has overtime: True or False
#
# Validations:
# - hours_worked must be >= 0.
# - hourly_rate must be > 0.
# - Inputs must be convertible to float.
#
# Test cases:
# 1) Normal: hours_worked = 35, hourly_rate = 100.
#    Expected: Regular pay = 3500, Overtime pay = 0,
#    Total pay = 3500, Has overtime = false.
# 2) Border: hours_worked = 40, hourly_rate = 100.
#    Expected: Regular pay = 4000, Overtime pay = 0,
#    Total pay = 4000, Has overtime = false.
# 3) Error: hours_worked = -5, hourly_rate = 100.
#    Expected: Error: invalid input.
#
def work_hours_payment():
    try:
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))

        if hours_worked < 0 or hourly_rate <= 0:
            print("Error: invalid input")
            return

        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", str(has_overtime).lower())

    except ValueError:
        print("Error: invalid input")

# ============================================================
# PROBLEM 3: DISCOUNT ELIGIBILITY WITH BOOLEANS
# ============================================================
#
# Description:
# Determines whether a customer qualifies for a 10% discount.
# Eligibility depends on student status, senior status, or
# a purchase total of at least 1000.0.
#
# Inputs:
# - purchase_total: Purchase amount (float).
# - is_student_text: "YES" or "NO".
# - is_senior_text: "YES" or "NO".
#
# Outputs:
# - Discount eligible: True or False.
# - Final total: Amount after the applicable discount.
#
# Validations:
# - purchase_total must be >= 0.
# - Both answers must be YES or NO.
# - Text inputs are normalized to uppercase.
#
# Test cases:
# 1) Normal: 500, YES, NO. Expected: eligible = true,
#    final total = 450.0.
# 2) Border: 1000, NO, NO. Expected: eligible = true,
#    final total = 900.0.
# 3) Error: -10, YES, NO. Expected: Error: invalid input.
#
def discount_eligibility():
    try:
        purchase_total = float(input("Enter purchase total: "))
        is_student_text = input(
            "Is the customer a student? (YES/NO): "
        ).strip().upper()
        is_senior_text = input(
            "Is the customer a senior? (YES/NO): "
        ).strip().upper()

        if purchase_total < 0:
            print("Error: invalid input")
            return

        if (is_student_text not in ("YES", "NO")
                or is_senior_text not in ("YES", "NO")):
            print("Error: invalid input")
            return

        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = (
            is_student or is_senior or purchase_total >= 1000.0
        )

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", round(final_total, 2))

    except ValueError:
        print("Error: invalid input")

# ============================================================
# PROBLEM 4: BASIC STATISTICS OF THREE INTEGERS
# ============================================================
#
# Description:
# Reads three integers and calculates their sum, average,
# maximum, minimum, and whether all three numbers are even.
#
# Inputs:
# - n1, n2, n3: Three integers.
#
# Outputs:
# - Sum, Average, Max, Min, All even.
#
# Validations:
# - All inputs must be convertible to integers.
# - Negative integers are allowed.
#
# Test cases:
# 1) Normal: 2, 4, 6. Expected: sum = 12, average = 4.0,
#    max = 6, min = 2, all even = true.
# 2) Border: 0, 0, 0. Expected: sum = 0, average = 0.0,
#    max = 0, min = 0, all even = true.
# 3) Error: 2, "abc", 6. Expected: Error: invalid input.
#
def basic_statistics():
    try:
        n1 = int(input("Enter the first integer: "))
        n2 = int(input("Enter the second integer: "))
        n3 = int(input("Enter the third integer: "))

        sum_value = n1 + n2 + n3
        average_value = sum_value / 3
        max_value = max(n1, n2, n3)
        min_value = min(n1, n2, n3)
        all_even = (
            n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0
        )

        print("Sum:", sum_value)
        print("Average:", round(average_value, 2))
        print("Max:", max_value)
        print("Min:", min_value)
        print("All even:", str(all_even).lower())

    except ValueError:
        print("Error: invalid input")

# ============================================================
# PROBLEM 5: LOAN ELIGIBILITY
# ============================================================
#
# Description:
# Determines loan eligibility using monthly income, monthly
# debt, and credit score.
#
# Inputs:
# - monthly_income: Monthly income (float).
# - monthly_debt: Monthly debt payments (float).
# - credit_score: Credit score (int).
#
# Outputs:
# - Debt ratio.
# - Eligible: True or False.
#
# Validations:
# - monthly_income must be > 0.
# - monthly_debt must be >= 0.
# - credit_score must be >= 0.
# - Inputs must have the required numeric types.
#
# Test cases:
# 1) Normal: income = 10000, debt = 2000, score = 700.
#    Expected: debt ratio = 0.2, eligible = true.
# 2) Border: income = 8000, debt = 3200, score = 650.
#    Expected: debt ratio = 0.4, eligible = true.
# 3) Error: income = 0, debt = 100, score = 700.
#    Expected: Error: invalid input.
#
def loan_eligibility():
    try:
        monthly_income = float(input("Enter monthly income: "))
        monthly_debt = float(input("Enter monthly debt: "))
        credit_score = int(input("Enter credit score: "))

        if (monthly_income <= 0 or monthly_debt < 0
                or credit_score < 0):
            print("Error: invalid input")
            return

        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print("Debt ratio:", round(debt_ratio, 2))
        print("Eligible:", str(eligible).lower())

    except ValueError:
        print("Error: invalid input")

# ============================================================
# PROBLEM 6: BODY MASS INDEX AND CATEGORY FLAG
# ============================================================
#
# Description:
# Calculates BMI using weight in kilograms and height in meters.
# Classifies the calculated value into the requested categories.
#
# Inputs:
# - weight_kg: Weight in kilograms (float).
# - height_m: Height in meters (float).
#
# Outputs:
# - BMI, Underweight, Normal, Overweight.
#
# Validations:
# - weight_kg must be > 0.
# - height_m must be > 0.
# - Inputs must be convertible to float.
#
# Test cases:
# 1) Normal: weight = 70, height = 1.75.
#    Expected: BMI = 22.86, normal = true.
# 2) Border: weight = 18.5, height = 1.0.
#    Expected: BMI = 18.5, normal = true.
# 3) Error: weight = 70, height = 0.
#    Expected: Error: invalid input.
#
def calculate_bmi():
    try:
        weight_kg = float(input("Enter weight in kilograms: "))
        height_m = float(input("Enter height in meters: "))

        if weight_kg <= 0 or height_m <= 0:
            print("Error: invalid input")
            return

        bmi = weight_kg / (height_m * height_m)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", round(bmi, 2))
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())

    except ValueError:
        print("Error: invalid input")

# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        print("\n=== NUMERIC AND BOOLEAN PRACTICE MENU ===")
        print("1. Temperature converter")
        print("2. Work hours and overtime payment")
        print("3. Discount eligibility")
        print("4. Basic statistics")
        print("5. Loan eligibility")
        print("6. BMI calculator")
        print("0. Exit")

        choice = input("Choose a problem (0-6): ").strip()

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            work_hours_payment()
        elif choice == "3":
            discount_eligibility()
        elif choice == "4":
            basic_statistics()
        elif choice == "5":
            loan_eligibility()
        elif choice == "6":
            calculate_bmi()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Error: invalid input")
if __name__ == "__main__":
    main()

# ============================================================
# CONCLUSIONS
# ============================================================
#
# Integers and floating-point numbers are useful for different
# types of calculations in real programming situations.
# Comparisons produce boolean values that help programs make
# decisions using conditional statements.
# Input validation prevents invalid values from being processed.
# Checking ranges and avoiding division by zero improves safety.
# The and, or, and not operators combine logical conditions.
# These techniques are useful in payroll, discounts, loans,
# statistics, temperature conversion, and other applications.
#
# ============================================================
# REFERENCES
# ============================================================
#
# 1. Python Software Foundation. Built-in Types.
#    https://docs.python.org/3/library/stdtypes.html
#
# 2. Python Software Foundation. Numeric Types.
#    https://docs.python.org/3/library/stdtypes.html
#
# 3. Python Software Foundation. Built-in Functions.
#    https://docs.python.org/3/library/functions.html
#
# 4. Python Software Foundation. Errors and Exceptions.
#    https://docs.python.org/3/tutorial/errors.html
#
# 5. Python Software Foundation. Control Flow Tools.
#    https://docs.python.org/3/tutorial/controlflow.html
#
# 6. Python Software Foundation. Expressions.
#    https://docs.python.org/3/reference/expressions.html
