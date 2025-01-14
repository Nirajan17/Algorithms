# monthly bill

monthly_bill = {
    "jan" : 2200,
    "feb" : 2530,
    "march" : 2390,
    "april" : 3498,
    "may" : 2000,
    "june" : 3400,
    "july" : 2000,
 }

# how much extra expense in feb compared to jan?

print(f"Expenses for Feb is more by {monthly_bill['feb'] - monthly_bill['jan']} amount")

# Expenses for first quarter of year

print(f"Total Expenses for first quarter is {monthly_bill['jan']+monthly_bill['feb']+monthly_bill['march']+monthly_bill['april']}")

# find out if you spent exactly 2000 dollars in any month

flag = False
for key, value in monthly_bill.items():
    if value == 2000:
        print(f"You spent 2000 dollars in {key} month")
        flag = True

if flag == False:
    print("You have not spent exactly 2000 dollars yet.")