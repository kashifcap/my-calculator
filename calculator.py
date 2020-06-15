from tkinter import *


class Calculator:
    def __init__(self, root):
        self.bracket_count = 0
        self.func_list = ['+','*','/','-','%']
        self.root = root
        self.main_var = StringVar()
        self.entry_box = Entry(self.root, justify = RIGHT, textvariable = self.main_var)
        self.number_button_0 = Button(self.root, text = '0', height = 3, width = 5,
         command = lambda : self.textfunc('0'))
        self.number_button_1 = Button(self.root, text = '1', height = 3, width = 5,
         command = lambda : self.textfunc('1'))
        self.number_button_2 = Button(self.root, text = '2', height = 3, width = 5,
         command = lambda : self.textfunc('2'))
        self.number_button_3 = Button(self.root, text = '3', height = 3, width = 5,
         command = lambda : self.textfunc('3'))
        self.number_button_4 = Button(self.root, text = '4', height = 3, width = 5,
         command = lambda : self.textfunc('4'))
        self.number_button_5 = Button(self.root, text = '5', height = 3, width = 5,
         command = lambda : self.textfunc('5'))
        self.number_button_6 = Button(self.root, text = '6', height = 3, width = 5,
         command = lambda : self.textfunc('6'))
        self.number_button_7 = Button(self.root, text = '7', height = 3, width = 5,
         command = lambda : self.textfunc('7'))
        self.number_button_8 = Button(self.root, text = '8', height = 3, width = 5,
         command = lambda : self.textfunc('8'))
        self.number_button_9 = Button(self.root, text = '9', height = 3, width = 5,
         command = lambda : self.textfunc('9'))
        self.multiply_button = Button(self.root, text = '*', height = 3, width = 5,
         command = lambda : self.textfunc('*'))
        self.divide_button = Button(self.root, text = '/', height = 3, width = 5,
         command = lambda : self.textfunc('/'))
        self.add_button = Button(self.root, text = '+', height = 3, width = 5,
         command = lambda : self.textfunc('+'))
        self.subtract_button = Button(self.root, text = '-', height = 3, width = 5,
         command = lambda : self.textfunc('-'))
        self.decimal_button = Button(self.root, text = '.', height = 3, width = 5,
         command = lambda : self.textfunc('.'))
        self.total_button = Button(self.root, text = '=', height = 3, width = 5,
         command = lambda : self.totalfunc())
        self.clear_all_button = Button(self.root, text = 'C', height = 3, width = 5,
         command = lambda : self.clearallfunc())
        self.brackets_button = Button(self.root, text = '()', height = 3, width = 5,
         command = lambda : self.bracketfunc())
        self.remainder_button = Button(self.root, text = '%', height = 3, width = 5,
         command = lambda : self.textfunc('%'))
        self.clear_last_button = Button(self.root, text = 'CE', height = 3, width = 5,
         command = lambda : self.clearlastfunc())

        self.entry_box.grid(row = 0, column = 0, columnspan = 4, pady = (10,5), padx = 5, ipady = 10, sticky = 'ew')
        self.number_button_0.grid(row = 5, column = 1)
        self.number_button_1.grid(row = 4, column = 0)
        self.number_button_2.grid(row = 4, column = 1)
        self.number_button_3.grid(row = 4, column = 2)
        self.number_button_4.grid(row = 3, column = 0)
        self.number_button_5.grid(row = 3, column = 1)
        self.number_button_6.grid(row = 3, column = 2)
        self.number_button_7.grid(row = 2, column = 0)
        self.number_button_8.grid(row = 2, column = 1)
        self.number_button_9.grid(row = 2, column = 2)
        self.multiply_button.grid(row = 2, column = 3)
        self.divide_button.grid(row = 3, column = 3)
        self.add_button.grid(row = 4, column = 3)
        self.subtract_button.grid(row = 5, column = 3)
        self.decimal_button.grid(row = 5, column = 0)
        self.total_button.grid(row = 5, column = 2)
        self.clear_all_button.grid(row = 1, column = 0)
        self.clear_last_button.grid(row = 1, column = 2)
        self.remainder_button.grid(row = 1, column = 3)
        self.brackets_button.grid(row = 1, column = 1)

    
    def textfunc(self, txt):
        self.main_var.set(self.main_var.get() + txt)

        
    def clearallfunc(self):
        self.main_var.set('')


    def clearlastfunc(self):
        self.main_var.set(self.main_var.get()[0:-1])

    
    def bracketfunc(self):
        if self.bracket_count == 0 or self.main_var.get()[-1] in self.func_list:
            self.main_var.set(self.main_var.get() + '(')
            self.bracket_count +=1
        else:
            self.main_var.set(self.main_var.get() + ')')
            self.bracket_count -=1


    def totalfunc(self):
        try:
            self.main_var.set(eval(self.main_var.get()))
        except:
            self.main_var.set("INVALID INPUT")
        


if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    Calculator(root)
    root.mainloop()