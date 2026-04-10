# Bước 1: Nhập thời gian từ bàn phím (định dạng hh:mm:ss)
time_input = input("Nhập thời gian (hh:mm:ss): ")
try:
    # Bước 2: Tách chuỗi dựa trên dấu hai chấm
    print(time_input.split(":"))
    h, m, s = map(int, time_input.split(':'))
    print(h)
    # Bước 3: Kiểm tra điều kiện hợp lệ
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        print("Hợp lệ!")
    else:
        print("Không hợp lệ!")      
except:
    # Trường hợp người dùng nhập sai định dạng hoặc không phải số
    print("Không hợp lệ! (Vui lòng nhập đúng định dạng hh:mm:ss)")

# testcase 1
# testcase 2