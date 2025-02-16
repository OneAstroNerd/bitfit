from PyQt5 import QtCore, QtGui, QtWidgets  

class Ui_MainWindow(object):  
    def setupUi(self, MainWindow):  
        MainWindow.setObjectName("MainWindow")  
        MainWindow.resize(1560, 1100)  
        self.centralwidget = QtWidgets.QWidget(MainWindow)  
        self.centralwidget.setObjectName("centralwidget")  

        font = QtGui.QFont()  
        font.setFamily("B Narm")  
        font.setPointSize(20)  

        self.weight = QtWidgets.QLineEdit(self.centralwidget)  
        self.weight.setGeometry(QtCore.QRect(20, 29, 660, 102))  
        self.weight.setFont(font)  
        self.weight.setObjectName("weight")  

        self.height = QtWidgets.QLineEdit(self.centralwidget)  
        self.height.setGeometry(QtCore.QRect(20, 159, 660, 102))  
        self.height.setFont(font)  
        self.height.setObjectName("height")  

        self.gender = QtWidgets.QLineEdit(self.centralwidget)  
        self.gender.setGeometry(QtCore.QRect(20, 289, 660, 102))  
        self.gender.setFont(font)  
        self.gender.setObjectName("gender")  

        self.age = QtWidgets.QLineEdit(self.centralwidget)  
        self.age.setGeometry(QtCore.QRect(20, 419, 660, 102))  
        self.age.setFont(font)  
        self.age.setObjectName("age")  

        self.exercisetime = QtWidgets.QLineEdit(self.centralwidget)  
        self.exercisetime.setGeometry(QtCore.QRect(20, 549, 660, 102))  
        self.exercisetime.setFont(font)  
        self.exercisetime.setObjectName("exercisetime")  

        self.enter = QtWidgets.QPushButton(self.centralwidget)  
        self.enter.setGeometry(QtCore.QRect(90, 670, 182, 82))  
        self.enter.setFont(font)  
        self.enter.setObjectName("enter")  

        self.output = QtWidgets.QTextBrowser(self.centralwidget)  
        self.output.setGeometry(QtCore.QRect(700, 20, 800, 800))  
        self.output.setObjectName("output")  
        self.output.setFont(font)  

        MainWindow.setCentralWidget(self.centralwidget)  
        self.menubar = QtWidgets.QMenuBar(MainWindow)  
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1560, 18))  
        self.menubar.setObjectName("menubar")  
        MainWindow.setMenuBar(self.menubar)  
        self.statusbar = QtWidgets.QStatusBar(MainWindow)  
        self.statusbar.setObjectName("statusbar")  
        MainWindow.setStatusBar(self.statusbar)  

        self.retranslateUi(MainWindow)  
        QtCore.QMetaObject.connectSlotsByName(MainWindow)  

        self.enter.clicked.connect(self.save_inputs)  

    def retranslateUi(self, MainWindow):  
        _translate = QtCore.QCoreApplication.translate  
        MainWindow.setWindowTitle(_translate("MainWindow", "محاسبه کالری سوزانده شده"))  
        self.weight.setPlaceholderText(_translate("MainWindow", "وزن خود را وارد کنید(kg)"))  
        self.height.setPlaceholderText(_translate("MainWindow", "قد خود را وارد کنید(cm)"))  
        self.gender.setPlaceholderText(_translate("MainWindow", "جنسیت خود را وارد کنید(مرد،زن)"))  
        self.age.setPlaceholderText(_translate("MainWindow", "سن خود را وارد کنید"))  
        self.enter.setText(_translate("MainWindow", "تایید"))  
        self.exercisetime.setPlaceholderText(_translate("MainWindow", "مدت زمان ورزش خود را وارد کنید(min)"))  

    def save_inputs(self):  
        weight_value = self.weight.text()  
        height_value = self.height.text()  
        gender_value = self.gender.text()  
        age_value = self.age.text()  
        exercise_time_value = self.exercisetime.text()  

        exercise_calories = {  
            "فوتبال": 15,  
            "والیبال": 5.2,  
            "بسکتبال": 14,  
            "ورزش کششی": 4.5,  
            "هوازی در خانه": 11,  
            "هوازی در بیرون خانه": 11.1,  
            "کوه نوردی با شیب کم": 10.5,  
            "کوه نوردی با شیب زیاد": 19.3,  
            "پیاده روی": 7,  
            "دویدن": 15.8,  
            "اسکیت": 12.3,  
            "تنیس": 12.3,  
            "پینگ پنگ": 4.3,  
            "کاراته": 14,  
            "تکواندو": 15.6,  
            "کنگ فو": 14.1,  
            "بکس": 15.8,  
        }  

        try:  
            weight = float(weight_value)  
            height_cm = float(height_value)  
            age = float(age_value)  

            if gender_value.lower() == "مرد":  
                base_calories = (655.1 + (9.6 * weight) + (1.8 * height_cm) - (4.7 * age))  
            elif gender_value.lower() == "زن":  
                base_calories = (66.5 + (13.75 * weight) + (5 * height_cm) - (6.755 * age))  
            else:  
                base_calories = None  

            exercise_time = float(exercise_time_value)  
            protein = 0  
            carbohydrates = 0  

            if 20 <= exercise_time <= 30:  
                protein = weight * 0.7  
                carbohydrates = weight * 4  
            elif 31 <= exercise_time <= 60:  
                protein = weight * 1.1  
                carbohydrates = weight * 6  
            elif exercise_time >= 61:  
                protein = weight * 1.7  
                carbohydrates = weight * 8 if exercise_time <= 180 else weight * 10  

            if exercise_time > 0:  
                exercise_dialog = self.show_exercise_choice(exercise_calories)  
                if exercise_dialog is not None:  # exercise selected  
                    calories_per_minute = exercise_calories[exercise_dialog]  
                    total_calories = base_calories + (exercise_time * calories_per_minute)  

                    output_text = (  
                        f"وزن: {weight_value} kg\n"  
                        f"قد: {height_value} cm\n"  
                        f"جنسیت: {gender_value}\n"  
                        f"سن: {age_value} سال\n"  
                        f"مدت زمان ورزش: {exercise_time_value} دقیقه\n"  
                        f"کالری سوزانده شده: {total_calories:.2f} kcal\n"  
                        f"پروتئین مورد نیاز: {protein:.2f} گرم\n"  
                        f"کربوهیدرات مورد نیاز: {carbohydrates:.2f} گرم\n"  
                    )  
                    self.output.setPlainText(output_text)  
            else:  
                if base_calories is not None:  
                    output_text = (  
                        f"وزن: {weight_value} kg\n"  
                        f"قد: {height_value} cm\n"  
                        f"جنسیت: {gender_value}\n"  
                        f"سن: {age_value} سال\n"  
                        f"مدت زمان ورزش: {exercise_time_value} دقیقه\n"  
                        f"کالری سوزانده شده: {base_calories:.2f} kcal\n"  
                        f"پروتئین مورد نیاز: {protein:.2f} گرم\n"  
                        f"کربوهیدرات مورد نیاز: {carbohydrates:.2f} گرم\n"  
                    )  
                    self.output.setPlainText(output_text)  

        except ValueError:  
            self.output.setPlainText("لطفاً مقادیر عددی را به درستی وارد کنید.")  

    def show_exercise_choice(self, exercise_calories):  
        exercise_dialog = QtWidgets.QDialog()  
        exercise_dialog.setWindowTitle("انتخاب رشته ورزشی")  
        exercise_dialog.setGeometry(QtCore.QRect(100, 100, 600, 400))  
        layout = QtWidgets.QVBoxLayout(exercise_dialog)  

        label = QtWidgets.QLabel("لطفاً رشته ورزشی خود را انتخاب کنید:")  
        label.setFont(QtGui.QFont("B Narm", 20))   
        layout.addWidget(label)  

        combo_box = QtWidgets.QComboBox()  
        combo_box.addItems(exercise_calories.keys())  
        combo_box.setFont(QtGui.QFont("B Narm", 20))  
        layout.addWidget(combo_box)  

        button = QtWidgets.QPushButton("تایید")  
        button.setFont(QtGui.QFont("B Narm", 20))  
        layout.addWidget(button)  

        selected_exercise = None  

        def on_confirm():  
            nonlocal selected_exercise  
            selected_exercise = combo_box.currentText()  
            exercise_dialog.accept()  

        button.clicked.connect(on_confirm)  
        exercise_dialog.exec_()  

        return selected_exercise  

if __name__ == "__main__":  
    import sys  
    app = QtWidgets.QApplication(sys.argv)  
    MainWindow = QtWidgets.QMainWindow()  
    ui = Ui_MainWindow()  
    ui.setupUi(MainWindow)  
    MainWindow.show()  
    sys.exit(app.exec_()) 