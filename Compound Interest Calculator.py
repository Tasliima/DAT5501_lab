import math

def InterestCal(Savings, AnnualInterestRate, Years):
    for i in range(0, Years): # range default 0 to number of years
        Amount = Savings * math.pow((1 + AnnualInterestRate/100), i)
        print("For Year", i+1," you will have a balance of £", round(Amount, 2)) # prints the balance for each year, to 2 decimal places
    return Amount

Savings = float(input("input your savings: £"))
AnnualInterestRate = float(input("input your interest rate:"))
Years = int(input("input your overall years:"))
print ("After", Years, "years, you will have: £", round(InterestCal(Savings, AnnualInterestRate, Years))) # prints the final balance to 2 decimal places
InterestCal(Savings, AnnualInterestRate, Years)