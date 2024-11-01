'''
Compute each worker's total hours and hours/day.
Should work no matter how many days a person works.
Suzy ID 123 worked 31.4 hours: 6.3 / day
'''
lines = open("hours.txt")
for line in lines:
    chuoi = line.replace("\n", "")
    mang = chuoi.split()
    # print(mang)
    arr_hours = mang[2:]
    sum = 0
    for item in arr_hours:
        sum += float(item)
    print(f"{mang[1]} ID {mang[0]} worked {sum} hours: {round(sum / len(arr_hours), 2)} / day")

lines.close()