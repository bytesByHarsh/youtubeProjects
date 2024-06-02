import sys
import subprocess

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFileDialog
from PyQt5.QtWidgets import QAction, QTreeWidget, QPushButton, QTreeWidgetItem, QMessageBox, QLabel
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5 import uic  # Import the uic module

from codeEditor import PythonCodeEditor


class PythonTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("ui/editor.ui", self)
        self.setWindowTitle("Python Text Editor in Python")

        ## Declare all the buttons and options data type
        ## Helps in writing the code bcz of autosuggestion

        self.codeLayout:QVBoxLayout
        self.runButton:QPushButton
        self.fileDirTreeWidget:QTreeWidget
        self.zoomInButton:QPushButton
        self.zoomOutButton:QPushButton
        self.fileNameLabel:QLabel

        self.actionOpen:QAction
        self.actionSave:QAction


        self.pythonCodeEditor: QWidget = PythonCodeEditor()
        self.codeLayout.addWidget(self.pythonCodeEditor)


        self.runButton.clicked.connect(self.runPythonCode)
        self.fileDirTreeWidget.itemDoubleClicked.connect(self.openSelectedFile)
        self.zoomInButton.clicked.connect(self.textZoomIn)
        self.zoomOutButton.clicked.connect(self.textZoomOut)

        ## Actions
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

        self.actionOpen.setShortcut("Ctrl+O")
        self.actionSave.setShortcut("Ctrl+S")


        self.show()

    def runPythonCode(self):
        print("Run Python Code")

        with open("temp.py", "w") as file:
            file.write(self.pythonCodeEditor.text())

        command = f"python temp.py"
        subprocess.Popen(["gnome-terminal", "--", "bash","-c",f"{command}; read -p 'Press Enter to exit...'"])
        print("Code Completed")


    def openSelectedFile(self, item, column):
        item = item.text(0)
        if item.endswith(".py"):
            with open(item, "r") as file:
                file_content = file.read()
                self.pythonCodeEditor.setPlainText(file_content)
                self.fileNameLabel.setText(item)

    def textZoomIn(self):
        self.pythonCodeEditor.textZoomIn()

    def textZoomOut(self):
        self.pythonCodeEditor.textZoomOut()

    def open_file(self):
        option = QFileDialog.Options()
        option |= QFileDialog.ReadOnly
        option |= QFileDialog.ExistingFiles


        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Python Files (*.py)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setOptions(option)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()

            for file_path in selected_files:
                with open(file_path, "r") as file:
                    file_content = file.read()
                    self.pythonCodeEditor.setPlainText(file_content)
                    self.fileNameLabel.setText(file_path)

                    ## Update in the tree as well
                    item = QTreeWidgetItem(self.fileDirTreeWidget, [file_path])
                    self.fileDirTreeWidget.addTopLevelItem(item)
                    return # Open single file for now




    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.ExistingFiles

        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Python Files (*.py)")
        file_dialog.setOptions(options)

        default_file_name = "TestCode.py"  # Default file name
        file_path, _ = file_dialog.getSaveFileName(self, "Save File", default_file_name, "Python Files (*.py)")

        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.pythonCodeEditor.text())
                self.fileNameLabel.setText(file_path)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        editor = PythonTextEditor()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("Got Keyboard Interrupt")
        exit(0)
