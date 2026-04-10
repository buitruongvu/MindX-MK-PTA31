# Kiểu dữ liệu (Data Types)
# Số nguyên (int), Số thực (float), Chuỗi (string), Boolean(True/False)
number = 7 #int
print(type(number)) # Kiểm tra kiểu dữ liệu
number_float = 3.14 # float
print(type(number_float))
my_name = 'Gia Bao' # string
print(type(my_name))
isStudent = True # Boolean
sum = number_float + number #Toán tử cộng
print("Tong:", sum)
print(2 ** 3) # Mũ
print(5 // 2) # Chia lấy phần nguyên
print(5 % 2) # Chia lấy phần dư
print(12 - 7) # phép trừ
print(10 * 3) # Phép nhân
# a = int(input("Nhap vao so nguyen: ")) 
# print(a + 12)
# Thực hành: Nhập vào 3 số nguyên a, b, c in ra tích của ba số nguyên đó 
# a, b, c = map(int, input("Nhập 3 so nguyên: ").split())
# mutiple =  a * b * c
# print(mutiple)

# Câu điều kiện
#Thực hành in ra bạn có chiều cao lớn nhất trong 3 bạn
# a, b, c = map(int, input("Nhap chieu cao cua 3 ban: ").split())
# if a > b and a > c:
#   print(f"Bạn a cao nhất với chiều cao là {a}") # template String
# elif b > a and b > c:
#   print(f"Bạn b cao nhất với chiều cao là {b}") # template String
# else: 
#   print(f"Bạn c cao nhất với chiều cao là {a}") # template String

total = 0
for number in range(1, 6):
    print("num", number)
    total = total + number
    print("total", total)
if total > 10:
    print("Tổng lớn hơn 10")
else:
    print("Tổng nhỏ hơn hoặc bằng 10")

# Function (Hàm)
# Hàm có giá trị trả về và hàm không có giá trị trả về
# type 1: Hàm không có giá trị trả về
def sayHello ():
    print("hi Gia Bao")

sayHello()
# type 2: Hàm có giá trị trả về
def calculateSum (a, b):
    return a + b
print("line 54:", calculateSum(10, 5))
    
