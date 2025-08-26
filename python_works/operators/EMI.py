#  EMI = P x R x (1+R)^n /(1+R)^n-1
#  P = loan amount
#  R = interest rate per month(annual_rate/(12*100))
#  n = loan tenure in months(6*12)

loan_amount = int(input("enter loan amount "))

interest_rate = int(input("enter interest rate "))

loan_tenure = int(input("enter loan tenure in years "))

p = loan_amount

r = interest_rate/(12*100)

n = loan_tenure*12

emi = p * r * (1 + r)**n / ((1 + r)**n - 1)

print("monthly emi:",round(emi,2))

total_payable_amout = emi * n

print("total payable amout:",round(total_payable_amout,2))

total_intrest = total_payable_amout -loan_amount

print("total intrest :" ,round(total_intrest,2))