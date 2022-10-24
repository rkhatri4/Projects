principal = int(input("Enter the principal amount: "))
APR = int(input("Enter the annual percent interest rate: "))
n = int(input("Enter the number of years: "))
amount = principal * (1 + APR/100)**n
print("The amount is", amount)
