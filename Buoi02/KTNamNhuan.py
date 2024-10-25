'''
Năm nhuận là năm chia hết cho 4.
Nhưng nếu chia hết cho 100 thì phải chia hết cho 400.
==>
- Năm chia cho 400 ==> năm nhuận
- Ngược lại (ko chia hết cho 400) thì năm chia hết cho 4 mà ko chia hết cho 100
'''
year = int(input("Nhập năm cần kiểm tra: "))
is_leap_year = False
# if year % 400 == 0:
#     is_leap_year = True
# elif year % 4 == 0 and year % 100 != 0:
#     is_leap_year = True
    
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    is_leap_year = True

month = int(input("Nhập tháng cần kiểm tra: "))
num_of_days = 0
if month in [1,3,5,7,8,10,12]:
    num_of_days = 31
elif month in [4,6,9,11]:
    num_of_days = 30
elif month == 2:
    num_of_days = 29 if is_leap_year else 28