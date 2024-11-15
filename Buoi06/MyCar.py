class Car:
    # khai báo thuộc tính (đặc điểm đặc trưng cho đối tượng phù hợp bài toán quản lý)
    name = ""
    model = ""
    color = ""
    year = 0

    # Hàm tạo (mục đích: khai báo và khởi tạo đối tượng)
    def __init__(self, hang, ten, mau, nam_sx):
        self.name =  hang
        self.model = ten
        self.color = mau
        self.year = nam_sx
       
    def xuat_thong_tin(self):
        print(f"{self.name} {self.model} {self.color} {self.year}")

    def start(self):
        print("Xe bắt đầu chạy")

    def __str__(self):
        return f"{self.name} {self.model} {self.color} {self.year}"
       
# Demo
if __name__ == "__main__":
    mycar = Car('Mazda', 'CX5', 'Red', 2020)
    print(mycar) # mycar.__str__()
    mycar.xuat_thong_tin()
    mycar.start()
    his_car = Car('Honda', 'HRV L', 'Gray', 2024)
    print(his_car.model)

    cars = []
    cars.append(mycar)
    cars.append(his_car)
    for car in cars:
        print(car)
