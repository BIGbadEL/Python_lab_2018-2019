#!/usr/bin/env python3

import sys, os
from string import *
from tkinter import *
from PIL import Image
from math import *
from time import *
from random import *
# from Canvas import *
from scipy.integrate import quad
from scipy.optimize import leastsq
from scipy.optimize import bisect
import numpy as np
import matplotlib.pyplot as plt


def onclick1():
    pole.insert(END, "1")


def onclick2():
    pole.insert(END, "2")


def onclick3():
    pole.insert(END, "3")


def onclick4():
    pole.insert(END, "4")


def onclick5():
    pole.insert(END, "5")


def onclick6():
    pole.insert(END, "6")


def onclick7():
    pole.insert(END, "7")


def onclick8():
    pole.insert(END, "8")


def onclick9():
    pole.insert(END, "9")


def onclickpl():
    pole.insert(END, "+")


def onclickmin():
    pole.insert(END, "-")


def onclickmult():
    pole.insert(END, "*")


def onclickdiv():
    pole.insert(END, "/")


def onclickmod():
    pole.insert(END, "%")


def onclickpot():
    pole.insert(END, "**")


def onclicklnawias():
    pole.insert(END, "(")


def onclickrnawias():
    pole.insert(END, ")")


def onclickrow():
    wart = eval(pole.get())
    pole.delete(0, END)
    pole.insert(0, str(wart))


def onclickcal():
    fun = lambda x: eval(pole.get())
    wart = quad(fun, float(stop_pole.get()), float(start_pole.get()))
    pole.delete(0, END)
    pole.insert(0, str(wart))


def onclickfindzero():
    fun = lambda x: eval(pole.get())
    try:
        wart = bisect(fun, float(stop_pole.get()), float(start_pole.get()))
    except ValueError:
        wart = "Brak miejsca zerowego"
    pole.delete(0, END)
    pole.insert(0, str(wart))


def onclickfit():
    global foto

    plt.savefig('wykr.png', dpi = 50)

    x, y = np.loadtxt(pole.get(), unpack = True)
    funcLine = lambda tpl, x: tpl[0] * x + tpl[1]
    funcQuad = lambda tpl, x: tpl[0] * x ** 2 + tpl[1] * x + tpl[2]
    ErrorFunc = lambda tpl, x, y: funcLine(tpl, x) - y

    plt.plot(x, y)

    tplFinal1, success = leastsq(ErrorFunc, (x[0], y[0]), args = (x, y))
    x = np.linspace(x[0], x[-1])
    plt.plot(x, funcLine(tplFinal1, x))
    try:
        Image.open('wykr.png').save('wykr.gif')
        foto = PhotoImage(file = "wykr.gif")
        cv.create_image(0, 0, anchor = NW, image = foto)
    except:
        pass


def onclickRysuj():
    global foto

    plt.savefig('wykr.png', dpi = 50)

    start = float(start_pole.get())
    stop = float(stop_pole.get())
    x = np.linspace(start, stop, 1000)
    fun = lambda x: eval(pole.get())
    plt.plot(x, fun(x))

    try:
        Image.open('wykr.png').save('wykr.gif')
        foto = PhotoImage(file = "wykr.gif")
        cv.create_image(0, 0, anchor = NW, image = foto)
    except:
        pass


def cl():
    plt.clf()
    pole.delete(0, END)
    cv.delete('all')


def exit():
    plt.close()
    okno.destroy()


okno = Tk()
import tkinter.font

calcfont = tkinter.font.Font(font = ("Courier", 10, "bold"))
ebg = '#000033'
gadbg = "#ffffff"
pole = Entry(okno)
pole.config(width = 60, fg = "white", bg = ebg, font = calcfont)
pole.grid(row = 1, column = 0, columnspan = 5, pady = 10)

start_pole = Entry(okno)
start_pole.config(width = 20, fg = "white", bg = ebg, font = calcfont)
start_pole.grid(row = 1, column = 5, columnspan = 1, pady = 10)

stop_pole = Entry(okno)
stop_pole.config(width = 20, fg = "white", bg = ebg, font = calcfont)
stop_pole.grid(row = 1, column = 6, columnspan = 1, pady = 10)

