print("Welcome to top calculator")
total_bill = float(input("What is the total bill?: "))
amount_of_people = float(input("How many people to split the bill?: "))
tip_percentage = float(input("How percentage tip do you want to give?: "))
final_bill = (tip_percentage / 100 + 1) * total_bill
per_person = round(final_bill / amount_of_people, 2)
print(f"Each person should pay {per_person}$")
