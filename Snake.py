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

    def move(self):
        """ Двигает змейку в заданном направлении """
        # перебираем все сегменты кроме первого
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            # задаем каждому сегменту позицию сегмента стоящего после него
            c.coords(segment, x1, y1, x2, y2)

        # получаем координаты сегмента перед "головой"
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)

        # помещаем "голову" в направлении указанном в векторе движения
        c.coords(self.segments[-1].instance,
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)



root = Tk()
root.title("PythonicWay Snake")

# создаем экземпляр класса Canvas (его мы еще будем использовать) и заливаем все зеленым цветом
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#330000")
c.grid()
# Наводим фокус на Canvas, чтобы мы могли ловить нажатия клавиш
c.focus_set()



# Запускаем окно
root.mainloop()
