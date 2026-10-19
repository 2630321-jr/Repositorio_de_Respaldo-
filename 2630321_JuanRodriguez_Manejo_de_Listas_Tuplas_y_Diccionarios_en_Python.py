# ============================================================
# COVER PAGE
# Title: Manejo de Listas, Tuplas y Diccionarios en Python
# Student: Juan Rodriguez
# Student ID: 2630321
# Group: IM 1-1
# Subject: Python Programming
# ============================================================

# ============================================================
# EXECUTIVE SUMMARY
# A list is an ordered and mutable collection of elements.
# A tuple is an ordered and immutable collection of elements.
# A dictionary stores data as key-value pairs.
# Lists allow elements to be added, removed, and sorted.
# Tuples are useful for fixed data, such as coordinates.
# Dictionaries make it easier to find information using keys.
# This assignment contains six practical programming problems.
# Each problem documents inputs, outputs, validations, and test cases.
# The examples cover products, coordinates, grades, words, and contacts.
# ============================================================

# ============================================================
# PRINCIPLES AND GOOD PRACTICES
# - Use lists when items must be added or removed frequently.
# - Use tuples for data that should not change.
# - Use dictionaries to search information by name, ID, or code.
# - Avoid modifying a list while iterating over it with a for loop.
# - Use descriptive dictionary keys such as name, age, and price.
# - Write readable code and clear messages for users.
# ============================================================

import math
import string


# ============================================================
# PROBLEM 1: SHOPPING LIST BASICS
#
# Description:
# Create a list of products, add a new product, count the items,
# and search for a specific product.
#
# Inputs:
# - initial_items_text: comma-separated product names.
# - new_item: product name to add.
# - search_item: product name to find.
#
# Outputs:
# - Items list, total items, and found status.
#
# Validations:
# - Reject empty initial text, new item, or search item.
# - Split products by commas and remove extra spaces.
# - Reject a list without valid product names.
#
# Test cases:
# 1) Normal: "apple, banana", add "orange", search "banana".
#    Expected: 3 items and Found item: true.
# 2) Border: "apple", add "apple", search "pear".
#    Expected: 2 items and Found item: false.
# 3) Error: initial text is empty.
#    Expected: Error: invalid input.
# ============================================================
def problem_1():
    print("\nProblem 1: Shopping list")

    initial_items_text = input(
        "Enter initial items separated by commas: "
    ).strip()

    if not initial_items_text:
        print("Error: invalid input")
        return

    items_list = [
        item.strip()
        for item in initial_items_text.split(",")
        if item.strip()
    ]

    if not items_list:
        print("Error: invalid input")
        return

    new_item = input("Enter a new item: ").strip()
    search_item = input("Enter an item to search for: ").strip()

    if not new_item or not search_item:
        print("Error: invalid input")
        return

    items_list.append(new_item)
    is_in_list = search_item in items_list

    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", str(is_in_list).lower())


# ============================================================
# PROBLEM 2: POINTS AND DISTANCES WITH TUPLES
#
# Description:
# Represent two points using tuples, calculate their Euclidean
# distance, and calculate the midpoint between the points.
#
# Inputs:
# - x1, y1, x2, y2: numeric coordinates.
#
# Outputs:
# - Point A, Point B, distance, and midpoint.
#
# Validations:
# - All four coordinates must be convertible to float.
# - Reject non-numeric coordinates.
#
# Test cases:
# 1) Normal: A=(0, 0), B=(3, 4).
#    Expected: distance 5.0 and midpoint (1.5, 2.0).
# 2) Border: A=(2, 2), B=(2, 2).
#    Expected: distance 0.0 and midpoint (2.0, 2.0).
# 3) Error: x1="hello".
#    Expected: Error: invalid input.
# ============================================================
def problem_2():
    print("\nProblem 2: Points and distances")

    try:
        x1 = float(input("Enter x1: ").strip())
        y1 = float(input("Enter y1: ").strip())
        x2 = float(input("Enter x2: ").strip())
        y2 = float(input("Enter y2: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2
    )

    midpoint = (
        (x1 + x2) / 2,
        (y1 + y2) / 2
    )

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)


