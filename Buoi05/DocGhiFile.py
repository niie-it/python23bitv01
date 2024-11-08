your_name = input("What is your name?\n")
year_old = input("How old are you?\n")
major = input("What is your major?\n")

with open("student.txt", "w") as myfile:
    myfile.write(f"{your_name}\n")
    myfile.write(f"{year_old} year old(s)\n")
    myfile.write(f"{major}\n")
