print("Welcome to the tip Calculator!")
Total_bill = float(input("What was the total bill: "))
Tip = int(input("how uch tip would you like to give ?, 10, 12 or 15: "))
Tip = (Tip / 100)
Total_bill += (Tip * Total_bill)
split_between = int(input("Between how many people you want to split the ammount: "))
final_bill = round(Total_bill / split_between,2)

print("Each person should pay: $",final_bill)