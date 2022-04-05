# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 700)
        Form.setMinimumSize(QtCore.QSize(700, 700))
        Form.setMaximumSize(QtCore.QSize(700, 700))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 681, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.panelList = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.panelList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.panelList.setStyleSheet("QListWidget::item\n"
"{\n"
"min-width: 106.75px;\n"
"min-height: 50px;\n"
"}")
        self.panelList.setLineWidth(1)
        self.panelList.setAutoScrollMargin(16)
        self.panelList.setObjectName("panelList")
        item = QtWidgets.QListWidgetItem()
        self.panelList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.panelList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.panelList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.panelList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.panelList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.panelList.addItem(item)
        self.horizontalLayout.addWidget(self.panelList)
        self.stackedWidget = QtWidgets.QStackedWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(550, 0))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.MAC = QtWidgets.QWidget()
        self.MAC.setObjectName("MAC")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.MAC)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 541, 321))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 521, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.targetMacLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.targetMacLine.setObjectName("targetMacLine")
        self.horizontalLayout_2.addWidget(self.targetMacLine)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.payloadMacLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.payloadMacLine.setObjectName("payloadMacLine")
        self.horizontalLayout_3.addWidget(self.payloadMacLine)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.timesMacLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.timesMacLine.setObjectName("timesMacLine")
        self.horizontalLayout_4.addWidget(self.timesMacLine)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sendMacBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.sendMacBtn.setObjectName("sendMacBtn")
        self.horizontalLayout_5.addWidget(self.sendMacBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 521, 291))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.sniffTimesMacLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.sniffTimesMacLine.setObjectName("sniffTimesMacLine")
        self.horizontalLayout_6.addWidget(self.sniffTimesMacLine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.sniffStartMacBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.sniffStartMacBtn.setObjectName("sniffStartMacBtn")
        self.verticalLayout_3.addWidget(self.sniffStartMacBtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.sniffStopMacBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.sniffStopMacBtn.setEnabled(False)
        self.sniffStopMacBtn.setObjectName("sniffStopMacBtn")
        self.verticalLayout_3.addWidget(self.sniffStopMacBtn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.stackedWidget.addWidget(self.MAC)
        self.ARP = QtWidgets.QWidget()
        self.ARP.setObjectName("ARP")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.ARP)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 541, 321))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.tab_9)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 0, 521, 291))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_17.addWidget(self.label_17)
        self.opArpCombo = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        self.opArpCombo.setObjectName("opArpCombo")
        self.opArpCombo.addItem("")
        self.opArpCombo.addItem("")
        self.horizontalLayout_17.addWidget(self.opArpCombo)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_18.addWidget(self.label_18)
        self.hwSrcArpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.hwSrcArpLine.setText("")
        self.hwSrcArpLine.setObjectName("hwSrcArpLine")
        self.horizontalLayout_18.addWidget(self.hwSrcArpLine)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_22.addWidget(self.label_19)
        self.ipSrcArpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.ipSrcArpLine.setText("")
        self.ipSrcArpLine.setObjectName("ipSrcArpLine")
        self.horizontalLayout_22.addWidget(self.ipSrcArpLine)
        self.verticalLayout_8.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_23.addWidget(self.label_20)
        self.hwDstArpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.hwDstArpLine.setObjectName("hwDstArpLine")
        self.horizontalLayout_23.addWidget(self.hwDstArpLine)
        self.verticalLayout_8.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_19.addWidget(self.label_15)
        self.ipDstArpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.ipDstArpLine.setObjectName("ipDstArpLine")
        self.horizontalLayout_19.addWidget(self.ipDstArpLine)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.sendArpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.sendArpBtn.setObjectName("sendArpBtn")
        self.horizontalLayout_20.addWidget(self.sendArpBtn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_20)
        self.tabWidget_3.addTab(self.tab_9, "")
        self.stackedWidget.addWidget(self.ARP)
        self.IP = QtWidgets.QWidget()
        self.IP.setObjectName("IP")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.IP)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 541, 321))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.tab_11)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(10, 0, 521, 291))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_25.addWidget(self.label_22)
        self.ipSrcIpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.ipSrcIpLine.setText("")
        self.ipSrcIpLine.setObjectName("ipSrcIpLine")
        self.horizontalLayout_25.addWidget(self.ipSrcIpLine)
        self.verticalLayout_10.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_26.addWidget(self.label_23)
        self.ipDstIpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.ipDstIpLine.setText("")
        self.ipDstIpLine.setObjectName("ipDstIpLine")
        self.horizontalLayout_26.addWidget(self.ipDstIpLine)
        self.verticalLayout_10.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_27.addWidget(self.label_24)
        self.payloadIpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.payloadIpLine.setText("")
        self.payloadIpLine.setObjectName("payloadIpLine")
        self.horizontalLayout_27.addWidget(self.payloadIpLine)
        self.verticalLayout_10.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.sendIpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.sendIpBtn.setObjectName("sendIpBtn")
        self.horizontalLayout_29.addWidget(self.sendIpBtn)
        self.verticalLayout_10.addLayout(self.horizontalLayout_29)
        self.tabWidget_4.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.tab_12)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 0, 521, 291))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem4)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_28.addWidget(self.label_25)
        self.sniffDstIpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_11)
        self.sniffDstIpLine.setObjectName("sniffDstIpLine")
        self.horizontalLayout_28.addWidget(self.sniffDstIpLine)
        self.verticalLayout_11.addLayout(self.horizontalLayout_28)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem5)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_30.addWidget(self.label_26)
        self.sniffTimesIpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_11)
        self.sniffTimesIpLine.setObjectName("sniffTimesIpLine")
        self.horizontalLayout_30.addWidget(self.sniffTimesIpLine)
        self.verticalLayout_11.addLayout(self.horizontalLayout_30)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem6)
        self.sniffStartIpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_11)
        self.sniffStartIpBtn.setObjectName("sniffStartIpBtn")
        self.verticalLayout_11.addWidget(self.sniffStartIpBtn)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem7)
        self.sniffStopIpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_11)
        self.sniffStopIpBtn.setEnabled(False)
        self.sniffStopIpBtn.setObjectName("sniffStopIpBtn")
        self.verticalLayout_11.addWidget(self.sniffStopIpBtn)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem8)
        self.tabWidget_4.addTab(self.tab_12, "")
        self.stackedWidget.addWidget(self.IP)
        self.UDP = QtWidgets.QWidget()
        self.UDP.setObjectName("UDP")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.UDP)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 0, 541, 321))
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.tab_13)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(10, 0, 521, 291))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_31.addWidget(self.label_27)
        self.ipSrcUdpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.ipSrcUdpLine.setText("")
        self.ipSrcUdpLine.setObjectName("ipSrcUdpLine")
        self.horizontalLayout_31.addWidget(self.ipSrcUdpLine)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_31.addWidget(self.label_5)
        self.portSrcUdpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.portSrcUdpLine.setMinimumSize(QtCore.QSize(100, 0))
        self.portSrcUdpLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.portSrcUdpLine.setObjectName("portSrcUdpLine")
        self.horizontalLayout_31.addWidget(self.portSrcUdpLine)
        self.verticalLayout_12.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_32.addWidget(self.label_28)
        self.ipDstUdpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.ipDstUdpLine.setObjectName("ipDstUdpLine")
        self.horizontalLayout_32.addWidget(self.ipDstUdpLine)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_32.addWidget(self.label_6)
        self.portDstUdpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.portDstUdpLine.setMinimumSize(QtCore.QSize(100, 0))
        self.portDstUdpLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.portDstUdpLine.setObjectName("portDstUdpLine")
        self.horizontalLayout_32.addWidget(self.portDstUdpLine)
        self.verticalLayout_12.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.sendUdpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_12)
        self.sendUdpBtn.setObjectName("sendUdpBtn")
        self.horizontalLayout_34.addWidget(self.sendUdpBtn)
        self.verticalLayout_12.addLayout(self.horizontalLayout_34)
        self.tabWidget_5.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.tab_14)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(10, 0, 521, 291))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_35.addWidget(self.label_30)
        self.sniffIpDstUdpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.sniffIpDstUdpLine.setObjectName("sniffIpDstUdpLine")
        self.horizontalLayout_35.addWidget(self.sniffIpDstUdpLine)
        self.verticalLayout_13.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_37.addWidget(self.label_32)
        self.sniffPortDstUdpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.sniffPortDstUdpLine.setObjectName("sniffPortDstUdpLine")
        self.horizontalLayout_37.addWidget(self.sniffPortDstUdpLine)
        self.verticalLayout_13.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_36.addWidget(self.label_31)
        self.sniffTimesUdpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.sniffTimesUdpLine.setObjectName("sniffTimesUdpLine")
        self.horizontalLayout_36.addWidget(self.sniffTimesUdpLine)
        self.verticalLayout_13.addLayout(self.horizontalLayout_36)
        self.sniffStartUdpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.sniffStartUdpBtn.setObjectName("sniffStartUdpBtn")
        self.verticalLayout_13.addWidget(self.sniffStartUdpBtn)
        self.sniffStopUdpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.sniffStopUdpBtn.setEnabled(False)
        self.sniffStopUdpBtn.setObjectName("sniffStopUdpBtn")
        self.verticalLayout_13.addWidget(self.sniffStopUdpBtn)
        self.tabWidget_5.addTab(self.tab_14, "")
        self.stackedWidget.addWidget(self.UDP)
        self.TCP = QtWidgets.QWidget()
        self.TCP.setObjectName("TCP")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.TCP)
        self.tabWidget_6.setGeometry(QtCore.QRect(0, 0, 541, 321))
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.tab_15)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(10, 0, 521, 291))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_33 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_38.addWidget(self.label_33)
        self.ipSrcTcpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.ipSrcTcpLine.setText("")
        self.ipSrcTcpLine.setObjectName("ipSrcTcpLine")
        self.horizontalLayout_38.addWidget(self.ipSrcTcpLine)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_38.addWidget(self.label_7)
        self.portSrcTcpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.portSrcTcpLine.setMinimumSize(QtCore.QSize(100, 0))
        self.portSrcTcpLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.portSrcTcpLine.setObjectName("portSrcTcpLine")
        self.horizontalLayout_38.addWidget(self.portSrcTcpLine)
        self.verticalLayout_14.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_34 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_39.addWidget(self.label_34)
        self.ipDstTcpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.ipDstTcpLine.setObjectName("ipDstTcpLine")
        self.horizontalLayout_39.addWidget(self.ipDstTcpLine)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_39.addWidget(self.label_8)
        self.portDstTcpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.portDstTcpLine.setMinimumSize(QtCore.QSize(100, 0))
        self.portDstTcpLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.portDstTcpLine.setObjectName("portDstTcpLine")
        self.horizontalLayout_39.addWidget(self.portDstTcpLine)
        self.verticalLayout_14.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.sendTcpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_14)
        self.sendTcpBtn.setObjectName("sendTcpBtn")
        self.horizontalLayout_41.addWidget(self.sendTcpBtn)
        self.verticalLayout_14.addLayout(self.horizontalLayout_41)
        self.tabWidget_6.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.tab_16)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(10, 0, 521, 291))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.label_36 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_42.addWidget(self.label_36)
        self.sniffIpDstTcpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_15)
        self.sniffIpDstTcpLine.setObjectName("sniffIpDstTcpLine")
        self.horizontalLayout_42.addWidget(self.sniffIpDstTcpLine)
        self.verticalLayout_15.addLayout(self.horizontalLayout_42)
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.label_37 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_43.addWidget(self.label_37)
        self.sniffPortDstTcpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_15)
        self.sniffPortDstTcpLine.setObjectName("sniffPortDstTcpLine")
        self.horizontalLayout_43.addWidget(self.sniffPortDstTcpLine)
        self.verticalLayout_15.addLayout(self.horizontalLayout_43)
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.label_38 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_44.addWidget(self.label_38)
        self.sniffTimesTcpLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_15)
        self.sniffTimesTcpLine.setObjectName("sniffTimesTcpLine")
        self.horizontalLayout_44.addWidget(self.sniffTimesTcpLine)
        self.verticalLayout_15.addLayout(self.horizontalLayout_44)
        self.sniffStartTcpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_15)
        self.sniffStartTcpBtn.setObjectName("sniffStartTcpBtn")
        self.verticalLayout_15.addWidget(self.sniffStartTcpBtn)
        self.sniffStopTcpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_15)
        self.sniffStopTcpBtn.setEnabled(False)
        self.sniffStopTcpBtn.setObjectName("sniffStopTcpBtn")
        self.verticalLayout_15.addWidget(self.sniffStopTcpBtn)
        self.tabWidget_6.addTab(self.tab_16, "")
        self.stackedWidget.addWidget(self.TCP)
        self.Receiver = QtWidgets.QWidget()
        self.Receiver.setObjectName("Receiver")
        self.packetList = QtWidgets.QListWidget(self.Receiver)
        self.packetList.setGeometry(QtCore.QRect(0, 0, 541, 131))
        self.packetList.setObjectName("packetList")
        self.packetByteBrowser = QtWidgets.QTextEdit(self.Receiver)
        self.packetByteBrowser.setGeometry(QtCore.QRect(0, 140, 541, 141))
        self.packetByteBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.packetByteBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.packetByteBrowser.setObjectName("packetByteBrowser")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Receiver)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 290, 541, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.startReceiveBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startReceiveBtn.setObjectName("startReceiveBtn")
        self.horizontalLayout_7.addWidget(self.startReceiveBtn)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.stopReceiveBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopReceiveBtn.setEnabled(False)
        self.stopReceiveBtn.setObjectName("stopReceiveBtn")
        self.horizontalLayout_7.addWidget(self.stopReceiveBtn)
        self.stackedWidget.addWidget(self.Receiver)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Terminal = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.Terminal.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Terminal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Terminal.setObjectName("Terminal")
        self.verticalLayout.addWidget(self.Terminal)
        self.clearTerminalBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clearTerminalBtn.setObjectName("clearTerminalBtn")
        self.verticalLayout.addWidget(self.clearTerminalBtn)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.panelList.isSortingEnabled()
        self.panelList.setSortingEnabled(False)
        item = self.panelList.item(0)
        item.setText(_translate("Form", "MAC"))
        item = self.panelList.item(1)
        item.setText(_translate("Form", "ARP"))
        item = self.panelList.item(2)
        item.setText(_translate("Form", "IP"))
        item = self.panelList.item(3)
        item.setText(_translate("Form", "UDP"))
        item = self.panelList.item(4)
        item.setText(_translate("Form", "TCP"))
        item = self.panelList.item(5)
        item.setText(_translate("Form", "Receiver"))
        self.panelList.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "目标MAC"))
        self.targetMacLine.setText(_translate("Form", "FF:FF:FF:FF:FF:FF"))
        self.label_2.setText(_translate("Form", "载荷        "))
        self.payloadMacLine.setText(_translate("Form", "networkDesign"))
        self.label_3.setText(_translate("Form", "发送次数 "))
        self.timesMacLine.setText(_translate("Form", "5"))
        self.sendMacBtn.setText(_translate("Form", "发送"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Form", "发送MAC帧"))
        self.label_4.setText(_translate("Form", "捕获次数"))
        self.sniffTimesMacLine.setText(_translate("Form", "10"))
        self.sniffStartMacBtn.setText(_translate("Form", "开始"))
        self.sniffStopMacBtn.setText(_translate("Form", "停止"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "接收MAC帧"))
        self.label_17.setText(_translate("Form", "操作类型"))
        self.opArpCombo.setItemText(0, _translate("Form", "who-has"))
        self.opArpCombo.setItemText(1, _translate("Form", "is-at"))
        self.label_18.setText(_translate("Form", "发送方MAC"))
        self.hwSrcArpLine.setPlaceholderText(_translate("Form", "不填默认本机网卡"))
        self.label_19.setText(_translate("Form", "发送方IP     "))
        self.ipSrcArpLine.setPlaceholderText(_translate("Form", "不填默认本机网卡"))
        self.label_20.setText(_translate("Form", "接收方MAC"))
        self.hwDstArpLine.setText(_translate("Form", "ff:ff:ff:ff:ff:ff"))
        self.label_15.setText(_translate("Form", "接收方IP     "))
        self.ipDstArpLine.setText(_translate("Form", "10.5.133.242/21"))
        self.sendArpBtn.setText(_translate("Form", "发送"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("Form", "发送并接受ARP报文"))
        self.label_22.setText(_translate("Form", "发送方IP"))
        self.ipSrcIpLine.setPlaceholderText(_translate("Form", "不填默认本机网卡"))
        self.label_23.setText(_translate("Form", "接收方IP"))
        self.label_24.setText(_translate("Form", "载荷       "))
        self.sendIpBtn.setText(_translate("Form", "发送"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("Form", "发送IP报"))
        self.label_25.setText(_translate("Form", "目标IP   "))
        self.sniffDstIpLine.setText(_translate("Form", "10.5.133.242"))
        self.label_26.setText(_translate("Form", "捕获次数"))
        self.sniffTimesIpLine.setText(_translate("Form", "10"))
        self.sniffStartIpBtn.setText(_translate("Form", "开始"))
        self.sniffStopIpBtn.setText(_translate("Form", "停止"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), _translate("Form", "接收IP报"))
        self.label_27.setText(_translate("Form", "发送方IP"))
        self.ipSrcUdpLine.setPlaceholderText(_translate("Form", "不填默认本机网卡"))
        self.label_5.setText(_translate("Form", "端口"))
        self.portSrcUdpLine.setText(_translate("Form", "8080"))
        self.label_28.setText(_translate("Form", "接收方IP"))
        self.ipDstUdpLine.setText(_translate("Form", "10.5.133.127"))
        self.label_6.setText(_translate("Form", "端口"))
        self.portDstUdpLine.setText(_translate("Form", "8000"))
        self.sendUdpBtn.setText(_translate("Form", "发送"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_13), _translate("Form", "发送UDP报"))
        self.label_30.setText(_translate("Form", "目标IP   "))
        self.sniffIpDstUdpLine.setText(_translate("Form", "10.5.133.242"))
        self.label_32.setText(_translate("Form", "目标端口"))
        self.sniffPortDstUdpLine.setText(_translate("Form", "8000"))
        self.label_31.setText(_translate("Form", "捕获次数"))
        self.sniffTimesUdpLine.setText(_translate("Form", "10"))
        self.sniffStartUdpBtn.setText(_translate("Form", "开始"))
        self.sniffStopUdpBtn.setText(_translate("Form", "停止"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_14), _translate("Form", "接收UDP报"))
        self.label_33.setText(_translate("Form", "发送方IP"))
        self.ipSrcTcpLine.setPlaceholderText(_translate("Form", "不填默认本机网卡"))
        self.label_7.setText(_translate("Form", "端口"))
        self.portSrcTcpLine.setText(_translate("Form", "8080"))
        self.label_34.setText(_translate("Form", "接收方IP"))
        self.ipDstTcpLine.setText(_translate("Form", "10.5.133.127"))
        self.label_8.setText(_translate("Form", "端口"))
        self.portDstTcpLine.setText(_translate("Form", "8000"))
        self.sendTcpBtn.setText(_translate("Form", "发送"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_15), _translate("Form", "发送TCP报"))
        self.label_36.setText(_translate("Form", "目标IP   "))
        self.sniffIpDstTcpLine.setText(_translate("Form", "10.5.133.242"))
        self.label_37.setText(_translate("Form", "目标端口"))
        self.sniffPortDstTcpLine.setText(_translate("Form", "8000"))
        self.label_38.setText(_translate("Form", "捕获次数"))
        self.sniffTimesTcpLine.setText(_translate("Form", "10"))
        self.sniffStartTcpBtn.setText(_translate("Form", "开始"))
        self.sniffStopTcpBtn.setText(_translate("Form", "停止"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_16), _translate("Form", "接收TCP报"))
        self.startReceiveBtn.setText(_translate("Form", "开始"))
        self.stopReceiveBtn.setText(_translate("Form", "停止"))
        self.clearTerminalBtn.setText(_translate("Form", "清空terminal"))