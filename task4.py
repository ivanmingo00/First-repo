age = int(input("Enter your age: "))

is_student = input("Are you a student? (True/False): ").lower() == "true"

base_price = 12

discount = 0

if age <= 12:

    discount = 3

elif age >= 65:

    discount = 4

elif is_student:

    discount = 2

final_price = base_price - discount

print("Your ticket price is (" + str(final_price) + ".")