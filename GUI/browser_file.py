# importing required libraries
import time
import statistics
from statistics import mode
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys
# import login.emailid
# from __main__ import *
from login import *
# from collections import Counter
list_url = []
global userEmail
# def CountFrequency(my_list):
#     # Creating an empty dictionary
# 		freq = {}
# 		for item in list_url:
# 			if (item in freq):
# 				freq[item] += 1
# 			else:
# 				freq[item] = 1
# 		for key,value in freq.items():
# 			if value == 5:
#
# 				self.add_new_tab(QUrl(f'{key}'), 'favourite')
def user_values(emailid):
		userEmail = emailid
		# print(userEmail)
class Browser(QMainWindow):
	# constructor
	def __init__(self ):
		super(Browser, self).__init__()
		# print(userEmail)
		# print("message from first window" +message)
		# self.setMouseTracking(True)
		self.setWindowIcon(QtGui.QIcon('pic_3.png'))
		# self.showMaximized()
		# mouse_move()
		# creating a tab widget
		self.tabs = QTabWidget()

		# making document mode true
		self.tabs.setDocumentMode(True)

		# adding action when clicked
		self.tabs.tabBarClicked.connect(self.tab_open_click)

		# adding action when tab is changed
		self.tabs.currentChanged.connect(self.current_tab_changed)

		# making tabs closeable
		self.tabs.setTabsClosable(True)

		# adding action when tab close is requested
		self.tabs.tabCloseRequested.connect(self.close_current_tab)

		# making tabs as central widget
		self.setCentralWidget(self.tabs)

		# creating a status bar
		self.status = QStatusBar()

		# setting status bar to the main window
		self.setStatusBar(self.status)

		# creating a tool bar for navigation
		navtb = QToolBar("Navigation")

		# adding tool bar to the main window
		self.addToolBar(navtb)
		# r = 'Capture.png'
		# creating back action
		back_btn = QAction("Backward", self)
		back_btn.setIcon(QtGui.QIcon('left.png'))
		# setting status tip
		back_btn.setStatusTip("Back to previous page")

		# adding action to back button
		# making current tab to go back
		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

		# adding this to the navigation tool bar
		navtb.addAction(back_btn)

		# similarly adding next button

		next_btn = QAction("Forward", self)
		next_btn.setIcon(QtGui.QIcon('right.png'))
		next_btn.setStatusTip("Forward to next page")
		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		navtb.addAction(next_btn)

		# similarly adding reload button
		reload_btn = QAction("Reload", self)
		reload_btn.setIcon(QtGui.QIcon('refresh.png'))
		reload_btn.setStatusTip("Reload page")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		navtb.addAction(reload_btn)

		# creating home action
		home_btn = QAction("Home", self)
		home_btn.setIcon(QtGui.QIcon('Home.png'))
		home_btn.setStatusTip("Go home")

		# adding action to home button
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)

		# adding a separator
		navtb.addSeparator()

		# creating a line edit widget for URL
		self.urlbar = QLineEdit()

		# adding action to line edit when return key is pressed
		self.urlbar.returnPressed.connect(self.navigate_to_url)

		# adding line edit to tool bar
		navtb.addWidget(self.urlbar)
		most_freq =  None
		if len(list_url) != 0:
			most_freq=(mode(list_url))

		# similarly adding stop action
		stop_btn = QAction("Stop", self)
		stop_btn.setIcon(QtGui.QIcon('cross_.png'))
		stop_btn.setStatusTip("Stop loading current page")
		stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
		navtb.addAction(stop_btn)
		# creating first tab
		# self.add_new_tab(QUrl('https://www.youtube.com'), 'youtube')
		# self.add_new_tab(QUrl('https://www.gmail.com'), 'gmail')
		self.add_new_tab(QUrl('https://www.duckduckgo.com'), 'Homepage')
		if most_freq is None:
			print("New user detected")
		else:
			self.add_new_tab(QUrl(f'{most_freq}'), 'Most Frequent')

		self.show()

		# setting window title
		self.setWindowTitle("Chanakya Browser")

	# method for adding new tab
	def add_new_tab(self, qurl = None, label ="Blank"):

		# if url is blank
		if qurl is None:
			# creating a duckduckgo url
			qurl = QUrl('https://www.duckduckgo.com')

		# creating a QWebEngineView object
		browser = QWebEngineView()

		# setting url to browser
		browser.setUrl(qurl)

		# setting tab index
		i = self.tabs.addTab(browser, label)
		self.tabs.setCurrentIndex(i)

		# adding action to the browser when url is changed
		# update the url
		browser.urlChanged.connect(lambda qurl, browser = browser:
								self.update_urlbar(qurl, browser))

		# adding action to the browser when loading is finished
		# set the tab title
		browser.loadFinished.connect(lambda _, i = i, browser = browser:
									self.tabs.setTabText(i, browser.page().title()))

	# when double clicked is pressed on tabs
	def tab_open_click(self, i):

		# checking index i.e
		# No tab under the click
		if i == -1:
			# creating a new tab
			self.add_new_tab()

	# wen tab is changed
	def current_tab_changed(self, i):

		# get the curl
		qurl = self.tabs.currentWidget().url()

		# update the url
		self.update_urlbar(qurl, self.tabs.currentWidget())

		# update the title
		self.update_title(self.tabs.currentWidget())

	# when tab is closed
	def close_current_tab(self, i):

		# if there is only one tab
		if self.tabs.count() < 2:
			# do nothing
			return

		# else remove the tab
		self.tabs.removeTab(i)

	# method for updating the title
	def update_title(self, browser):

		# if signal is not from the current tab
		if browser != self.tabs.currentWidget():
			# do nothing
			return

		# get the page title
		title = self.tabs.currentWidget().page().title()

		# set the window title
		self.setWindowTitle("% s - Chanakya Browser" % title)

	# action to go to home
	def navigate_home(self):

		# go to duckduckgo
		self.tabs.currentWidget().setUrl(QUrl("https://www.duckduckgo.com"))

	# method for navigate to url
	def navigate_to_url(self):

		# get the line edit text
		# convert it to QUrl object
		q = QUrl(self.urlbar.text())
		# if scheme is blank
		if q.scheme() == "":
			# set scheme
			q.setScheme("https")

		# set the url
		self.tabs.currentWidget().setUrl(q)

	# method to update the url
	def update_urlbar(self, q, browser = None):

		# If this signal is not from the current tab, ignore
		if browser != self.tabs.currentWidget():

			return

		# set text to the url bar
		self.urlbar.setText(q.toString())
		list_url.append(self.urlbar.text())

