# Set variables

bill=float(input("Enter your bill: "))
tax=float(input("Enter your Tax(percentage)?  "))
tip=float(input("Enter your tip(percentage): "))

# Calculate and add tax
tax_amount = (bill*tax)/100
total = bill+tax_amount

# Calculate and add tip
tip_amount = (total*tip)/100
total = total+tip_amount

# Round
total = round(total,2)


# Print
print(total)
