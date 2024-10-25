'''
Write a Python program to ask how much money the user spent at the store.
If they spend less than $75, they will not receive the discount.
If they spend $75 or more, they get a $15 discount.
If users spend $100 or more, they will receive a $25 discount.
If users spend $150 or more, they will receive a $50 discount.
Then print out the total amount the user must pay.
'''
x = int(input("How much money the user spent at the store? "))
discount = 0
if x >= 150:
    discount = 50
elif x >= 100: # 100 <= x < 150
    discount = 25
elif x >= 75:
    discount = 15
# else:
#     discount = 0
print(f"discount = {discount}, pay = {x - discount}")