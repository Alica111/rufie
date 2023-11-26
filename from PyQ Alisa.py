from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QVBoxLayout
app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('индекс руфье')
main_win.resize(400,200)

text1=QLabel('добро пожаловать в индекс руфье')

text2=QLabel('Оценка работоспособности сердца ')

button = QPushButton('начать')
v1=QVBoxLayout()
v1.addWidget(text1, alignment= Qt.AlignCenter)
v1.addWidget(text2, alignment= Qt.AlignCenter)
v1.addWidget(button, alignment= Qt.AlignCenter)
main_win.setLayout(v1)


main_win.show()
app.exec_()