# creating a PyQt5 application

app = QApplication(sys.argv)
# setting name to the application
app.setApplicationName("Automated Web Browser")
app.setStyle("Fusion")
dark_palette = QPalette()

dark_palette.setColor(QPalette.Window, QColor(46, 47, 48))
dark_palette.setColor(QPalette.WindowText, QColor(208, 208, 208))
dark_palette.setColor(QPalette.Light, QColor(255, 255, 255))
dark_palette.setColor(QPalette.Midlight, QColor(227, 227, 227))
dark_palette.setColor(QPalette.Dark, QColor(64, 66, 68))
dark_palette.setColor(QPalette.Mid, QColor(160, 160, 160))
dark_palette.setColor(QPalette.Text, QColor(208, 208, 208))
dark_palette.setColor(QPalette.BrightText, QColor(255, 51, 51))
dark_palette.setColor(QPalette.Button, QColor(64, 66, 68))
dark_palette.setColor(QPalette.ButtonText, QColor(208, 208, 208))
dark_palette.setColor(QPalette.Base, QColor(46, 47, 48))
dark_palette.setColor(QPalette.Shadow, QColor(105, 105, 105))
dark_palette.setColor(QPalette.Highlight, QColor(0, 0, 0, 102))
dark_palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
dark_palette.setColor(QPalette.Link, QColor(0, 122, 244))
dark_palette.setColor(QPalette.LinkVisited, QColor(165, 122, 255))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 54, 55))
dark_palette.setColor(QPalette.NoRole, QColor(0, 0, 0))
dark_palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0, 102))
dark_palette.setColor(QPalette.ToolTipText, QColor(208, 208, 208))
dark_palette.setColor(QPalette.Disabled, QPalette.Window, QColor(68, 68, 68, 255))
dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(164, 166, 168, 96))
dark_palette.setColor(QPalette.Disabled, QPalette.Text, QColor(164, 166, 168, 96))
dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(164, 166, 168, 96))
dark_palette.setColor(QPalette.Disabled, QPalette.Base, QColor(68, 68, 68, 255))
dark_palette.setColor(QPalette.Disabled, QPalette.Shadow, QColor(0, 0, 0, 255))

app.setPalette(dark_palette)
app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

# creating MainWindow object
window = Browser()
# loop
app.exec_()
print(list_url)
print("Most Viewed")
# print(emailid)
print((mode(list_url)))
