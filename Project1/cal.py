from tkinter import *
import tkinter.font
from functools import partial

class Cal:
    def get_input(entry, argu):
        entry.insert(END, argu)

    def back(entry):
        input_len = len(entry.get())
        entry.delete(input_len - 1)

    def clear(entry):
        entry.delete(0, END)

    def calculate(entry):
        input = entry.get()
        try:
            output = str(eval(input.strip()))
        except ZeroDivisionError:
            output = '除0错误'
        Cal.clear(entry)
        entry.insert(END, output)

def pad():
    # 主窗体
    root = Tk()
    root.title("Cal")
    root.minsize(240, 306)
    root.resizable(0, 0)
    # 显示部分
    show_font = tkinter.font.Font(size=34)
    show = Entry(root, bg='#323232', justify="right", font=show_font)
    show.place(x=0, y=0, width=240, heigh=54)
    # 按钮部分
    button_font = tkinter.font.Font(size=20, weight=tkinter.font.NORMAL)
    myButton = partial(Button, root, font=button_font)
    button_clear = myButton(text='AC', command=lambda: Cal.clear(show))
    button_clear.place(x=0, y=54, width=120, heigh=50)
    button_back = myButton(text='←', command=lambda: Cal.back(show))
    button_back.place(x=120, y=54, width=60, heigh=50)
    button_divide = myButton(text='÷', command=lambda: Cal.get_input(show, '/'))
    button_divide.place(x=180, y=54, width=60, heigh=50)
    button7 = myButton(text='7', command=lambda: Cal.get_input(show, '7'))
    button7.place(x=0, y=104, width=60, heigh=50)
    button8 = myButton(text='8', command=lambda: Cal.get_input(show, '8'))
    button8.place(x=60, y=104, width=60, heigh=50)
    button9 = myButton(text='9', command=lambda: Cal.get_input(show, '9'))
    button9.place(x=120, y=104, width=60, heigh=50)
    button_multiply = myButton(text='×', command=lambda: Cal.get_input(show, '*'))
    button_multiply.place(x=180, y=104, width=60, heigh=50)
    button4 = myButton(text='4', command=lambda: Cal.get_input(show, '4'))
    button4.place(x=0, y=154, width=60, heigh=50)
    button5 = myButton(text='5', command=lambda: Cal.get_input(show, '5'))
    button5.place(x=60, y=154, width=60, heigh=50)
    button6 = myButton(text='6', command=lambda: Cal.get_input(show, '6'))
    button6.place(x=120, y=154, width=60, heigh=50)
    button_subtract = myButton(text='-', command=lambda: Cal.get_input(show, '-'))
    button_subtract.place(x=180, y=154, width=60, heigh=50)
    button1 = myButton(text='1', command=lambda: Cal.get_input(show, '1'))
    button1.place(x=0, y=204, width=60, heigh=50)
    button2 = myButton(text='2', command=lambda: Cal.get_input(show, '2'))
    button2.place(x=60, y=204, width=60, heigh=50)
    button3 = myButton(text='3', command=lambda: Cal.get_input(show, '3'))
    button3.place(x=120, y=204, width=60, heigh=50)
    button_add = myButton(text='+', command=lambda: Cal.get_input(show, '+'))
    button_add.place(x=180, y=204, width=60, heigh=50)
    button0 = myButton(text='0', command=lambda: Cal.get_input(show, '0'))
    button0.place(x=0, y=254, width=120, heigh=50)
    button_point = myButton(text='.', command=lambda: Cal.get_input(show, '.'))
    button_point.place(x=120, y=254, width=60, heigh=50)
    button_equal = myButton(text='=', command=lambda: Cal.calculate(show))
    button_equal.place(x=180, y=254, width=60, heigh=50)
    root.mainloop()

if __name__=="__main__":
    pad()
