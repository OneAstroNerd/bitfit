import sys  
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QLineEdit, QComboBox, QSpacerItem, QSizePolicy)  
from PyQt5 import QtCore  

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
        button_layout.addSpacerItem(QSpacerItem(340, 20, QSizePolicy.Minimum, QSizePolicy.Minimum))
        
        self.submit_info_button = QPushButton('تایید', self)  
        self.submit_info_button.setStyleSheet("border-radius: 5px; padding: 2px; background-color: #4CAF50; color: white;")  
        self.submit_info_button.setFixedWidth(100)
        self.submit_info_button.setFixedHeight(25)
        self.submit_info_button.clicked.connect(self.save_information)  
        
        button_layout.addWidget(self.submit_info_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)  

    def save_information(self):  
        try:  
            name = self.name_input.text()  
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            age = int(self.age_input.text())  
            gender = self.gender_combo.currentText()  
            exercise = self.exercise_combo.currentText()  

            QMessageBox.information(self, 'اطلاعات ذخیره شد',   
                                    f'نام: {name}, وزن: {weight}, قد: {height}, جنسیت: {gender}, سن: {age}, ورزش: {exercise}')  
        except ValueError:  
            QMessageBox.warning(self, 'خطا', 'لطفا اطلاعات را کامل وارد کنید.')  

if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    setup = Setup()  
    setup.show()  
    sys.exit(app.exec_())
