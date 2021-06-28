import functools
import operator
import sys
from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter
from PyQt5.QtCore import Qt


class Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.text = None

        self.initUI()

    def initUI(self):
        # x and y coordinates on the screen, width, height
        self.setGeometry(100, 100, 1030, 800)

        self.setWindowTitle("Writer")

    def initToolbar(self):
        self.newAction = QtWidgets.QAction(QtGui.QIcon("icons/new.png"), "New", self)
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon("icons/open.png"), "Open file", self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtWidgets.QAction(QtGui.QIcon("icons/safe.png"), "Save", self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.printAction = QtWidgets.QAction(QtGui.QIcon("icons/druck.png"), "Print document", self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.print)

        self.cutAction = QtWidgets.QAction(QtGui.QIcon("icons/scheere.png"),"Cut to clipboard",self)
        self.cutAction.setStatusTip("Delete and copy text to clipboard")
        self.cutAction.setShortcut("Ctrl+x")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtWidgets.QAction(QtGui.QIcon("icons/copy.png"), "Copy to clipboard", self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtWidgets.QAction(QtGui.QIcon("icons/paste.png"), "Paste from clipboard", self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtWidgets.QAction(QtGui.QIcon("icons/undo.png"), "Undo last action", self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtWidgets.QAction(QtGui.QIcon("icons/open.svg"), "Redo last undone thing", self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)
        self.toolbar.addAction(self.cutAction)

        self.toolbar.addSeparator()

        # Makes the next toolbar appear underneath this one
        self.addToolBarBreak()

    def initFormatbar(self):
        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):
        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)

        file.addAction(self.printAction)


        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)

    def initUI(self):
        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)

        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # x and y coordinates on the screen, width, height
        self.setGeometry(100, 100, 1030, 800)

        self.setWindowTitle("Writer")

    def print(self):
        dialog = QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.text.document().print_(dialog.printer())
    def new(self):

        spawn = Main(self)
        spawn.show()

    def open(self):
        # Get filename and show only .txt files
        self.filename = str(QtWidgets.QFileDialog.getOpenFileName(self, 'Open File'))
        self.x = self.filename.split(',')
        filename = self.x[0]
        filename = filename.replace('(', '')
        filename = filename.replace('\'', '')
        filename = filename.strip(" ")

        if filename is not None:
            with open(filename,"rt") as file:
                text = file.read()
                self.text.setText(text)

    def save(self):

        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = str(QtWidgets.QFileDialog.getSaveFileName(self, 'Save File'))
            self.x = self.filename.split(',')
            self.filename = self.x[0]
            self.filename = self.filename.replace('(', '')
            self.filename = self.filename.replace('\'', '')
            self.filename = self.filename.strip(" ")
            print(self.filename + "test")

        # Append extension if not there yet
        if not self.filename.endswith(".txt"):
            print(self.filename + "2")
            self.filename += ".txt"


        self.filename = self.filename.split(',')[0]
        self.filename = self.filename.replace('(', '')
        self.filename = self.filename.replace('\'', '')
        self.filename.strip(' ')

        with open(self.filename, "wt") as file:
            self.s = self.text.toPlainText()
            print(self.s + " tess1")
            file.write(self.s)



    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.filename = ""

        self.initUI()

    def convertTuple(tup):
        str = functools.reduce(operator.add, (tup))
        return str

def main():
    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
