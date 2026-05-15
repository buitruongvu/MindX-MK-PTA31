#import thư viện 
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

#Tạo app
app = QApplication(sys.argv)

#Mỗi trang giao diện là một class riêng biệt
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    #Lấy file giao diện tạo cùng folder
    uic.loadUi('lesson06.ui', self)

#Hàm hiển thị thông báo
def msg_box(title, content):
  msg = QtWidgets.QMessageBox()
  # msg.setStyleSheet("QLabel{min_width: 200px;}"
  #                   "Q")
  msg.setWindowTitle(title)
  msg.setInformativeText(content)
  msg.exec

# Chuyển cửa sổ giao diện 
def switch_window(classw):
  global window 
  window = classw
  window.show()
#chạy app
# run app
window = MainWindow()
window.show()
sys.exit(app.exec())
# Cách chạy file
# Step 1: Chuột phải vào folder muốn chạy
# Step 2: Chọn "Open in integrated Terminal"
# Step 3: Nhập lệnh "python main.py"