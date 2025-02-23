from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, QTimeEdit, QPushButton, QRadioButton, QLineEdit, QComboBox
from PyQt5.QtCore import Qt, QSize, QTime
from PyQt5.QtGui import QFont, QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("بیت‌فیت")
        self.setFixedSize(1400, 1000)

        # دیکشنری مختصات
        self.positions = {
            "label": (160, 5, 300, 100),
            "time_label": (40, 20, 420, 150),
            "time_edit": (250, 120, 200, 50),
            "push_button": (50, 900, 60, 60),
            "settings_button": (1350, 950, 30, 30),
            "back_button": (10, 10, 60, 60),
            "radio_day": (250, 670, 100, 50),
            "radio_night": (360, 670, 100, 50),
            "gender_combobox": (20, 200, 200, 50),  # موقعیت کمبو باکس جنسیت
        }

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.section1 = QFrame(self.main_widget)
        self.section1.setStyleSheet("background-color: rgba(183, 182, 182, 0.24); border-right: 1px solid #ccc; padding: 10px;")
        self.section1.setGeometry(0, 0, 1400 // 3, 1000)

        self.label = QLabel("ثبت فعالیت جدید", self.section1)
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setAlignment(Qt.AlignTop)
        self.label.setGeometry(*self.positions["label"])

        self.time_label = QLabel("مدت زمان انجام فعالیت ورزشی خود را وارد کنید", self.section1)
        self.time_label.setFont(QFont('Arial', 12))
        self.time_label.setStyleSheet("background-color: transparent; border-radius: 10px;")
        self.time_label.setGeometry(*self.positions["time_label"])

        self.time_edit = QTimeEdit(self.section1)
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setTime(QTime(0, 0))
        self.time_edit.setStyleSheet("border-radius: 10px;")
        self.time_edit.setGeometry(*self.positions["time_edit"])

        self.push_button = QPushButton(self.section1)
        self.push_button.setText("")
        icon_pixmap = QPixmap(r"C:\\Users\\as\\Desktop\\New folder\\add.png")
        self.push_button.setIcon(QIcon(icon_pixmap))
        self.push_button.setIconSize(QSize(40, 40))
        self.push_button.setFixedSize(60, 60)
        self.push_button.setStyleSheet("border-radius: 15px; background-color: rgba(76, 175, 80, 1);")
        self.push_button.setGeometry(*self.positions["push_button"])

        # ایجاد پنل تنظیمات
        self.section2 = QFrame(self.main_widget)
        self.section2.setStyleSheet("background-color: rgba(252, 252, 252, 0.95); border-left: 1px solid #ccc;")
        self.section2.setGeometry(1400 // 3, 0, (1400 // 3) * 2, 1000)

        self.button2 = QPushButton(self.main_widget)
        self.button2.setText("")
        icon_pixmap2 = QPixmap(r"C:\\Users\\as\\Desktop\\New folder\\setting.png")
        self.button2.setIcon(QIcon(icon_pixmap2))
        self.button2.setIconSize(QSize(30, 30))
        self.button2.setFixedSize(30, 30)
        self.button2.setStyleSheet("border-radius: 15px; background-color: rgba(156, 154, 154, 0.6);")
        self.button2.setGeometry(*self.positions["settings_button"])
        self.button2.clicked.connect(self.toggle_settings_panel)

        # ایجاد پنل تنظیمات (tab widget)
        self.overlay = QFrame(self.main_widget)
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.overlay.setGeometry(0, 0, 0, 0)  # شروع از حالت مخفی
        self.overlay.hide()

        # پنل تنظیمات (حالا به صورت مربع در وسط صفحه)
        self.settings_panel = QFrame(self.main_widget)
        self.settings_panel.setStyleSheet("background-color: white;")
        self.settings_panel.setGeometry(450, 250, 500, 500)
        self.settings_panel.hide()

        # اضافه کردن تایتل تنظیمات
        self.settings_title = QLabel("تنظیمات", self.settings_panel)
        self.settings_title.setFont(QFont('Arial', 10))
        self.settings_title.setStyleSheet("background-color: transparent; border: none; color: black;")  # تغییر رنگ و پس‌زمینه
        self.settings_title.setGeometry(10, 10, 70, 30)

        # تنظیمات تب‌ها
        self.tabs = QTabWidget(self.settings_panel)
        self.tabs.setGeometry(0, 40, 500, 460)
        self.tabs.setLayoutDirection(Qt.RightToLeft)

        # اضافه کردن تب‌ها
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tabs.addTab(self.tab1, "اصلی")

        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout(self.tab2)
        self.tabs.addTab(self.tab2, "ظاهری")

        # افزودن گزینه‌های انتخابی برای حالت روز و شب
        self.radio_day = QRadioButton("حالت روز", self.tab2)
        self.radio_night = QRadioButton("حالت شب", self.tab2)
      


        # چینش افقی
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.radio_day)
        radio_layout.addWidget(self.radio_night)

        self.tab2_layout.addLayout(radio_layout)

        # انتخاب پیش‌فرض حالت روز
        self.radio_day.setChecked(True)

        # تغییر حالت از طریق رادیو باتن
        self.radio_day.toggled.connect(self.update_theme)
        self.radio_night.toggled.connect(self.update_theme)

        # دکمه برگشت داخل پنل تنظیمات
        self.back_button = QPushButton(self.settings_panel)
        self.back_button.setGeometry(10, 430, 60, 60)
        back_icon = QIcon(r"C:\\Users\\as\\Desktop\\New folder\\arrow_back_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png")
        self.back_button.setIcon(back_icon)
        self.back_button.setIconSize(QSize(30, 30))
        self.back_button.setText(" ")
        self.back_button.setStyleSheet("border-radius: 15px; background-color: rgba(156, 154, 154, 0.6);")
        self.back_button.clicked.connect(self.toggle_settings_panel)

        # ایجاد ورودی نام در تب اصلی
        self.name_input = QLineEdit(self.tab1)
        self.name_input.setPlaceholderText("نام خود را وارد کنید")  # متن نمایشی به عنوان راهنما
        self.name_input.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 12px;")
        self.name_input.setGeometry(270, 50, 200, 50)  # موقعیت ورودی در گوشه بالا سمت راست

        # ایجاد ورودی وزن در تب اصلی (زیر ورودی نام)
        self.weight_input = QLineEdit(self.tab1)
        self.weight_input.setPlaceholderText("وزن خود را وارد کنید")  # متن نمایشی برای وزن
        self.weight_input.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 12px;")
        self.weight_input.setGeometry(20, 50, 200, 50)  # موقعیت ورودی وزن

        # ایجاد ورودی قد در تب اصلی (زیر ورودی وزن)
        self.height_input = QLineEdit(self.tab1)
        self.height_input.setPlaceholderText("قد خود را وارد کنید")  # متن نمایشی برای قد
        self.height_input.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 12px;")
        self.height_input.setGeometry(20, 110, 200, 50)  # موقعیت ورودی قد

        # ایجاد ورودی سن در تب اصلی (زیر ورودی قد)
        self.age_input = QLineEdit(self.tab1)
        self.age_input.setPlaceholderText("سن خود را وارد کنید")  # متن نمایشی برای سن
        self.age_input.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 12px;")
        self.age_input.setGeometry(270, 110, 200, 50)  # موقعیت ورودی سن

        # ایجاد کمبو باکس جنسیت
        self.gender_combobox = QComboBox(self.tab1)
        self.gender_combobox.addItem("مرد")
        self.gender_combobox.addItem("زن")
        self.gender_combobox.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 12px;")
        self.gender_combobox.setGeometry(*self.positions["gender_combobox"])
                # ایجاد کمبو باکس رشته ورزشی در تب اصلی
        self.sports_combobox = QComboBox(self.tab1)
        self.sports_combobox.addItem("هیچ ورزشی")
        self.sports_combobox.addItem("فوتبال")
        self.sports_combobox.addItem("والیبال")
        self.sports_combobox.addItem("بسکتبال")
        self.sports_combobox.addItem("ورزش کششی")
        self.sports_combobox.addItem("هوازی در خانه")
        self.sports_combobox.addItem("هوازی بیرون خانه")
        self.sports_combobox.addItem("کوه نوردی با شیب کم")
        self.sports_combobox.addItem("کوه نوردی با شیب زیاد")
        self.sports_combobox.addItem("پیاده روی")
        self.sports_combobox.addItem("دویدن")
        self.sports_combobox.addItem("اسکیت")
        self.sports_combobox.addItem("پینگ پنگ")
        self.sports_combobox.addItem("تنیس")
        self.sports_combobox.addItem("کاراته")
        self.sports_combobox.addItem("تکواندو")
        self.sports_combobox.addItem("کنگ فو")
        self.sports_combobox.addItem("بوکس")
        self.sports_combobox.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 12px;")
        self.sports_combobox.setGeometry(270, 200, 200, 50)  # موقعیت کومبو باکس رشته ورزشی
        # اضافه کردن لیبل جنسیت
        self.gender_label = QLabel("جنسیت خود را وارد کنید", self.tab1)
        self.gender_label.setFont(QFont('Arial', 9))
        self.gender_label.setStyleSheet("background-color: transparent; border: none; color: black;")
        self.gender_label.setGeometry(20, 170, 200, 30)
        # اضافه کردن لیبل رشته ورزشی
        self.sport_label = QLabel("رشته ورزشی خود را وارد کنید", self.tab1)
        self.sport_label.setFont(QFont('Arial', 9))
        self.sport_label.setStyleSheet("background-color: transparent; border: none; color: black;")
        self.sport_label.setGeometry(270, 170, 200, 30)
        # اضافه کردن دکمه با آیکون
        self.ok_button = QPushButton(self.tab1)
        self.ok_button.setIcon(QIcon(r"C:\Users\as\Desktop\New folder\select_check_box_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png"))
        self.ok_button.setStyleSheet("QPushButton { border-radius: 15px; background-color: rgba(76, 175, 80, 1); border: none; }")
        self.ok_button.setGeometry(200, 270, 60, 60)
        self.ok_button.setIconSize(QSize(30, 30))
        # تنظیمات اولیه: تشخیص حالت روز/شب از روی ساعت سیستم
        self.is_night = self.check_if_night()
        self.apply_theme(self.is_night)

        # به‌روز رسانی وضعیت گزینه‌های رادیویی در تب ظاهری
        self.update_radio_buttons()

    def toggle_settings_panel(self):
        if self.settings_panel.isVisible():
            self.settings_panel.hide()
            self.overlay.hide()
        else:
            self.settings_panel.show()
            self.overlay.setGeometry(0, 0, 1400, 1000)  # پوشش مات
            self.overlay.show()

    def update_theme(self):
        # بررسی اینکه کدام حالت انتخاب شده
        if self.radio_night.isChecked():
            self.apply_theme(True)
        else:
            self.apply_theme(False)

    def apply_theme(self, is_night):
        if is_night:
            # حالت شب
            self.setStyleSheet("background-color: black; color: white;")
            self.label.setStyleSheet("color: white; background-color: transparent;")
            self.settings_title.setStyleSheet("background-color: transparent; color: white;")  # تغییر رنگ تایتل به سفید
            self.time_label.setStyleSheet("background-color: transparent; border-radius: 10px; color: white;")
            self.time_edit.setStyleSheet("border-radius: 10px; color: white; background-color: #333;")
            self.push_button.setStyleSheet("border-radius: 15px; background-color: rgba(0, 128, 0, 1);")
            self.button2.setStyleSheet("border-radius: 15px; background-color: rgba(80, 80, 80, 0.6);")
            self.section1.setStyleSheet("background-color: rgba(50, 50, 50, 0.24); border-right: 1px solid #444;")
            self.section2.setStyleSheet("background-color: rgba(40, 40, 40, 0.95); border-left: 1px solid #444;")
            self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.7);")
            self.settings_panel.setStyleSheet("background-color: #2c2c2c; border: 1px solid #444;")
            self.tabs.setStyleSheet("background-color: #333; color: white;")
            self.tabs.tabBar().setStyleSheet(""" 
                QTabBar::tab {
                    background-color: #444;
                    color: white;
                    padding: 5px;
                    margin-right: 2px;
                    border-radius: 5px;
                    border: none;
                    outline: none;
                }
            """)
            self.tab1.setStyleSheet("background-color: #333; color: white;")
            self.time_edit.setStyleSheet("border-radius: 10px; color: white; background-color: #333;")
        
        else:
            # حالت روز
            self.setStyleSheet("background-color: white; color: black;")
            self.label.setStyleSheet("color: black; background-color: transparent;")
            self.settings_title.setStyleSheet("background-color: transparent; color: black;")  # تغییر رنگ تایتل به سیاه
            self.time_label.setStyleSheet("background-color: transparent; border-radius: 10px; color: black;")
            self.time_edit.setStyleSheet("border-radius: 10px; color: black; background-color: white;")
            self.push_button.setStyleSheet("border-radius: 15px; background-color: rgba(76, 175, 80, 1);")
            self.button2.setStyleSheet("border-radius: 15px; background-color: rgba(156, 154, 154, 0.6);")
            self.section1.setStyleSheet("background-color: rgba(183, 182, 182, 0.24); border-right: 1px solid #ccc;")
            self.section2.setStyleSheet("background-color: rgba(252, 252, 252, 0.95); border-left: 1px solid #ccc;")
            self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
            self.settings_panel.setStyleSheet("background-color: white; border: 1px solid #ccc;")
            self.tabs.setStyleSheet("background-color: white; color: black;")
            self.tabs.tabBar().setStyleSheet(""" 
                QTabBar::tab {
                    background-color: white;
                    color: black;
                    padding: 5px;
                    margin-right: 2px;
                    border-radius: 5px;
                    border: none;
                    outline: none;
                }
            """)
            self.tab1.setStyleSheet("background-color: white; color: black;")
            self.time_edit.setStyleSheet("border-radius: 10px; color: black; background-color: white;")
            
      
    def check_if_night(self):
        current_time = QTime.currentTime()
        if current_time.hour() >= 19 or current_time.hour() <= 6:
            return True
        return False

    def update_radio_buttons(self):
        if self.is_night:
            self.radio_night.setChecked(True)
        else:
            self.radio_day.setChecked(True)

# اجرای برنامه
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
