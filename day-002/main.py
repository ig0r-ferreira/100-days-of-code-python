print("Welcome to the tip calculator!")
bill_value = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_peoples = int(input("How many people to split the bill? "))

value_per_person = (bill_value * (1 + tip / 100)) / num_peoples
print(f"Each person should pay: ${value_per_person:.2f}")