button = Button(okno, text = '1', command = onclick1, bg = gadbg, font = calcfont)
button.grid(row = 2, column = 0, sticky = EW)
button = Button(okno, text = '2', command = onclick2, bg = gadbg, font = calcfont)
button.grid(row = 2, column = 1, sticky = EW)
button = Button(okno, text = '3', command = onclick3, bg = gadbg, font = calcfont)
button.grid(row = 2, column = 2, sticky = EW)

button = Button(okno, text = '4', command = onclick4, bg = gadbg, font = calcfont)
button.grid(row = 3, column = 0, sticky = EW)
button = Button(okno, text = '5', command = onclick5, bg = gadbg, font = calcfont)
button.grid(row = 3, column = 1, sticky = EW)
button = Button(okno, text = '6', command = onclick6, bg = gadbg, font = calcfont)
button.grid(row = 3, column = 2, sticky = EW)

button = Button(okno, text = '7', command = onclick7, bg = gadbg, font = calcfont)
button.grid(row = 4, column = 0, sticky = EW)
button = Button(okno, text = '8', command = onclick8, bg = gadbg, font = calcfont)
button.grid(row = 4, column = 1, sticky = EW)
button = Button(okno, text = '9', command = onclick9, bg = gadbg, font = calcfont)
button.grid(row = 4, column = 2, sticky = EW)

button = Button(okno, text = '+', command = onclickpl, bg = gadbg, font = calcfont)
button.grid(row = 2, column = 4, sticky = EW)
button = Button(okno, text = '-', command = onclickmin, bg = gadbg, font = calcfont)
button.grid(row = 2, column = 5, sticky = EW)
button = Button(okno, text = '=', command = onclickrow, bg = gadbg, font = calcfont)
button.grid(row = 2, column = 6, sticky = EW)

button = Button(okno, text = '*', command = onclickmult, bg = gadbg, font = calcfont)
button.grid(row = 3, column = 4, sticky = EW)
button = Button(okno, text = '/', command = onclickdiv, bg = gadbg, font = calcfont)
button.grid(row = 3, column = 5, sticky = EW)
button = Button(okno, text = '%', command = onclickmod, bg = gadbg, font = calcfont)
button.grid(row = 3, column = 6, sticky = EW)

button = Button(okno, text = '**', command = onclickpot, bg = gadbg, font = calcfont)
button.grid(row = 4, column = 4, sticky = EW)
button = Button(okno, text = '(', command = onclicklnawias, bg = gadbg, font = calcfont)
button.grid(row = 4, column = 5, sticky = EW)
button = Button(okno, text = ')', command = onclickrnawias, bg = gadbg, font = calcfont)
button.grid(row = 4, column = 6, sticky = EW)

w = Label(okno, text = "label")
w.grid(row = 5, column = 0)

button = Button(okno, text = 'Rysuj', command = onclickRysuj, bg = gadbg, font = calcfont)
button.grid(row = 6, column = 2, sticky = EW)

button = Button(okno, text = 'exit', command = exit, bg = gadbg, font = calcfont)
button.grid(row = 5, column = 5, sticky = EW)
button = Button(okno, text = 'clear', command = cl, bg = gadbg, font = calcfont)
button.grid(row = 5, column = 4, sticky = EW)
button = Button(okno, text = 'integral', command = onclickcal, bg = gadbg, font = calcfont)
button.grid(row = 5, column = 6, sticky = EW)

button = Button(okno, text = 'find zero', command = onclickfindzero, bg = gadbg, font = calcfont)
button.grid(row = 6, column = 4, sticky = EW)

button = Button(okno, text = 'fit form file', command = onclickfit, bg = gadbg, font = calcfont)
button.grid(row = 6, column = 5, sticky = EW)

cv = Canvas(okno, width = 400, height = 300)
cv["background"] = "white"
cv["borderwidth"] = 0
cv.config()
cv.grid(row = 10, column = 0, columnspan = 9)

okno.title('Kalkulator')
okno.mainloop()
