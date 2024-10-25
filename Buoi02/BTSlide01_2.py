'''
Write a program that reads two employees' hours and displays each employee's total and the overall total.
Cap each day at 8 hours.

Employee 1: How many days? 3
Hours? 6
Hours? 12
Hours? 5
Employee 1's total hours = 19 (6.33 / day)

Employee 2: How many days? 2
Hours? 11
Hours? 6
Employee 2's total hours = 14 (7.00 / day)

Total hours for both = 33

'''
def nhap_thong_tin(idx):
    emp1_day = int(input(f"Employee {idx}: How many days? "))
    emp1_total = 0
    for day in range(1, emp1_day  + 1):
        tmp = int(input("Hours? "))
        emp1_total += 8 if tmp > 8 else tmp

    print(f"Employee {idx}'s total hours = {emp1_total} ({round(emp1_total/emp1_day, 2)} / day)\n")
    
    return emp1_total

n = int(input("How many employees? "))
sum = 0
for idx in range(1, n + 1):
    sum += nhap_thong_tin(idx)

print(f"Total hours for all = {sum} hrs.")