# ============================================================
# PROBLEM 3: PRODUCT CATALOG WITH DICTIONARY
#
# Description:
# Store product names and prices in a dictionary.
# Find a product and calculate its total cost.
#
# Inputs:
# - product_name: product name.
# - quantity: positive integer.
#
# Outputs:
# - Unit price, quantity, and total price.
#
# Validations:
# - Product name cannot be empty.
# - Quantity must be an integer greater than zero.
# - The product must exist in the catalog.
#
# Test cases:
# 1) Normal: apple, quantity 2.
#    Expected: unit price 10.0 and total 20.0.
# 2) Border: notebook, quantity 1.
#    Expected: total 25.0.
# 3) Error: quantity 0 or unknown product.
#    Expected: an appropriate error message.
# ============================================================
def problem_3():
    print("\nProblem 3: Product catalog")

    product_prices = {
        "apple": 10.0,
        "banana": 7.5,
        "notebook": 25.0,
        "pen": 8.0
    }

    product_name = input(
        "Enter product name: "
    ).strip().lower()

    if not product_name:
        print("Error: invalid input")
        return

    try:
        quantity = int(input("Enter quantity: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    if quantity <= 0:
        print("Error: quantity must be greater than zero")
        return

    if product_name not in product_prices:
        print("Error: product not found")
        return

    unit_price = product_prices[product_name]
    total_price = unit_price * quantity

    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", round(total_price, 2))


# ============================================================
# PROBLEM 4: STUDENT GRADES WITH DICTIONARY AND LIST
#
# Description:
# Store student grades in a dictionary of lists.
# Calculate a student's average and passing status.
#
# Inputs:
# - student_name: student name.
#
# Outputs:
# - Grades, average, and passed status.
#
# Validations:
# - Student name cannot be empty.
# - Student must exist in the dictionary.
# - Grade lists cannot be empty when calculating averages.
#
# Test cases:
# 1) Normal: Alice.
#    Expected: average 90.0 and Passed: true.
# 2) Border: Charlie.
#    Expected: average 70.0 and Passed: true.
# 3) Error: Unknown.
#    Expected: Error: student not found.
# ============================================================
def problem_4():
    print("\nProblem 4: Student grades")

    grades = {
        "Alice": [90.0, 85.0, 95.0],
        "Bob": [60.0, 65.0, 68.0],
        "Charlie": [70.0, 70.0, 70.0]
    }

    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Error: invalid input")
        return

    if student_name not in grades:
        print("Error: student not found")
        return

    student_grades = grades[student_name]

    if not student_grades:
        print("Error: no grades available")
        return

    average = sum(student_grades) / len(student_grades)
    is_passed = average >= 70.0

    print("Grades:", student_grades)
    print("Average:", round(average, 2))
    print("Passed:", str(is_passed).lower())


# ============================================================
# PROBLEM 5: WORD FREQUENCY COUNTER
#
# Description:
# Convert a sentence to lowercase and split it into words.
# Count each word and display the most common word.
#
# Inputs:
# - sentence: a non-empty sentence.
#
# Outputs:
# - Words list, frequency dictionary, and most common word.
#
# Validations:
# - Reject empty sentences.
# - Remove common punctuation from the beginning and end of words.
# - Verify that at least one word remains after cleaning.
#
# Test cases:
# 1) Normal: "Cat dog cat".
#    Expected: cat appears twice and is the most common word.
# 2) Border: "Hello!".
#    Expected: words list ['hello'].
# 3) Error: sentence contains only spaces.
#    Expected: Error: invalid input.
# ============================================================
def problem_5():
    print("\nProblem 5: Word frequency counter")

    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    cleaned_sentence = sentence.lower()

    words_list = [
        word.strip(string.punctuation)
        for word in cleaned_sentence.split()
    ]

    words_list = [word for word in words_list if word]

    if not words_list:
        print("Error: no words found")
        return

    freq_dict = {}

    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    most_common_word = max(freq_dict, key=freq_dict.get)

    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)


# ============================================================
# PROBLEM 6: SIMPLE CONTACT BOOK
#
# Description:
# Use a dictionary to add, search, or delete contacts.
# ADD creates or updates a contact; SEARCH and DELETE check
# whether a contact exists before performing the operation.
#
# Inputs:
# - action_text: ADD, SEARCH, or DELETE.
# - name: contact name.
# - phone: non-empty phone number for ADD.
#
# Outputs:
# - A success message or an appropriate error message.
#
# Validations:
# - Convert the action to uppercase.
# - Accept only ADD, SEARCH, or DELETE.
# - Reject empty contact names and phone numbers.
# - Check contact existence before searching or deleting.
#
# Test cases:
# 1) Normal: ADD, Dana, 5551234.
#    Expected: Contact saved: Dana 5551234.
# 2) Border: SEARCH, Alice.
#    Expected: Phone: 1234567890.
# 3) Error: DELETE, Missing.
#    Expected: Error: contact not found.
# ============================================================
contacts = {
    "Alice": "1234567890",
    "Bob": "5559876543",
    "Charlie": "5550001122"
}


def problem_6():
    print("\nProblem 6: Simple contact book")

    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")

    action_option = input("Choose an action (1-3): ").strip()

    actions = {
        "1": "ADD",
        "2": "SEARCH",
        "3": "DELETE"
    }

    action_text = actions.get(action_option)

    if action_text is None:
        print("Error: invalid option")
        return

    name = input("Enter contact name: ").strip()

    if not name:
        print("Error: invalid input")
        return

    if action_text == "ADD":
        phone = input("Enter phone number: ").strip()

        if not phone:
            print("Error: invalid input")
            return

        contacts[name] = phone
        print("Contact saved:", name, phone)

    elif action_text == "SEARCH":
        phone = contacts.get(name)

        if phone is None:
            print("Error: contact not found")
        else:
            print("Phone:", phone)

    elif action_text == "DELETE":
        if name not in contacts:
            print("Error: contact not found")
        else:
            contacts.pop(name)
            print("Contact deleted:", name)

# ============================================================
# MAIN MENU
# Allows the user to choose and run any of the six problems.
# The menu repeats until the user selects 0 to exit.
# ============================================================
def main():
    while True:
        print("\n=== LISTS, TUPLES AND DICTIONARIES MENU ===")
        print("1. Shopping list")
        print("2. Points and distances")
        print("3. Product catalog")
        print("4. Student grades")
        print("5. Word frequency counter")
        print("6. Contact book")
        print("0. Exit")

        choice = input("Choose a problem (0-6): ").strip()

        if choice == "1":
            problem_1()
        elif choice == "2":
            problem_2()
        elif choice == "3":
            problem_3()
        elif choice == "4":
            problem_4()
        elif choice == "5":
            problem_5()
        elif choice == "6":
            problem_6()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Error: invalid input")


if __name__ == "__main__":
    main()


# ============================================================
# CONCLUSIONS
# Lists are useful when collections need to grow or shrink.
# Their mutability allows items to be added, removed, or sorted.
# Tuples are appropriate for fixed data such as point coordinates.
# Their immutability helps keep grouped values unchanged.
# Dictionaries make information easy to find using descriptive keys.
# A dictionary of lists is useful for organizing student grades.
# Input validation helps prevent common errors during execution.
# Choosing the right collection makes a program easier to maintain.
# ============================================================

# ============================================================
# REFERENCES
# 1. Python Software Foundation. Built-in Types.
#    https://docs.python.org/3/library/stdtypes.html
#
# 2. Python Software Foundation. Data Structures.
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 3. Python Software Foundation. Built-in Functions.
#    https://docs.python.org/3/library/functions.html
#
# 4. Python Software Foundation. Errors and Exceptions.
#    https://docs.python.org/3/tutorial/errors.html
#
# 5. Python Software Foundation. More Control Flow Tools.
#    https://docs.python.org/3/tutorial/controlflow.html
# ============================================================