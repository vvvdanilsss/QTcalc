# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(286, 428)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(286, 428))
        Widget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setKerning(True)
        Widget.setFont(font)
        Widget.setFocusPolicy(Qt.NoFocus)
        Widget.setStyleSheet(u"background-color: black;")
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(12, -1, -1, -1)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Helvetica"])
        font1.setPointSize(50)
        self.label.setFont(font1)
        self.label.setMouseTracking(True)
        self.label.setStyleSheet(u"QLabel {\n"
" qproperty-alignment: 'AlignVCenter | AlignRight';\n"
" overflow: auto;\n"
" color: white;\n"
"}")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_3.setHorizontalSpacing(-1)
        self.gridLayout_3.setContentsMargins(10, 10, 4, 10)
        self.pushButton_minus = QPushButton(Widget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_minus, 3, 3, 1, 1)

        self.pushButton_6 = QPushButton(Widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_plus = QPushButton(Widget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_plus, 2, 3, 1, 1)

        self.pushButton_delete = QPushButton(Widget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"src/calc_with_python//pictures/backspace_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_delete.setIcon(icon)

        self.gridLayout_3.addWidget(self.pushButton_delete, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(Widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_procent = QPushButton(Widget)
        self.pushButton_procent.setObjectName(u"pushButton_procent")
        self.pushButton_procent.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_procent, 0, 2, 1, 1)

        self.pushButton_slesh = QPushButton(Widget)
        self.pushButton_slesh.setObjectName(u"pushButton_slesh")
        self.pushButton_slesh.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_slesh, 0, 3, 1, 1)

        self.pushButton_ravn = QPushButton(Widget)
        self.pushButton_ravn.setObjectName(u"pushButton_ravn")
        self.pushButton_ravn.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_ravn, 4, 3, 1, 1)

        self.pushButton_8 = QPushButton(Widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(Widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_umn = QPushButton(Widget)
        self.pushButton_umn.setObjectName(u"pushButton_umn")
        self.pushButton_umn.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_umn.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_umn, 1, 3, 1, 1)

        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_clean = QPushButton(Widget)
        self.pushButton_clean.setObjectName(u"pushButton_clean")
        self.pushButton_clean.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"src/calc_with_python/pictures/delete_forever_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_clean.setIcon(icon1)

        self.gridLayout_3.addWidget(self.pushButton_clean, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(Widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_1 = QPushButton(Widget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_1.setCheckable(False)
        self.pushButton_1.setChecked(False)
        self.pushButton_1.setAutoRepeat(False)
        self.pushButton_1.setFlat(False)

        self.gridLayout_3.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_dot = QPushButton(Widget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_dot, 4, 2, 1, 1)

        self.pushButton_0 = QPushButton(Widget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setStyleSheet(u"QPushButton {\n"
" background-color: white;\n"
" width: 50px;\n"
" height: 30 px;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_0, 4, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"0", None))
        self.pushButton_minus.setText(QCoreApplication.translate("Widget", u"-", None))
#if QT_CONFIG(shortcut)
        self.pushButton_minus.setShortcut(QCoreApplication.translate("Widget", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"6", None))
#if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut(QCoreApplication.translate("Widget", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_plus.setText(QCoreApplication.translate("Widget", u"+", None))
#if QT_CONFIG(shortcut)
        self.pushButton_plus.setShortcut(QCoreApplication.translate("Widget", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_delete.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_delete.setShortcut(QCoreApplication.translate("Widget", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_9.setText(QCoreApplication.translate("Widget", u"9", None))
#if QT_CONFIG(shortcut)
        self.pushButton_9.setShortcut(QCoreApplication.translate("Widget", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_procent.setText(QCoreApplication.translate("Widget", u"%", None))
#if QT_CONFIG(shortcut)
        self.pushButton_procent.setShortcut(QCoreApplication.translate("Widget", u"%", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_slesh.setText(QCoreApplication.translate("Widget", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_slesh.setShortcut(QCoreApplication.translate("Widget", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_ravn.setText(QCoreApplication.translate("Widget", u"=", None))
#if QT_CONFIG(shortcut)
        self.pushButton_ravn.setShortcut(QCoreApplication.translate("Widget", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_8.setText(QCoreApplication.translate("Widget", u"8", None))
#if QT_CONFIG(shortcut)
        self.pushButton_8.setShortcut(QCoreApplication.translate("Widget", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"5", None))
#if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut(QCoreApplication.translate("Widget", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"2", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("Widget", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_umn.setText(QCoreApplication.translate("Widget", u"x", None))
#if QT_CONFIG(shortcut)
        self.pushButton_umn.setShortcut(QCoreApplication.translate("Widget", u"X", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"3", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("Widget", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_clean.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_clean.setShortcut(QCoreApplication.translate("Widget", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_7.setText(QCoreApplication.translate("Widget", u"7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(QCoreApplication.translate("Widget", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"4", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("Widget", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_1.setText(QCoreApplication.translate("Widget", u"1", None))
#if QT_CONFIG(shortcut)
        self.pushButton_1.setShortcut(QCoreApplication.translate("Widget", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_dot.setText(QCoreApplication.translate("Widget", u".", None))
#if QT_CONFIG(shortcut)
        self.pushButton_dot.setShortcut(QCoreApplication.translate("Widget", u".", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_0.setText(QCoreApplication.translate("Widget", u"0", None))
#if QT_CONFIG(shortcut)
        self.pushButton_0.setShortcut(QCoreApplication.translate("Widget", u"0", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

