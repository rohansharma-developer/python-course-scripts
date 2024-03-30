print("Welcome to the tip calculator!")
bill = float(input("What is your total bill? $"))
p = int(input("What percentage would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
f_bill = float((((p*bill)/100) + bill) /split)
r_bill = round(f_bill, 2)
print(f"Each person should pay ${r_bill}")


