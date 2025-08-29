name = str(input())
salary = float(input())
sales = float(input())

commission = sales * (15/100)
result = commission + salary
print(f"TOTAL = R$ {result:.2f}")