from PyQt5.QtGui import QTextCursor, QTextCharFormat, QSyntaxHighlighter, QFont
from PyQt5.QtWidgets import QPlainTextEdit, QTextEdit, QWidget, QVBoxLayout, QPushButton, QApplication
from PyQt5.QtCore import Qt, QRegExp


class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        self.highlighting_rules = []

        #Create rules to highlight different elements
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.blue)
        keyword_format.setFontWeight(QFont.Bold)
        keywords = ["False","None","True","and","as","assert","break",
                    "class","continue","def","del","elif","else","except",
                    "finally","for","from","global","if","import","in","is",
                    "lambda","nonlocal","not","or","pass","raise","return",
                    "try","while","with","yield"]  # Add more as needed
        for keyword in keywords:
            rule = (r'\b' + keyword + r'\b', keyword_format)
            self.highlighting_rules.append(rule)

        # Create a rule for strings (in double or single quotes)
        string_format = QTextCharFormat()
        string_format.setForeground(Qt.darkGreen)
        self.highlighting_rules.append((r'\".*\"', string_format))
        self.highlighting_rules.append((r'\'.*\'', string_format))
        self.highlighting_rules.append((r'#.*$', string_format))

        triple_double_quoted_format = QTextCharFormat()
        triple_double_quoted_format.setForeground(Qt.red)
        self.highlighting_rules.append((r'""".*?"""', triple_double_quoted_format))

    def highlightBlock(self, text) -> None:
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)

            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)


class PythonCodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.setTabStopWidth(20)
        self.setTabChangesFocus(False)

        self.highlighter = PythonSyntaxHighlighter(self.document())

        self.zoom_level = 5

    def text(self):
        return self.toPlainText()

    def textZoomIn(self):
        self.zoom_level *= 2
        self.zoom_level = min(self.zoom_level, 20)
        self.zoomIn(self.zoom_level)

    def textZoomOut(self):
        self.zoom_level /= 2
        self.zoom_level = max(self.zoom_level, 2)
        self.zoomOut(self.zoom_level)

if __name__ == "__main__":
    app = QApplication([])

    editor = PythonCodeEditor()
    editor.show()

    app.exec_()