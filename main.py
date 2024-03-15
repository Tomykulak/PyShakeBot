import bot_engine
import sys
import json
from PyQt5.QtWidgets import (QMessageBox, QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)

def main():
    bot_engine.start('w54')

tact = 'xp'

class Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Choose your tactic: ')
        self.rbtn1 = QRadioButton('XP')
        self.rbtn2 = QRadioButton('Gold')
        self.label2 = QLabel("")
        self.startBtn = QPushButton("Start!")
        self.stopBtn = QPushButton("Stop!")

        self.rbtn1.toggled.connect(self.onClicked)
        self.rbtn2.toggled.connect(self.onClicked)
        self.startBtn.clicked.connect(self.start)


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.rbtn1)
        layout.addWidget(self.rbtn2)
        layout.addWidget(self.label2)
        layout.addWidget(self.startBtn)



        self.setGeometry(200, 200, 300, 150)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Radio Button Example')

        

        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                       "Are you sure to quit?", QMessageBox.Yes |
                                        QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label2.setText("Your tactic is " + radioBtn.text())
            tact = radioBtn.text()
            print(tact)
    def start(self):
        print(tact)
        configuration = {"tact":tact}
        jsonString = json.dumps(configuration)
        jsonFile = open("config.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
        main()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())

