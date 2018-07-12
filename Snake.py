from tkinter import *
import random

# Globals
# ширина экрана
WIDTH = 800
# высота экрана
HEIGHT = 600
# Размер сегмента змейки
SEG_SIZE = 20
# Переменная отвечающая за состояние игры
IN_GAME = True



#Сегмент змейки будет простым прямоугольником
#созданным при помощи метода create_rectangle
# класса Canvas модуля tkinter.
class Segment(object):
    """ Single snake segment """
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x+SEG_SIZE, y+SEG_SIZE,
                                           fill="white")

class Snake(object):
    """ Simple Snake class """
    def __init__(self, segments):
        self.segments = segments
        #  список доступных направлений движения змейки
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # изначально змейка двигается вправо
        self.vector = self.mapping["Right"]





root = Tk()
root.title("PythonicWay Snake")

# создаем экземпляр класса Canvas (его мы еще будем использовать) и заливаем все зеленым цветом
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#330000")
c.grid()
# Наводим фокус на Canvas, чтобы мы могли ловить нажатия клавиш
c.focus_set()



# Запускаем окно
root.mainloop()