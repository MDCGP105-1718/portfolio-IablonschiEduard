total_cost = float(input("The cost of your dream home: "))
portion_deposit = 0.20
current_savings = 0.0
r = 0.04
annual_salary = float(input("The starting annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
monthly_salary = annual_salary / 12
months = 0

while current_savings < total_cost * portion_deposit:
    current_savings = current_savings + monthly_salary * portion_saved
    current_savings = current_savings + current_savings * r / 12
    months = months + 1
print(f"Number of months: {months}")
