workers_name = input("Employee name:")
activity_done = input("Role:")
hours_worked = input("hours worked:")
rate=30000


wage = (int(hours_worked)*rate)
allowance =(0.05*wage)
gross_wage =(allowance+wage)
tax = (0.05*gross_wage) 
net_wage =(gross_wage-tax)

print(f"wage: {wage}\nallowance:{allowance}\ngross wage:{gross_wage}\ntax{tax}\n{net_wage}")

