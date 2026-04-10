# Lập trình hướng đối tượng (OOP) - Object Oriented Programming

# Class (Lớp) 
    #Thuộc tính (Attribute): Là những thông tin, đặc điểm của đối tượng.
      #ví dụ: Con mèo (mắt, mũi, tai, chân, đuôi)
    #Phương thức (Method): là những thao tác, hành động mà đối tượng đó có thể thực hiện.
      #Ví dụ: Một con mèo có thể kêu meo meo, chạy, nhảy, ăn và uống

class Car:
  def __init__(self, brand, color):
    self.brand = brand #thuộc tính
    self.color = color #thuộc tính
  def start(self):  #phương thức start
    print(self.color, self.brand, "is starting")

# Object (Đối tượng) 
                      # class: Car 
                      # objects: brand: Audi, Nissan, vinfast 
                                 #color: white, red, blue
car1 = Car("Toyota", "red")
car1.start()
car2 = Car("Vinfast", "blue")
car2.start()

#Practices
# Bài 1: Tạo lớp Sinh viên
# Tạo class Student với:
# thuộc tính: name, age, score
# Viết hàm display() để in thông tin
# 👉 Ví dụ:
# Name: An, Age: 20, Score: 8.5

class Student:
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score
  def display(self):
    print(f"Name: {self.name}, Age: {self.age}, Score: {self.score}")

  #Bài 2
  def get_grade(self):
    if self.score >=8:
      return "Gioi"
    elif self.score >= 6.5:
      return "Kha"
    else:
      return "Trung binh"
student1 = Student("Minh Duc", 12, 6)
student1.display() 
print(student1.get_grade())
student2 = Student("Gia Bao", 11, 8.5)
student2.display()
student3 = Student("Nguyen", 13, 9)
student3.display()
student4 = Student("Gia Khanh", 12, 7)
student4.display()
print(student4.get_grade())

# 🟢 Bài 2: Tính điểm trung bình
# Thêm phương thức get_grade():
# >= 8 → Giỏi
# >= 6.5 → Khá
# < 6.5 → Trung bình


# 🟢 Bài 3: Lớp Hình chữ nhật
# Tạo class Rectangle:
# thuộc tính: width, height
# Viết:
# area() → diện tích
# perimeter() → chu vi


                           
