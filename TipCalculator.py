print("Welcome to tip calculator")
bill=float(input("what is the bill?"))
people=int(input("How many people are there?"))
tip=float(input("What percante you want to tip?"))
final_bill=bill+(bill*(tip/100))
Payamount=float(final_bill/people)
print(f"Total bill is {final_bill}")
print(f"Tip is {bill*(tip/100)}")
print(f"Each person will pay {Payamount}")

