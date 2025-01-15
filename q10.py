# Prompt the user for the principal amount, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate the compound interest
# amount = principal * (1 + rate / 100) ** time
amount = principal * pow((1 + rate /100),time) 
compound_interest = amount - principal

print(f"The compound interest is {compound_interest}.")
