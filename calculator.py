from tkinter import *


class Calculator:
    def __init__(self, root):
        self.entry_box = Entry(root)
        self.number_button_0 = Button(root, text = '0', padx = 40, pady = 40)
        self.number_button_1 = Button(root, text = '1', padx = 40, pady = 40)
        self.number_button_2 = Button(root, text = '2', padx = 40, pady = 40)
        self.number_button_3 = Button(root, text = '3', padx = 40, pady = 40)
        self.number_button_4 = Button(root, text = '4', padx = 40, pady = 40)
        self.number_button_5 = Button(root, text = '5', padx = 40, pady = 40)
        self.number_button_6 = Button(root, text = '6', padx = 40, pady = 40)
        self.number_button_7 = Button(root, text = '7', padx = 40, pady = 40)
        self.number_button_8 = Button(root, text = '8', padx = 40, pady = 40)
        self.number_button_9 = Button(root, text = '9', padx = 40, pady = 40)

        self.entry_box.grid(row = 0, column = 0, columnspan = 3, pady = (10,5), ipadx = 50, ipady = 10)
        self.number_button_0.grid(row = 4, column = 0, columnspan = 3)
        self.number_button_1.grid(row = 3, column = 0)
        self.number_button_2.grid(row = 3, column = 1)
        self.number_button_3.grid(row = 3, column = 2)
        self.number_button_4.grid(row = 2, column = 0)
        self.number_button_5.grid(row = 2, column = 1)
        self.number_button_6.grid(row = 2, column = 2)
        self.number_button_7.grid(row = 1, column = 0)
        self.number_button_8.grid(row = 1, column = 1)
        self.number_button_9.grid(row = 1, column = 2)

        


if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    Calculator(root)
    root.mainloop()