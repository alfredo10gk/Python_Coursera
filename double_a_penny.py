amount = float(input("Enter the initial amount: "))  # Start with any value
total_amount = 0  # Initialize total amount

for day in range(1, 15):
    total_amount += amount
    amount *= 2  # Double the amount each day

print(f"Total amount after 14 days: ${total_amount:.2f}")
