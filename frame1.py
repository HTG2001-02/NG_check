import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check NG")
        self.setFixedSize(750,560)

        self.MainUI()

    def MainUI(self):
        main_layout = QVBoxLayout()
        # frame for the main content
        frame_show = QFrame()
        frame_show.setStyleSheet("background-color: #f9f9f9; border: 1px solid #ccc;")
        frame_show.setFrameShape(QFrame.StyledPanel)
        frame_show.setFrameShadow(QFrame.Raised)

        # tạo các layout, widget cho các frame để hiển thị nội dung trong frame_show
        # với tab Check NG khi nhấn btn Check_NG thì hiển thị chức năng như Frame1.py
        # tạo hàm để hiển thị nội dung trong frame_show
        self.tab_view = QWidget()
        self.tab_view.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")       
        self.table_view = QWidget()
        self.table_view.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;") 




        main_layout.addWidget(frame_show)

        # Group button layout
        group_btn = QHBoxLayout()
        btn_check = QPushButton("Check_NG")
        btn_check.setFixedWidth(150)

        btn_check.setStyleSheet("background-color: #4CAF50; color: #353D38; font-weight: bold; font-size: 12px;")
        
        btn_settings = QPushButton("Settings")
        btn_settings.setFixedWidth(150)

        btn_settings.setStyleSheet("background-color: #E6D230; color: #353D38; font-weight: bold; font-size: 12px;")
        
        btn_config = QPushButton("Config")
        btn_config.setFixedWidth(150)
        btn_config.setStyleSheet("background-color: #2353D9; color: #353D38; font-weight: bold; font-size: 12px;")
        
        group_btn.addWidget(btn_check)
        group_btn.addWidget(btn_settings)   
        group_btn.addWidget(btn_config)
        
        main_layout.addLayout(group_btn)
        
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTabWidget,
                             QLabel, QTabBar, QFrame, QPushButton,
                             QHBoxLayout, QTableWidget, QTableWidgetItem,
                             QInputDialog)

class CustomTabBar(QTabBar):
    def mouseReleaseEvent(self, event):
        index = self.tabAt(event.pos())
        if index == self.count() - 1:
            # Nếu click vào tab cuối (tab '+')
            self.parent().handle_plus_tab()
        else:
            super().mouseReleaseEvent(event)

class CustomTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabBar(CustomTabBar(self))  # Gắn tab bar tùy chỉnh
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.add_plus_tab()

    def add_plus_tab(self):
        plus_tab = QWidget()
        self.addTab(plus_tab, "+")
        self.tabBar().setTabButton(self.count() - 1, QTabBar.RightSide, None)  # Ẩn nút x

    def add_named_tab(self, title):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Nội dung của tab: {title}"))
        tab.setLayout(layout)

        # Thêm tab mới trước tab '+'
        index = self.insertTab(self.count() - 1, tab, title)
        self.setCurrentIndex(index)

    def handle_plus_tab(self):
        title, ok = QInputDialog.getText(self, "Thêm tab", "Nhập tên tab:")
        if ok and title.strip():
            self.add_named_tab(title.strip())

    def close_tab(self, index):
        # Không cho đóng tab '+'
        if index == self.count() - 1:
            return
        self.removeTab(index)

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,460)
        self.setWindowTitle("Check NG")

        # Tạo layout chính
        main_layout = QVBoxLayout()
        
        # Tạo frame chứa các tab tùy chỉnh
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFixedHeight(400)
        
        # Tạo layout cho frame và thêm CustomTabWidget vào
        frame_layout = QVBoxLayout()
        self.tab_widget = CustomTabWidget()
        frame_layout.addWidget(self.tab_widget)
        frame.setLayout(frame_layout)
        
        main_layout.addWidget(frame)

        button_layout = QHBoxLayout()
        button1 = QPushButton("Check NG")
        button2 = QPushButton("Config VNC")
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())


