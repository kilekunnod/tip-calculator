# exchange your pleasantries, be nice :)
print("Hello there. Welcome to the tip calculator! Hope you had an amazing meal.")
# variable to store the bill
bill = float(input("What was the total bill? $"))
# another variable to store the tip given
tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15%?"))
# another variable to store the number of people splitting the bill
people = int(input("How many will be splitting the bill today?"))
# convert the tip to a percentage
tip_as_percent = tip / 100
# multiply the bill by the tip - it's a percentage value
bill_with_tip = bill * tip_as_percent
# adding the tip to the total bill
total_bill = bill_with_tip + bill
# calculation for the individual bills
bill_per_person = total_bill / people
# rounding it to 2 decimal places
final_bill = round(bill_per_person, 2)
print(f"Each person should pay ${final_bill}")