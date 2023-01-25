#Tip calculator
print("Welcome to the tip calculator")
bill = input("What was the total bill? $ ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
tipp = 1 + int(tip)/100
pay = int(bill) * tipp / int(people)
payf = "{:.2f}".format(pay) 

print(f"Each person should pay ${payf}")