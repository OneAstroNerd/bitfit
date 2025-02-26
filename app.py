import sys  
#from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QLineEdit, QComboBox, QSpacerItem, QSizePolicy)  
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, QTimeEdit, QPushButton, QRadioButton, QLineEdit, QComboBox,QSpacerItem,QSizePolicy,QMessageBox

from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, QTime
from PyQt5 import QtCore  
import json
import os
from persiantools.jdatetime import JalaliDate as jdate


# Calculations

def calc(weight, hight, gender, age, exercise, sport):

    result = {}

    y = hight**2
    x=float(weight/y)
    bmim=(1.20*x)+(0.23*age)-16.02 
    bmiw=((1.20*x)+(0.23*age)-16.02)-5.4



    if gender == 'male':
        result["fat percentage"] = bmim
    if gender == 'female':  
        result["fat percentage"] = bmiw
    #variable1   

    bmr_men=( 655.1+(9.6 * weight)+(1.8*hight)-(4.7*age))
    bmr_women=(66.5+(13.75*weight)+(5*hight)-(6.755*age))
    
    gymnastics=4.5
    aerobics=11
    aerobic_outdoors=11
    hiking=10.5
    rockclimbing=19.3
    walking=7
    running=15.8
    skating=12.3
    soccer=15
    volleyball=5.2
    basketball=14
    pingpong=4.3
    tennis=12.3
    karate=14
    tekwando=15.6
    kungfo=14.1
    boxing=15.8


    if sport != "none":   
        t=input( 'enter your exercise time')
        if sport=="gymnastics":
            if gender=="male":
                kcal=(gymnastics*t)+(bmr_men)
            if gender=="female":
                kcal= (gymnastics*t)+(bmr_women)   
        if sport=="aerobics":
            if gender=="male":
                kcal=(aerobics*t)+(bmr_men)
            if gender=="female":
                kcal= (aerobics*t)+(bmr_women)  
        if sport=="aerobic_oudoors":
            if gender=="male":
                kcal=(aerobic_outdoors*t)+(bmr_men)
            if gender=="female":
                kcal= (aerobic_outdoors*t)+(bmr_women) 
        if sport=="hiking":
            if gender=="male":
                kcal=(hiking*t)+(bmr_men)
            if gender=="female":
                kcal= (hiking*t)+(bmr_women) 
        if sport=="rockclimbing":
            if gender=="male":
                kcal=(rockclimbing*t)+(bmr_men)
            if gender=="female":
                kcal= (rockclimbing*t)+(bmr_women) 
        if sport=="walking":
            if gender=="male":
                kcal=(walking*t)+(bmr_men)
            if gender=="female":
                kcal= (walking*t)+(bmr_women) 
        if sport=="running":
            if gender=="male":
                kcal=(running*t)+(bmr_men)
            if gender=="female":
                kcal= (running*t)+(bmr_women) 
        if sport=="skating":
            if gender=="male":
                kcal=(skating*t)+(bmr_men)
            if gender=="female":
                kcal= (skating*t)+(bmr_women) 
        if sport=="soccer":
            if gender=="male":
                kcal=(soccer*t)+(bmr_men)
            if gender=="female":
                kcal= (soccer*t)+(bmr_women) 
        if sport=="volleyball":
            if gender=="male":
                kcal=(volleyball*t)+(bmr_men)
            if gender=="female":
                kcal= (volleyball*t)+(bmr_women) 
        if sport=="basketball":
            if gender=="male":
                kcal=(basketball*t)+(bmr_men)
            if gender=="female":
                kcal= (basketball*t)+(bmr_women) 
        if sport=="pingpong":
            if gender=="male":
                kcal=(pingpong*t)+(bmr_men)
            if gender=="female":
                kcal= (pingpong*t)+(bmr_women) 
        if sport=="tennis":
            if gender=="male":
                kcal=(tennis*t)+(bmr_men)
            if gender=="female":
                kcal= (tennis*t)+(bmr_women) 
        if sport=="karate":
            if gender=="male":
                kcal=(karate*t)+(bmr_men)
            if gender=="female":
                kcal= (karate*t)+(bmr_women) 
        if sport=="tekwando":
            if gender=="male":
                kcal=(tekwando*t)+(bmr_men)
            if gender=="female":
                kcal= (tekwando*t)+(bmr_women) 
        if sport=="kungfo":
            if gender=="male":
                kcal=(kungfo*t)+(bmr_men)
            if gender=="female":
                kcal= (kungfo*t)+(bmr_women) 
        if sport=="boxing":
            if gender=="male":
                kcal=(boxing*t)+(bmr_men)
            if gender=="female":
                kcal= (boxing*t)+(bmr_women)
        result["calories"] = kcal
        if t>=20 and t<=30 :
            result["carbohydrates"] =weight*4

        if t>=31 and t<=60 :
            result["carbohydrates"] =weight*6
        if t>=61 and t<=180 :
            result["carbohydrates"] =weight*8
        if t>180 :
            result["carbohydrates"] =weight*10
        if t >=44 and t<=20 :
            result["protein"] =weight*0.7
        if t >= 45 and t <= 60: 
            result["protein"] =weight*1.1
        if t >= 61  :
            result["protein"] =weight*1.7



        
    if exercise == "none":
        if gender=='male':
            result["calories"]=bmim
        if gender=="female":
            result["calories"]=bmiw

        result["protein"] =weight*0.8

    return result








