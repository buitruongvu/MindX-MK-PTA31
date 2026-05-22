import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi

class LoginApp(QMainWindow):
  def __init__(self):
    super(LoginApp, self).__init__()
    #Load file UI được tạo từ Qt Designer
    loadUi("lesson07.ui", self)
    # Kết nối sự kiện (events)
    # Nút chuyển dổi giữa hai màn hình
    self.btn_switch_register.clicked.connect(self.show_register_page)
    self.btn_switch_login.clicked.connect(self.show_login_page)
    #Nút hành động
    self.btn_login.clicked.connect(self.handle_login)
    self.btn_register.clicked.connect(self.handle_register)




  def show_register_page(self):
    # Chuyển sang đăng ký (index 1)
    self.stackedWidget.setCurrentIndex(1)
  def show_login_page(self):
    #chuyển về trang đăng nhập index 0
    self.stackedWidget.setCurrentIndex(0)
  def handle_login(self):
    username = self.txt_username_login.text()
    password = self.txt_password_login.text()

    #Logic Kiểm tra đăng nhập cơ bản
    if username == "admin" and password == "123456":
      QMessageBox.information(self, "Thanh cong", "Dang nhap thanh cong!")
      #Code mở cửa sổ làm việc chính ở đây
    else:
      QMessageBox.warning(self, "Loi", "Sai tai khoan hoac mat khau")
  def handle_register(self):
    username = self.txt_username_reg.text()
    password = self.txt_password_reg.text()
    confirm_password = self.txt_confirm_reg.text()
    if not username or not password:
      QMessageBox.warning(self, "Canh bao", "Vui long nhap day du thong tin")
      return
    if password != confirm_password:
      QMessageBox.warning(self, "loi", "Mat khau xac nhan khong khop!")
      return
    QMessageBox.information(self, "Thanh Cong", f"Tao tai khoan {username} thanh cong!")
      #Xoá form và quay lại trang đăng nhập
    self.txt_username_reg.clear()
    self.txt_password_reg.clear()
    self.txt_confirm_reg.clear()
    self.show_login_page()

if __name__ == "__main__":
  app = QApplication(sys.event_loop()) if QApplication.instance() else QApplication(sys.argv)
  window = LoginApp()
  window.setWindowTitle("Ung dung dang nhap")
  window.resize(400, 500) #Cài đặt kích thước mặc định
  window.show()
  sys.exit(app.exec())
  
  
