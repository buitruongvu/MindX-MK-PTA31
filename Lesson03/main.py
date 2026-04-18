import oop
human1 = oop.Human("Minh Nguyên", 11, "male")
human1.introduce()

student1 = oop.Student("Gia Bao", 11, "male", "TH Thanh Tri")
student1.introduce()
student1.show_info()
student1.edit_age()
print(student1.age)
student1.edit_school("Vinschool")
print(student1.school)