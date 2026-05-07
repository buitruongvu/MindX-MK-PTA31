#practice 1
class DongVat:
  #1. Khởi tạo
  def __init__(self, ten_loai, tuoi, loai, moi_truong_song): # tên biến: Snake case 
    self.ten_loai = ten_loai
    self.tuoi = tuoi
    self.loai = loai
    self.moi_truong_song = moi_truong_song
  #2. Cập nhật môi trường sống
  def cap_nhat_moi_truong_song(self, moi_truong_moi):
    self.moi_truong_song = moi_truong_moi
    print(f"Cập nhật {self.ten_loai} đã được chuyển đến: {self.moi_truong_song}")
  #3. Xuất ra thông tin
  def xuat_thong_tin(self):
    print(f'''
=====THÔNG TIN ĐỘNG VẬT=========
Tên loài: {self.ten_loai}
Tuổi: {self.tuoi}
Loài: {self.loai}
Môi trường sống: {self.moi_truong_song}
================================
''')
#Ví dụ
ho_bengal = DongVat("Hổ Bengal", 8, "Động vật có vú", "Rừng nhiệt đới")
ho_bengal.xuat_thong_tin()
ho_bengal.cap_nhat_moi_truong_song("Khu bảo tồn hoang giã")
ho_bengal.xuat_thong_tin()
#Practice2
#lớp cơ sở (Base class)
class PhuongTien:
  #1 Khởi tạo
  def __init__(self, bien_so, hang_xe, mau_sac):
    self.bien_so = bien_so
    self.hang_xe = hang_xe
    self.mau_sac = mau_sac
  #2 Cập nhật màu sắc
  def cap_nhat_mau_sac(self, mau_moi):
    self.mau_sac = mau_moi
    print(f"Cập nhật xe {self.bien_so} Đã được sơn thành màu {self.mau_sac}")
  # 3 xuất thông tin
  def display_info(self):
    print(f'''
========Thông tin=======
Biển số: {self.bien_so}
Hãng xe: {self.hang_xe}
Màu sắc: {self.mau_sac}
========================''')
#Lớp kế thừa: Ô tô
class Oto(PhuongTien):
  def __init__(self, bien_so, hang_xe, mau_sac, so_cho_ngoi):
    super().__init__(bien_so, hang_xe, mau_sac)
    self.so_cho_ngoi = so_cho_ngoi
  #Ghi đè phương thức display_info
  def display_info(self):
    super().display_info()
    print(f"Số chỗ ngồi: {self.so_cho_ngoi}")
class XeMay(PhuongTien):
  def __init__(self, bien_so, hang_xe, mau_sac, loai_xe):
    super().__init__(bien_so, hang_xe, mau_sac)
    self.loai_xe = loai_xe
  def display_info(self):
    super().display_info()
    print(f"Loại xe: {self.loai_xe}")
#Thực thi yêu cầu: Tạo đối tượng và gọi phương thức
xe_may_1 = XeMay("73A243", "BMW", "Gray", "tay ga")
oto_1 = Oto("65A243", "BMW", "Gray", 8)
xe_may_1.display_info()
oto_1.display_info()  
# Cập nhật màu sắc
oto_1.cap_nhat_mau_sac("red")
oto_1.display_info()