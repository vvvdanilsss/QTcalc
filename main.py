# This Python file uses the following encoding: utf-8
import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QFontDatabase

from ui_form import Ui_Widget

# Dictionary of operators
operators = {
    '+': add,
    '−': sub,
    '×': mul,
    '/': truediv
}

# Error messages
err_zero_division = 'Division by zero!'
err_undefined_result = 'Result is undefined'

# Default font sizes
default_font_size = 16
default_value_font_size = 32


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Maximum input length
        self.max_input_length = self.ui.lineEdit.maxLength()
        self.input_field = self.ui.lineEdit
        self.temp_expression_label = self.ui.label

        # Load font
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        # Connect events to buttons
        # Numbers
        self.ui.btn_0.clicked.connect(self.add_digit)
        self.ui.btn_1.clicked.connect(self.add_digit)
        self.ui.btn_2.clicked.connect(self.add_digit)
        self.ui.btn_3.clicked.connect(self.add_digit)
        self.ui.btn_4.clicked.connect(self.add_digit)
        self.ui.btn_5.clicked.connect(self.add_digit)
        self.ui.btn_6.clicked.connect(self.add_digit)
        self.ui.btn_7.clicked.connect(self.add_digit)
        self.ui.btn_8.clicked.connect(self.add_digit)
        self.ui.btn_9.clicked.connect(self.add_digit)

        # Action buttons
        self.ui.btn_cl.clicked.connect(self.clear_all)
        self.ui.btn_del.clicked.connect(self.delete)
        self.ui.btn_point.clicked.connect(self.add_decimal_point)
        self.ui.btn_neg.clicked.connect(self.toggle_negative)
        self.ui.btn_back.clicked.connect(self.backspace)

        # Math buttons
        self.ui.btn_calc.clicked.connect(self.calculate)
        self.ui.btn_plus.clicked.connect(self.add_operator)
        self.ui.btn_sub.clicked.connect(self.add_operator)
        self.ui.btn_mul.clicked.connect(self.add_operator)
        self.ui.btn_div.clicked.connect(self.add_operator)

    def add_digit(self) -> None:
        """
        Adds digits to the input field
        """
        self.remove_error()
        self.clear_temp_expression_if_equals()
        btn = self.sender()
        digit_buttons = (
            'btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
            'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9'
        )

        if btn.objectName() in digit_buttons:
            if self.input_field.text() == '0':
                self.input_field.setText(btn.text())
            else:
                self.input_field.setText(self.input_field.text() + btn.text())

            self.adjust_value_font_size()

    def clear_all(self) -> None:
        """
        Clears the input field and the temporary expression label
        """
        self.remove_error()
        self.input_field.setText('0')
        self.adjust_value_font_size()
        self.temp_expression_label.clear()

    def delete(self) -> None:
        """
        Clears only the input field
        """
        self.remove_error()
        self.clear_temp_expression_if_equals()
        self.input_field.setText('0')
        self.adjust_value_font_size()

    def add_decimal_point(self) -> None:
        """
        Adds a decimal point to the input field
        """
        self.clear_temp_expression_if_equals()

        if '.' not in self.input_field.text():
            self.input_field.setText(self.input_field.text() + '.')
            self.adjust_value_font_size()

    def add_temp_expression(self) -> None:
        """
        Adds a temporary expression
        """
        btn = self.sender()
        value = self.remove_trailing_zeros(self.input_field.text())

        if not self.temp_expression_label.text() or self.get_operator() == '=':
            self.temp_expression_label.setText(f'{value} {btn.text()} ')
            self.adjust_temp_expression_font_size()
            self.delete()

    @staticmethod
    def remove_trailing_zeros(value: str) -> str:
        """
        Removes trailing zeros from a floating-point number
        :param value: Floating-point number
        :return: Floating-point number without trailing zeros after the decimal point
        """
        value = str(float(value))
        formatted_value = value.rstrip('0').rstrip('.') if '.' in value else value
        return formatted_value

    def get_value(self) -> Union[float, int]:
        """
        Gets the number from the input field
        :return: Number
        """
        value = self.input_field.text().strip('.')
        return float(value) if '.' in value else int(value)

    def get_value_from_temp_expression(self) -> Union[float, int, None]:
        """
        Gets the number from the temporary expression
        :return: Number or None
        """
        if self.temp_expression_label.text():
            value_temp_expression = self.temp_expression_label.text().strip('.').split()[0]
            return float(value_temp_expression) if '.' in value_temp_expression else int(value_temp_expression)

    def get_operator(self) -> Optional[str]:
        """
        Gets the operator from the temporary expression
        :return: Mathematical operator
        """
        if self.temp_expression_label.text():
            return self.temp_expression_label.text().strip('.').split()[-1]

    def calculate(self) -> Optional[str]:
        """
        Calculates the result
        :return: Result or None
        """
        try:
            result = self.remove_trailing_zeros(
                str(operators[self.get_operator()](self.get_value_from_temp_expression(), self.get_value()))
            )
            self.temp_expression_label.setText(
                f'{self.temp_expression_label.text()}{self.remove_trailing_zeros(self.input_field.text())} =')
            self.input_field.setText(result)
            self.adjust_temp_expression_font_size()
            self.adjust_value_font_size()
            return result
        except KeyError:
            pass
        except ZeroDivisionError:
            if self.get_value_from_temp_expression() == 0:
                self.show_error(err_undefined_result)
            else:
                self.show_error(err_zero_division)

    def add_operator(self) -> None:
        """
        Adds a mathematical operator to the expression
        """
        btn = self.sender()

        if not self.temp_expression_label.text():
            self.add_temp_expression()
        elif self.get_operator() != btn.text():
            if self.get_operator() == '=':
                self.add_temp_expression()
            else:
                self.temp_expression_label.setText(f'{self.temp_expression_label.text()[:-2]}{btn.text()} ')
        else:
            try:
                self.temp_expression_label.setText(f'{self.calculate()} {btn.text()} ')
            except TypeError:
                pass

        self.adjust_temp_expression_font_size()

    def toggle_negative(self) -> None:
        """
        Toggles the sign of the number
        """
        self.clear_temp_expression_if_equals()
        value = self.input_field.text()

        if '-' not in value:
            if value != '0':
                value = '-' + value
        else:
            value = value[1:]

        if len(value) == self.max_input_length + 1 and '-' in value:
            self.input_field.setMaxLength(self.max_input_length + 1)
        else:
            self.input_field.setMaxLength(self.max_input_length)

        self.input_field.setText(value)
        self.adjust_value_font_size()

    def backspace(self) -> None:
        """
        Deletes the last digit in the input field
        """
        self.remove_error()
        self.clear_temp_expression_if_equals()
        value = self.input_field.text()

        if len(value) != 1:
            if len(value) == 2 and '-' in value:
                self.input_field.setText('0')
            else:
                self.input_field.setText(value[:-1])
            self.adjust_value_font_size()
        else:
            self.delete()

    def clear_temp_expression_if_equals(self) -> None:
        """
        Clears the temporary expression if it contains an equals sign
        """
        if self.get_operator() == '=':
            self.ui.label.clear()

    def show_error(self, error: str) -> None:
        """
        Displays an error
        :param error: Error message
        """
        self.input_field.setMaxLength(len(error))
        self.input_field.setText(error)
        self.adjust_value_font_size()
        self.disable_buttons(True)

    def remove_error(self) -> None:
        """
        Removes the error message
        """
        if self.input_field.text() in (err_zero_division, err_undefined_result):
            self.input_field.setMaxLength(self.max_input_length)
            self.input_field.setText('0')
            self.adjust_value_font_size()
            self.disable_buttons(False)

    def disable_buttons(self, disable: bool) -> None:
        """
        Disables/enables buttons when there's an error
        :param disable: Disables/enables
        """
        self.ui.btn_calc.setDisabled(disable)
        self.ui.btn_plus.setDisabled(disable)
        self.ui.btn_sub.setDisabled(disable)
        self.ui.btn_mul.setDisabled(disable)
        self.ui.btn_div.setDisabled(disable)
        self.ui.btn_neg.setDisabled(disable)
        self.ui.btn_point.setDisabled(disable)

        color = 'color: sandybrown' if disable else 'color: white'
        self.change_button_color(color)

    def change_button_color(self, color: str) -> None:
        """
        Changes button color when buttons are disabled
        :param color: Color to set
        """
        self.ui.btn_calc.setStyleSheet(color)
        self.ui.btn_plus.setStyleSheet(color)
        self.ui.btn_sub.setStyleSheet(color)
        self.ui.btn_mul.setStyleSheet(color)
        self.ui.btn_div.setStyleSheet(color)
        self.ui.btn_neg.setStyleSheet(color)
        self.ui.btn_point.setStyleSheet(color)

    def get_input_text_width(self) -> int:
        return self.input_field.fontMetrics().boundingRect(self.input_field.text()).width()

    def get_temp_expression_text_width(self) -> int:
        return self.temp_expression_label.fontMetrics().boundingRect(self.temp_expression_label.text()).width()

    def adjust_value_font_size(self) -> None:
        """
        Adjusts the font size in the input field
        """
        font_size = default_value_font_size
        while self.get_input_text_width() > self.input_field.width() - 16:
            font_size -= 1
            self.input_field.setStyleSheet(f'font-size: {str(font_size)}pt; border: none;')

        font_size = 1
        while self.get_input_text_width() < self.input_field.width() - 48:
            if font_size == 32:
                break

            font_size += 1
            self.input_field.setStyleSheet(f'font-size: {str(font_size)}pt; border: none;')

    def adjust_temp_expression_font_size(self) -> None:
        """
        Adjusts the font size in the temporary expression label
        """
        font_size = default_font_size
        while self.get_temp_expression_text_width() > self.temp_expression_label.width() - 8:
            font_size -= 1
            self.temp_expression_label.setStyleSheet(f'font-size: {str(font_size)}pt; color: sandybrown;')

        font_size = 1
        while self.get_temp_expression_text_width() < self.temp_expression_label.width() - 48:
            if font_size == 16:
                break

            font_size += 1
            self.temp_expression_label.setStyleSheet(f'font-size: {str(font_size)}pt; color: sandybrown;')

    def resizeEvent(self, event) -> None:
        self.adjust_value_font_size()
        self.adjust_temp_expression_font_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
