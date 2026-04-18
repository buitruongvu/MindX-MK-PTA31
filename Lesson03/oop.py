# Tính chất kế thừa
class Human:
  #hàm khởi tạo giá trị
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  # Giới thiệu bản thân
  def introduce(self):
    print(f'Xin chào, tôi tên là {self.name}, {self.age} tuổi')
# Lớp Student kế thừa từ lớp Human
class Student(Human):
  #hàm khởi tạo giá trị
  def __init__(self, name, age, gender, school):
    # Gọi hàm khởi tạo giá trị từ lớp cha
    super().__init__(name, age, gender)
    # Thêm thuộc tính riêng của lớp Student
    self.school = school
  # Ghi đè (override) phương thức từ lớp cha
  def introduce(self):
    print(f"Tôi tên là {self.name}, học tại {self.school}")
  #Phương thức hiển thị thông tin
  def show_info(self):
    print(f'''
======= Thông tin =======          
Họ tên: {self.name}
Tuổi: {self.age}
Giới tính: {self.gender}
Trường học: {self.school}
=========================
''')
  #phương thức chỉnh sửa thông tin
  #Chỉnh sửa tuổi (Tự nhập)
  def edit_age(self):
    new_age = int(input("Nhập tuổi mới: "))
    if new_age <=0:
      print("Tuổi không hợp lệ")
    else:
      self.age = new_age
      print(f"Tuổi của {self.name} đã được cập nhật")
  #Chỉnh sửa trường học (Truyền tham số)
  def edit_school(self, new_school):
    if new_school.strip() == "":
      print("Tên trường không hợp lệ")
    else: 
      self.school = new_school.strip()
      print(f"Trường của {self.name} đã được cập nhật")