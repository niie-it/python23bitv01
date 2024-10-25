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
emp1_day = int(input("Employee 1: How many days? "))
emp1_total = 0
for day in range(1, emp1_day  + 1):
    tmp = int(input("Hours? "))
    # emp1_total += 8 if tmp > 8 else tmp
    if tmp > 8:
        emp1_total += 8
    else:
        emp1_total += tmp

print(f"Employee 1's total hours = {emp1_total} ({round(emp1_total/emp1_day, 2)} / day)")


emp2_day = int(input("Employee 2: How many days? "))
emp2_total = 0
for day in range(1, emp2_day  + 1):
    tmp = int(input("Hours? "))
    emp1_total += 8 if tmp > 8 else tmp

print(f"Employee 2's total hours = {emp2_total} ({round(emp2_total/emp2_day, 2)} / day)")


print(f"Total hours for both = {emp1_total + emp2_total}")