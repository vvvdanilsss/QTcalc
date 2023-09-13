# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from form_ui import Ui_Widget
from PySide6 import QtWidgets 

class Widget(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)    
        self.ui.label.setText(QCoreApplication.translate("Widget", u"0", None))


        self.ui.pushButton_0.clicked.connect(lambda: self.number('0'))
        self.ui.pushButton_1.clicked.connect(lambda: self.number('1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.number('2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.number('3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.number('4'))
        self.ui.pushButton_5.clicked.connect(lambda: self.number('5'))
        self.ui.pushButton_6.clicked.connect(lambda: self.number('6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.number('7'))
        self.ui.pushButton_8.clicked.connect(lambda: self.number('8'))
        self.ui.pushButton_9.clicked.connect(lambda: self.number('9'))

        self.ui.pushButton_slesh.clicked.connect(lambda: self.operation('/'))
        self.ui.pushButton_umn.clicked.connect(lambda: self.operation('*'))
        self.ui.pushButton_dot.clicked.connect(lambda: self.operation('.'))
        self.ui.pushButton_plus.clicked.connect(lambda: self.operation('+'))
        self.ui.pushButton_minus.clicked.connect(lambda: self.operation('-'))
        self.ui.pushButton_procent.clicked.connect(lambda: self.operation('%'))

        self.ui.pushButton_delete.clicked.connect(lambda: self.delete_last())
        
        self.ui.pushButton_clean.clicked.connect(lambda: self.clean_all())

        self.ui.pushButton_ravn.clicked.connect(lambda: self.result())

    # Продолжает функциональность при нажатии дальнейших кнопок
    @QtCore.Slot()

    def number(self, entry_text) -> None:
        if self.ui.label.text() == '0':
            self.ui.label.setText(f'{entry_text}')
        elif (self.ui.label.text() == 'SyntaxError') or (self.ui.label.text() == 'MathError'):
            self.ui.label.setText(f'{entry_text}')
        else:
            self.ui.label.setText(f'{self.ui.label.text()}' + entry_text)
        pass

    def operation(self, entry_text) -> None:
        self.ui.label.setText(f'{self.ui.label.text()}' + entry_text)
        pass

    def delete_last(self) -> None:
        x = str(self.ui.label.text())
        self.ui.label.setText(x[0:len(x)-1])
        pass

    def clean_all(self) -> None:
        self.ui.label.setText(QCoreApplication.translate("Widget", u"0", None))
        pass
    
    def result(self) -> None:

        try:
            self.ui.label.setText(f'{eval(self.ui.label.text())}')
        except SyntaxError:
            self.ui.label.setText(QCoreApplication.translate("Widget", u"SyntaxError", None))
        except ZeroDivisionError:
            self.ui.label.setText(QCoreApplication.translate("Widget", u"MathError", None))
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
