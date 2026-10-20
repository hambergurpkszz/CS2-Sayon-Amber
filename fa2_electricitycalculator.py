# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")
previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules

# 1. Customer name -- Must not be empty
name = input("Emter customer name: ")

if name.strip() == "":
    print("Invalid name, please try again.")
    name = input("Enter customer name: ")

# 2. Previous reading -- Number at least 0
previous = float(input("Enter previous meter reading: "))

if previous < 0:
    print("Invalid meter reading, must be at least 0.")
    previous = float(input("Enter previous meter reading: "))
    
# 3. Current reading -- Number at least the previous reading
current = float(input("Enter current meter reading: "))

if current < previous:
    print("Invalid meter reading, must be at least the previous reading.")
    current = float(input("Enter current meter reading: "))
