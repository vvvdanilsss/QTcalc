# This Python file uses the following encoding: utf-8
import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QFontDatabase

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

sings = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont(("fonts/Rubik-Regular.ttf"))

        # Отображение цифр в lineEdit
        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

        # Выполнение кнопок действий
        self.ui.btn_cl.clicked.connect(self.clear_all)
        self.ui.btn_del.clicked.connect(self.delete)
        self.ui.btn_point.clicked.connect(self.add_point)

        # Математика
        self.ui.btn_calc.clicked.connect(self.calc)
        self.ui.btn_plus.clicked.connect(lambda: self.add_sign('+'))
        self.ui.btn_sub.clicked.connect(lambda: self.add_sign('-'))
        self.ui.btn_mul.clicked.connect(lambda: self.add_sign('*'))
        self.ui.btn_div.clicked.connect(lambda: self.add_sign('/'))

    def add_digit(self, btn_text: str) -> None:
        """
        Добавляет цифры в строку ввода
        :param btn_text: Нажатая цифра
        :return:
        """
        if self.ui.lineEdit.text() == '0':
            self.ui.lineEdit.setText(btn_text)
        else:
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn_text)

    def clear_all(self) -> None:
        """
        Чистит строку ввода и временное выражение сверху
        :return:
        """
        self.ui.lineEdit.setText('0')
        self.ui.label.clear()

    def delete(self) -> None:
        """
        Чистит только строку вывода
        :return:
        """
        self.ui.lineEdit.setText('0')

    def add_point(self) -> None:
        """
        Добавляет точку в строку ввода
        :return:
        """
        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')

    def add_temp_ex(self, sign: str) -> None:
        """
        Добавление временного выражения
        :param sign: Знак математической операции
        :return:
        """
        if not self.ui.label.text() or self.get_sign() == '=':
            self.ui.label.setText(f'{self.rm_zeros(self.ui.lineEdit.text())} {sign} ')
            self.delete()

    @staticmethod
    def rm_zeros(val: str) -> str:
        """
        Удаляет незначащие нули
        :param val: Вещественное число
        :return: Вещественное число без нулей после точки
        """
        val = str(float(val))
        form_val = val.rstrip('0').rstrip('.') if '.' in val else val
        return form_val

    def get_val(self) -> Union[float, int]:
        """
        Получение числа из строки ввода
        :return: Число
        """
        val = self.ui.lineEdit.text().strip('.')
        return float(val) if '.' in val else int(val)

    def get_temp_ex_val(self) -> Union[float, int, None]:
        """
        Получение числа из временного выражения
        :return: Число или ничего
        """
        if self.ui.label.text():
            temp_ex_val = self.ui.label.text().strip('.').split()[0]
            return float(temp_ex_val) if '.' in temp_ex_val else int(temp_ex_val)

    def get_sign(self) -> Optional[str]:
        """
        Получение знака из временного выражения
        :return: Знак математической операции
        """
        if self.ui.label.text():
            return self.ui.label.text().strip('.').split()[-1]

    def calc(self) -> Optional[str]:
        """
        Вычисляет
        :return: Результат вычисления или ничего
        """
        val = self.ui.lineEdit.text()
        val_temp_ex = self.ui.label.text()

        if val_temp_ex:
            res = self.rm_zeros(
                str(sings[self.get_sign()](self.get_temp_ex_val(), self.get_val()))
            )
            self.ui.label.setText(val_temp_ex + self.rm_zeros(val) + ' = ')
            self.ui.lineEdit.setText(res)
            return res

    def add_sign(self, sign: str):
        """
        Добавляет в математическое выражение знак математической операции
        :param sign: Знак математической операции
        :return:
        """
        val_temp_ex = self.ui.label.text()

        if not val_temp_ex:
            self.add_temp_ex(sign)
        elif self.get_sign() != sign:
            if self.get_sign() == '=':
                self.add_temp_ex(sign)
            else:
                self.ui.label.setText(f'{val_temp_ex[:-2]}{sign} ')
        else:
            self.ui.label.setText(f'{self.calc()} {sign}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
