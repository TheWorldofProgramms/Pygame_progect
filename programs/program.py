import pygame, PyQt5, sys

from main_snake import GameSnake
from main_window import Ui_MainWindow
from arrow_game import ArrowGame
from help import Ui_HelpWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

pygame.init()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):                 #Главное окно и выбор игры
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.snake)

        self.pushButton_3.clicked.connect(self.arrow)

        self.pushButton_4.clicked.connect(self.help)

    def snake(self):
        snake = GameSnake()
        snake.main()

    def arrow(self):
        arrow = ArrowGame()
        arrow.main()

    def help(self):
        self.help = HelpWindow()
        self.help.show()


class HelpWindow(QWidget, Ui_HelpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.a = 0



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

pygame.quit()