print("welcome to tip calculator\n")
bill_amount=float(input("enter total bill\n"))
tip_amount_percent=int(input("enter tip amount percent 10,12,15\n"))
tip=((bill_amount*tip_amount_percent)/100)
print(type(tip))
print("\n")
print(f"you paid tip is {tip}")
no_people=int(input("enter no people to split bill\n"))
balance=bill_amount-tip
paid_bill=balance/no_people
print(f"each person paid amount of {paid_bill}")

