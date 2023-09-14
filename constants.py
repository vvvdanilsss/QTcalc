from operator import add, sub, mul, truediv

# Dictionary of operators
OPERATORS = {
    '+': add,
    '−': sub,
    '×': mul,
    '/': truediv
}

# Error messages
ERR_ZERO_DIVISION = 'Division by zero!'
ERR_UNDEFINED_RESULT = 'Result is undefined'

# Default font sizes
DEFAULT_FONT_SIZE = 16
DEFAULT_VALUE_FONT_SIZE = 32

# Digit buttons
DIGIT_BUTTONS = (
    'btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
    'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9'
)
