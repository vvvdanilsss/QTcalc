# -*- coding: utf-8 -*-
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(320, 480)
        Widget.setMinimumSize(QSize(320, 480))
        icon = QIcon()
        icon.addFile(u"icons/calculate.png", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"QWidget {\n"
                             "    color: white;\n"
                             "    background-color: saddlebrown;\n"
                             "    font-family: Rubik;\n"
                             "    font-size: 16pt;\n"
                             "    font-weight: 600;\n"
                             "}\n"
                             "\n"
                             "/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043e\u043a */\n"
                             "QPushButton {\n"
                             "    background-color: transparent;\n"
                             "    border: 2px solid chocolate; /* \u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u0442\u043e\u043b\u0449\u0438\u043d\u0443 \u0438 \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
                             "    border-radius: 10px; /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
                             "    padding: 10px 20px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
                             "}\n"
                             "\n"
                             "/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438"
                             " */\n"
                             "QPushButton:hover {\n"
                             "    background-color: chocolate;\n"
                             "    color: white; /* \u0418\u0437\u043c\u0435\u043d\u0438\u0442\u0435 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
                             "}\n"
                             "\n"
                             "/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
                             "QPushButton:pressed {\n"
                             "    background-color: sandybrown;\n"
                             "}\n"
                             "\n"
                             "/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u044f */\n"
                             "QLineEdit {\n"
                             "    font-size: 32pt;\n"
                             "    border: 2px solid chocolate;\n"
                             "    border-radius: 10px;\n"
                             "    padding: 5px;\n"
                             "}")
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: sandybrown;")
        self.label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(32)
        font1.setBold(True)
        self.lineEdit.setFont(font1)
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setStyleSheet(u"font-size: 32pt;\n"
                                    "border: none;")
        self.lineEdit.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_back = QPushButton(Widget)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u"icons/backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon1)
        self.btn_back.setIconSize(QSize(24, 24))
        self.btn_back.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_back, 0, 2, 1, 1)

        self.btn_4 = QPushButton(Widget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_del = QPushButton(Widget)
        self.btn_del.setObjectName(u"btn_del")
        sizePolicy2.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy2)
        self.btn_del.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_del.setIcon(icon2)
        self.btn_del.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_del, 0, 0, 1, 1)

        self.btn_0 = QPushButton(Widget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_div = QPushButton(Widget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy2)
        self.btn_div.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_calc = QPushButton(Widget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy2.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy2)
        self.btn_calc.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_calc, 4, 3, 1, 1)

        self.btn_3 = QPushButton(Widget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_neg = QPushButton(Widget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy2)
        self.btn_neg.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_neg, 4, 0, 1, 1)

        self.btn_6 = QPushButton(Widget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_point = QPushButton(Widget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy2)
        self.btn_point.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_2 = QPushButton(Widget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_8 = QPushButton(Widget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(Widget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_cl = QPushButton(Widget)
        self.btn_cl.setObjectName(u"btn_cl")
        sizePolicy2.setHeightForWidth(self.btn_cl.sizePolicy().hasHeightForWidth())
        self.btn_cl.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u"icons/clear_all.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cl.setIcon(icon3)
        self.btn_cl.setIconSize(QSize(24, 24))
        self.btn_cl.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_cl, 0, 1, 1, 1)

        self.btn_sub = QPushButton(Widget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)
        self.btn_sub.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_sub, 2, 3, 1, 1)

        self.btn_mul = QPushButton(Widget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)
        self.btn_mul.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_5 = QPushButton(Widget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_1 = QPushButton(Widget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_plus = QPushButton(Widget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy2.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy2)
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_7 = QPushButton(Widget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"QTcalc", None))
        self.lineEdit.setText(QCoreApplication.translate("Widget", u"0", None))
        self.btn_back.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_back.setShortcut(QCoreApplication.translate("Widget", u"Backspace", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("Widget", u"4", None))
        # if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("Widget", u"4", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_del.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_del.setShortcut(QCoreApplication.translate("Widget", u"Del", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("Widget", u"0", None))
        # if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("Widget", u"0", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_div.setText(QCoreApplication.translate("Widget", u"/", None))
        # if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("Widget", u"/", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_calc.setText(QCoreApplication.translate("Widget", u"=", None))
        # if QT_CONFIG(shortcut)
        for sc in ('=', 'Enter', 'Return'):
            QShortcut(sc, self.btn_calc).activated.connect(self.btn_calc.animateClick)
        # endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("Widget", u"3", None))
        # if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("Widget", u"3", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_neg.setText(QCoreApplication.translate("Widget", u"+/-", None))
        self.btn_6.setText(QCoreApplication.translate("Widget", u"6", None))
        # if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("Widget", u"6", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("Widget", u".", None))
        # if QT_CONFIG(shortcut)
        for sc in (',', '.'):
            QShortcut(sc, self.btn_point).activated.connect(self.btn_point.animateClick)
        # endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("Widget", u"2", None))
        # if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("Widget", u"2", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("Widget", u"8", None))
        # if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("Widget", u"8", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("Widget", u"9", None))
        # if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("Widget", u"9", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_cl.setText("")
        self.btn_sub.setText(QCoreApplication.translate("Widget", u"\u2212", None))
        # if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("Widget", u"-", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("Widget", u"\u00d7", None))
        # if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("Widget", u"*", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("Widget", u"5", None))
        # if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("Widget", u"5", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("Widget", u"1", None))
        # if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("Widget", u"1", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_plus.setText(QCoreApplication.translate("Widget", u"+", None))
        # if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("Widget", u"+", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("Widget", u"7", None))
        # if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("Widget", u"7", None))
# endif // QT_CONFIG(shortcut)
# retranslateUi
