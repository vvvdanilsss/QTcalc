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

err_zero_div = 'Деление на ноль!'
err_undefined = 'Результат не определён'

def_font_size = 16
def_val_font_size = 32


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.val_max_len = self.ui.lineEdit.maxLength()

        QFontDatabase.addApplicationFont(("fonts/Rubik-Regular.ttf"))

        # Отображение цифр в lineEdit
        self.ui.btn_0.clicked.connect(self.add_dig)
        self.ui.btn_1.clicked.connect(self.add_dig)
        self.ui.btn_2.clicked.connect(self.add_dig)
        self.ui.btn_3.clicked.connect(self.add_dig)
        self.ui.btn_4.clicked.connect(self.add_dig)
        self.ui.btn_5.clicked.connect(self.add_dig)
        self.ui.btn_6.clicked.connect(self.add_dig)
        self.ui.btn_7.clicked.connect(self.add_dig)
        self.ui.btn_8.clicked.connect(self.add_dig)
        self.ui.btn_9.clicked.connect(self.add_dig)

        # Выполнение кнопок действий
        self.ui.btn_cl.clicked.connect(self.clear_all)
        self.ui.btn_del.clicked.connect(self.delete)
        self.ui.btn_point.clicked.connect(self.add_point)
        self.ui.btn_neg.clicked.connect(self.set_neg)
        self.ui.btn_back.clicked.connect(self.backspace)

        # Математика
        self.ui.btn_calc.clicked.connect(self.calc)
        self.ui.btn_plus.clicked.connect(lambda: self.add_sign('+'))
        self.ui.btn_sub.clicked.connect(lambda: self.add_sign('-'))
        self.ui.btn_mul.clicked.connect(lambda: self.add_sign('*'))
        self.ui.btn_div.clicked.connect(lambda: self.add_sign('/'))

    def add_dig(self) -> None:
        """
        Добавляет цифры в строку ввода
        :return:
        """
        self.rm_err()
        self.clear_temp_ex_if_eq()
        btn = self.sender()
        dig_btn = (
            'btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
            'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9'
        )

        if btn.objectName() in dig_btn:
            if self.ui.lineEdit.text() == '0':
                self.ui.lineEdit.setText(btn.text())
            else:
                self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn.text())

            self.reg_val_font_size()

    def clear_all(self) -> None:
        """
        Чистит строку ввода и временное выражение сверху
        :return:
        """
        self.rm_err()
        self.ui.lineEdit.setText('0')
        self.reg_val_font_size()
        self.ui.label.clear()

    def delete(self) -> None:
        """
        Чистит только строку вывода
        :return:
        """
        self.rm_err()
        self.clear_temp_ex_if_eq()
        self.ui.lineEdit.setText('0')
        self.reg_val_font_size()

    def add_point(self) -> None:
        """
        Добавляет точку в строку ввода
        :return:
        """
        self.clear_temp_ex_if_eq()

        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')
            self.reg_val_font_size()

    def add_temp_ex(self, sign: str) -> None:
        """
        Добавление временного выражения
        :param sign: Знак математической операции
        :return:
        """
        if not self.ui.label.text() or self.get_sign() == '=':
            self.ui.label.setText(f'{self.rm_zeros(self.ui.lineEdit.text())} {sign} ')
            self.reg_val_temp_ex_font_size()
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

    def get_val_temp_ex(self) -> Union[float, int, None]:
        """
        Получение числа из временного выражения
        :return: Число или ничего
        """
        if self.ui.label.text():
            val_temp_ex = self.ui.label.text().strip('.').split()[0]
            return float(val_temp_ex) if '.' in val_temp_ex else int(val_temp_ex)

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
            try:
                res = self.rm_zeros(
                    str(sings[self.get_sign()](self.get_val_temp_ex(), self.get_val()))
                )
                self.ui.label.setText(val_temp_ex + self.rm_zeros(val) + ' = ')
                self.reg_val_temp_ex_font_size()
                self.ui.lineEdit.setText(res)
                self.reg_val_font_size()
                return res
            except KeyError:
                pass
            except ZeroDivisionError:
                if self.get_val_temp_ex() == 0:
                    self.show_err(err_undefined)
                else:
                    self.show_err(err_zero_div)

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

        self.reg_val_temp_ex_font_size()

    def set_neg(self):
        """
        Меняет знак у числа
        :return:
        """
        self.clear_temp_ex_if_eq()
        val = self.ui.lineEdit.text()

        if '-' not in val:
            if val != '0':
                val = '-' + val
        else:
            val = val[1:]

        if len(val) == self.val_max_len + 1 and '-' in val:
            self.ui.lineEdit.setMaxLength(self.val_max_len + 1)
        else:
            self.ui.lineEdit.setMaxLength(self.val_max_len)

        self.ui.lineEdit.setText(val)
        self.reg_val_font_size()

    def backspace(self) -> None:
        """
        Удаляет последнюю цифру в строке ввода
        :return:
        """
        self.rm_err()
        self.clear_temp_ex_if_eq()
        val = self.ui.lineEdit.text()

        if len(val) != 1:
            if len(val) == 2 and '-' in val:
                self.ui.lineEdit.setText('0')
            else:
                self.ui.lineEdit.setText(val[:-1])
            self.reg_val_font_size()
        else:
            self.delete()

    def clear_temp_ex_if_eq(self) -> None:
        """
        Удаляет временное выражение, если в нем есть знак равно
        :return:
        """
        if self.get_sign() == '=':
            self.ui.label.clear()

    def show_err(self, err: str) -> None:
        """
        Вывод ошибки
        :param err: Ошибка
        :return:
        """
        self.ui.lineEdit.setMaxLength(len(err))
        self.ui.lineEdit.setText(err)
        self.reg_val_font_size()
        self.dis_btn(True)

    def rm_err(self) -> None:
        """
        Удаляет ошибку
        :return:
        """
        if self.ui.lineEdit.text() in (err_zero_div, err_undefined):
            self.ui.lineEdit.setMaxLength(self.val_max_len)
            self.ui.lineEdit.setText('0')
            self.reg_val_font_size()
            self.dis_btn(False)

    def dis_btn(self, dis: bool) -> None:
        """
        Блокирует/деблокирует кнопки при ошибке
        :param dis: Блокирует/деблокирует
        :return:
        """
        self.ui.btn_calc.setDisabled(dis)
        self.ui.btn_plus.setDisabled(dis)
        self.ui.btn_sub.setDisabled(dis)
        self.ui.btn_mul.setDisabled(dis)
        self.ui.btn_div.setDisabled(dis)
        self.ui.btn_neg.setDisabled(dis)
        self.ui.btn_point.setDisabled(dis)

        color = 'color: sandybrown' if dis else 'color: white'
        self.change_btn_color(color)

    def change_btn_color(self, color: str) -> None:
        """
        Меняет цвет при блокировке кнопок
        :param color: Устанавливаемый цвет
        :return:
        """
        self.ui.btn_calc.setStyleSheet(color)
        self.ui.btn_plus.setStyleSheet(color)
        self.ui.btn_sub.setStyleSheet(color)
        self.ui.btn_mul.setStyleSheet(color)
        self.ui.btn_div.setStyleSheet(color)
        self.ui.btn_neg.setStyleSheet(color)
        self.ui.btn_point.setStyleSheet(color)

    def get_val_text_width(self) -> int:
        return self.ui.lineEdit.fontMetrics().boundingRect(self.ui.lineEdit.text()).width()

    def get_val_temp_ex_text_width(self) -> int:
        return self.ui.label.fontMetrics().boundingRect(self.ui.label.text()).width()

    def reg_val_font_size(self) -> None:
        """
        Регулирует размер шрифта в строке ввода
        :return:
        """
        font_size = def_val_font_size
        while self.get_val_text_width() > self.ui.lineEdit.width() - 16:
            font_size -= 1
            self.ui.lineEdit.setStyleSheet(f'font-size: {str(font_size)}pt; border: none;')

        font_size = 1
        while self.get_val_text_width() < self.ui.lineEdit.width() - 48:
            if font_size == 32:
                break

            font_size += 1
            self.ui.lineEdit.setStyleSheet(f'font-size: {str(font_size)}pt; border: none;')

    def reg_val_temp_ex_font_size(self) -> None:
        """
        Регулирует размер шрифта в строке временного выражения
        :return:
        """
        font_size = def_font_size
        while self.get_val_temp_ex_text_width() > self.ui.label.width() - 8:
            font_size -= 1
            self.ui.label.setStyleSheet(f'font-size: {str(font_size)}pt; border: none;')

        font_size = 1
        while self.get_val_temp_ex_text_width() < self.ui.label.width() - 48:
            if font_size == 32:
                break

            font_size += 1
            self.ui.label.setStyleSheet(f'font-size: {str(font_size)}pt; border: none;')

    def resizeEvent(self, event) -> None:
        self.reg_val_font_size()
        self.reg_val_temp_ex_font_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