#  Setup system
class Setup(QWidget):
    def __init__(self):  
        super().__init__()  
        self.initUI()  

    def initUI(self):  
        self.setWindowTitle('راه اندازی')  
        self.setFixedSize(600, 500)  

        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)  

        layout = QVBoxLayout()  

        self.name_input = QLineEdit(self)  
        self.name_input.setPlaceholderText("نام")  
        self.name_input.setStyleSheet("border-radius: 5px; padding: 5px;")  
        layout.addWidget(self.name_input)  

        self.weight_input = QLineEdit(self)  
        self.height_input = QLineEdit(self)  
        self.age_input = QLineEdit(self)  

        self.weight_input.setPlaceholderText("وزن (کیلوگرم)")  
        self.height_input.setPlaceholderText("قد (سانتیمتر)")  
        self.age_input.setPlaceholderText("سن")  

        for input_field in [self.weight_input, self.height_input, self.age_input]:  
            input_field.setStyleSheet("border-radius: 5px; padding: 5px;")  
            layout.addWidget(input_field)  

        gender_layout = QHBoxLayout()
        self.gender_combo = QComboBox(self)  
        self.gender_combo.addItems(["مرد", "زن"])  
        gender_layout.addWidget(self.gender_combo)
        gender_layout.addWidget(QLabel("جنسیت:"))
        layout.addLayout(gender_layout)

        exercise_layout = QHBoxLayout()
        self.exercise_combo = QComboBox(self)  
        self.exercise_combo.addItems([
            "هیچ ورزشی", "فوتبال", "والیبال", "بسکتبال", "ورزش کششی", "هوازی در خانه",   
            "هوازی بیرون خانه", "کوه نوردی با شیب کم", "کوه نوردی با شیب زیاد",   
            "پیاده روی", "دویدن", "اسکیت", "پینگ پنگ",   
            "تنیس", "کاراته", "تکواندو", "کنگ فو", "بوکس"
        ])  
        exercise_layout.addWidget(self.exercise_combo)
        exercise_layout.addWidget(QLabel("ورزش انجام شده:"))
        layout.addLayout(exercise_layout)

        button_layout = QHBoxLayout()
        button_layout.addSpacerItem(QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        self.submit_info_button = QPushButton('تایید', self)  
        self.submit_info_button.setStyleSheet("border-radius: 5px; padding: 2px; background-color: #4CAF50; color: white;")  
        self.submit_info_button.setFixedWidth(80)
        self.submit_info_button.setFixedHeight(25)
        self.submit_info_button.clicked.connect(self.save_information)
        self.submit_info_button.clicked.connect(self.open_main_window)
        
        button_layout.addWidget(self.submit_info_button)
        button_layout.addSpacerItem(QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(button_layout)
        self.setLayout(layout)  

    def save_information(self):  
        try:  
            data = {}
            name = self.name_input.text()  
            if name != "":
                data["name"] = name
            weight = float(self.weight_input.text())
            if weight != "":
                data["weight"] = weight
            height = float(self.height_input.text())
            if height != "":
                data["height"] = height
            age = int(self.age_input.text())  
            if age != "":
                data["age"] = age
            gender = self.gender_combo.currentText()  
            if gender != ""
            exercise = self.exercise_combo.currentText()  

            with open("userData.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

                    
                
            # QMessageBox.information(self, 'اطلاعات ذخیره شد',   
                                    # f'نام: {name}, وزن: {weight}, قد: {height}, جنسیت: {gender}, سن: {age}, ورزش: {exercise}')  
        except ValueError:  
            QMessageBox.warning(self, 'خطا', 'لطفا اطلاعات را کامل و صحیح وارد کنید.')
    def open_main_window(self):
        self.close()
        self.main_window = MainWindow()  
        self.main_window.show()




         

#######
####### Main window
#######

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
            "gender_combobox": (40, 380, 300, 80),
        }

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.section1 = QFrame(self.main_widget)
        self.section1.setStyleSheet("background-color: rgba(183, 182, 183, 0.24); border-right: 1px solid #ccc; padding: 10px;")
        self.section1.setGeometry(0, 0, 1400 // 3, 1000)

        self.label = QLabel("ثبت فعالیت جدید", self.section1)
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: none;")
        self.label.setAlignment(Qt.AlignTop)
        self.label.setGeometry(*self.positions["label"])


        
        #ليبل براي نمايش اطلاعات
        self.label_empty = QLabel('test', self.main_widget)
        self.label_empty.setGeometry(680, 50, 500, 400)
        self.label_empty.setStyleSheet("background-color: none; color: black")


        #ليبل براي نمودار دايره اي نسبت زمان به کالري سوخته شده 
        self.label_cal = QLabel('', self.main_widget)
        self.label_cal.setGeometry(10, 300, 440, 440)
        self.label_cal.setStyleSheet("background-color: none;")




        #ليبل براي نمودار ستوني مقايسه هفت روز آخر
        self.label_last7 = QLabel('', self.main_widget)
        self.label_last7.setGeometry(680, 550, 440, 440)
        self.label_last7.setStyleSheet("background-color: none;")


        
        
        
        

        self.time_label = QLabel("مدت زمان انجام فعالیت", self.section1)
        self.time_label.setFont(QFont('Arial', 12))
        self.time_label.setStyleSheet("background-color: none;")
        self.time_label.setGeometry(*self.positions["time_label"])

        self.time_edit = QTimeEdit(self.section1)
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setTime(QTime(0, 0))
        self.time_edit.setStyleSheet("border-radius: 10px;")
        self.time_edit.setGeometry(*self.positions["time_edit"])

        self.push_button = QPushButton(self.section1)
        self.push_button.setText("")
        icon_pixmap = QPixmap(r"add.png")
        self.push_button.setIcon(QIcon(icon_pixmap))
        self.push_button.setIconSize(QSize(40, 40))
        self.push_button.setFixedSize(60, 60)
        self.push_button.setStyleSheet("border-radius: 15px; background-color: rgba(76, 175, 80, 1);")
        self.push_button.setGeometry(*self.positions["push_button"])
        
        self.push_button.clicked.connect(self.push_buttonadd)




        self.section2 = QFrame(self.main_widget)
        self.section2.setStyleSheet("background-color: rgba(252, 252, 252, 0.95); border-left: 1px solid #ccc;")
        self.section2.setGeometry(1400 // 3, 0, (1400 // 3) * 2, 1000)

        self.button2 = QPushButton(self.main_widget)
        self.button2.setText("")
        icon_pixmap2 = QPixmap(r"setting.png")
        self.button2.setIcon(QIcon(icon_pixmap2))
        self.button2.setIconSize(QSize(30, 30))
        self.button2.setFixedSize(30, 30)
        self.button2.setStyleSheet("border-radius: 15px; background-color: rgba(156, 154, 154, 0.6);")
        self.button2.setGeometry(*self.positions["settings_button"])
        self.button2.clicked.connect(self.toggle_settings_panel)

        self.overlay = QFrame(self.main_widget)
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.overlay.setGeometry(0, 0, 0, 0)
        self.overlay.hide()

        self.settings_panel = QFrame(self.main_widget)
        self.settings_panel.setStyleSheet("background-color: white;")
        self.settings_panel.setGeometry(350, 150, 700, 700)
        self.settings_panel.hide()

        self.settings_title = QLabel("تنظیمات", self.settings_panel)
        self.settings_title.setFont(QFont('Arial', 10))
        self.settings_title.setStyleSheet("background-color: transparent; border: none; color: black;")
        self.settings_title.setGeometry(10, 10, 70, 30)

        self.tabs = QTabWidget(self.settings_panel)
        self.tabs.setGeometry(0, 30, 700, 670)
        self.tabs.setLayoutDirection(Qt.RightToLeft)

        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tabs.addTab(self.tab1, "اصلی")

        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout(self.tab2)
        self.tabs.addTab(self.tab2, "ظاهری")

        self.radio_day = QRadioButton("حالت روز", self.tab2)
        self.radio_night = QRadioButton("حالت شب", self.tab2)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.radio_day)
        radio_layout.addWidget(self.radio_night)
        self.tab2_layout.addLayout(radio_layout)

        self.radio_day.setChecked(True)
        self.radio_day.toggled.connect(self.update_theme)
        self.radio_night.toggled.connect(self.update_theme)

        self.back_button = QPushButton(self.settings_panel)
        self.back_button.setGeometry(10, 626, 60, 60)
        back_icon = QIcon(r"arrow_back_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png")
        self.back_button.setIcon(back_icon)
        self.back_button.setIconSize(QSize(30, 30))
        self.back_button.setText(" ")
        self.back_button.setStyleSheet("border-radius: 15px; background-color: rgba(156, 154, 154, 0.6);")
        self.back_button.clicked.connect(self.toggle_settings_panel)

        # ایجاد ورودی‌های تب اصلی
        self.name_input = QLineEdit(self.tab1)
        self.name_input.setPlaceholderText("نام خود را وارد کنید")
        self.name_input.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 20px;")
        self.name_input.setGeometry(360, 100, 300, 80)

        self.weight_input = QLineEdit(self.tab1)
        self.weight_input.setPlaceholderText("وزن خود را وارد کنید")
        self.weight_input.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 20px;")
        self.weight_input.setGeometry(40, 100, 300, 80)

        self.height_input = QLineEdit(self.tab1)
        self.height_input.setPlaceholderText("قد خود را وارد کنید")
        self.height_input.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 20px;")
        self.height_input.setGeometry(360, 230, 300, 80)

        self.age_input = QLineEdit(self.tab1)
        self.age_input.setPlaceholderText("سن خود را وارد کنید")
        self.age_input.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 20px;")
        self.age_input.setGeometry(40, 230, 300, 80)

        self.gender_combobox = QComboBox(self.tab1)
        self.gender_combobox.addItem("مرد")
        self.gender_combobox.addItem("زن")
        self.gender_combobox.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 20px;")
        self.gender_combobox.setGeometry(*self.positions["gender_combobox"])

        self.sports_combobox = QComboBox(self.tab1)
        self.sports_combobox.addItems([
            "هیچ ورزشی", "فوتبال", "والیبال", "بسکتبال", "ورزش کششی", "هوازی در خانه",
            "هوازی بیرون خانه", "کوه نوردی با شیب کم", "کوه نوردی با شیب زیاد", "پیاده روی",
            "دویدن", "اسکیت", "پینگ پنگ", "تنیس", "کاراته", "تکواندو", "کنگ فو", "بوکس"
        ])
        self.sports_combobox.setStyleSheet("border-radius: 10px; padding: 5px; font-size: 20px;")
        self.sports_combobox.setGeometry(360, 380, 300, 80)

        self.gender_label = QLabel("جنسیت خود را وارد کنید", self.tab1)
        self.gender_label.setFont(QFont('Arial', 13))
        self.gender_label.setStyleSheet("background-color: transparent; border: none; color: black;")
        self.gender_label.setGeometry(35, 340, 300, 40)

        self.sport_label = QLabel("رشته ورزشی خود را وارد کنید", self.tab1)
        self.sport_label.setFont(QFont('Arial', 13))
        self.sport_label.setStyleSheet("background-color: transparent; border: none; color: black;")
        self.sport_label.setGeometry(360, 340, 300, 40)

        self.ok_button = QPushButton(self.tab1)
        self.ok_button.setIcon(QIcon(r"select_check_box_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png"))
        self.ok_button.setStyleSheet("QPushButton { border-radius: 15px; background-color: rgba(76, 175, 80, 1); border: none; }")
        self.ok_button.setGeometry(336, 550, 60, 60)
        self.ok_button.setIconSize(QSize(30, 30))
        self.ok_button.clicked.connect(self.save_data)

        self.is_night = self.check_if_night()
        self.apply_theme(self.is_night)
        self.update_radio_buttons()
    #تابع دکمه افزودن
    def push_buttonadd(self):
        """Add a new sports activity"""
        
        with open("userData.json", "r") as f:
            data = json.load(f)

        print(data["weight"], data["height"], data["age"], data["gender"], data["sport"])
        
        sport_t = {
            "هیچ ورزشی": "none",
            "ورزش کششی":"gymnastics",
            "هوازی در خانه": "aerobics",
            "هوازی بیرون خانه":"aerobic_outdoors",
            "کوه نوردی با شیب کم":"hiking",
            "کوه نوردی با شیب زیاد":"rockclimbing",
            "پیاده روی":"walking",
            "دویدن":"running",
            "اسکیت":"skating",
            "فوتبال":"soccer",
            "والیبال":"volleyball",
            "بسکتبال":"basketball",
            "پینگ پنگ":"pingpong",
            "تنیس":"tennis",
            "کاراته":"karate",
            "تکواندو":"tekwando",
            "کنگ فو":"kungfo",
            "بوکس":"boxing",
        }

        gender = {
            "مرد": "male",
            "زن": "female"
        }

    
    def toggle_settings_panel(self):
        if self.settings_panel.isVisible():
            self.settings_panel.hide()
            self.overlay.hide()
        else:
            self.settings_panel.show()
            self.overlay.setGeometry(0, 0, 1400, 1000)
            self.overlay.show()

    def update_theme(self):
        if self.radio_night.isChecked():
            self.apply_theme(True)
        else:
            self.apply_theme(False)

    def apply_theme(self, is_night):
        if is_night:
            self.setStyleSheet("background-color: black; color: white;")
            self.label.setStyleSheet("color: white; background-color: transparent;")
            self.settings_title.setStyleSheet("background-color: transparent; color: white;")
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

            self.gender_label.setStyleSheet("background-color: none; border: none; color:rgb(247, 247, 247)")
            self.sport_label.setStyleSheet("background-color: none; border: none; color: rgb(247, 247, 247)")
        
 
            
            
        else:
            self.setStyleSheet("background-color: white; color: black;")
            self.label.setStyleSheet("color: black; background-color: transparent;")
            self.settings_title.setStyleSheet("background-color: transparent; color: black;")
            self.time_label.setStyleSheet("background-color: transparent; border-radius: 10px; color: black;")
            self.time_edit.setStyleSheet("border-radius: 10px; color: black; background-color: white;")
            self.push_button.setStyleSheet("border-radius: 15px; background-color: rgba(76, 175, 80, 1);")
            self.button2.setStyleSheet("border-radius: 15px; background-color: rgba(156, 154, 154, 0.6);")
            self.section1.setStyleSheet("background-color: rgba(183, 182, 183, 0.24); border-right: 1px solid #ccc;")
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

            self.gender_label.setStyleSheet("background-color: none; border: none; color: rgb(39, 39, 39)")
            self.sport_label.setStyleSheet("background-color: none; border: none; color: rgb(39, 39, 39)")
             

    def check_if_night(self):
        current_time = QTime.currentTime()
        return current_time.hour() >= 19 or current_time.hour() <= 6

    def update_radio_buttons(self):
        if self.is_night:
            self.radio_night.setChecked(True)
        else:
            self.radio_day.setChecked(True)

    def save_data(self):
        data = {
            "name": self.name_input.text(),
            "weight": self.weight_input.text(),
            "height": self.height_input.text(),
            "age": self.age_input.text(),
            "gender": self.gender_combobox.currentText(),
            "sport": self.sports_combobox.currentText()
        }
        try:
            with open("userData.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            self.settings_panel.hide()
            self.overlay.hide()
        except Exception:
            pass



if not "userData.json" in os.listdir():
    if __name__ == '__main__':  
        app = QApplication(sys.argv)  
        setup = Setup()
        setup.show()
        sys.exit(app.exec_())
else:
    if __name__ == '__main__':  
        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec_()
