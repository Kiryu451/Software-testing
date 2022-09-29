from tkinter import *
import math


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=10, y=50)

        btns = [
            "C", "DEL", "X^2", "√",
            "1", "2", "3", "/",
            "4", "5", "6", "*",
            "7", "8", "9", "-",
            "(", "0", ")", "+",
            "log", "sin", "cos", "="
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "√":
            self.formula = str((eval(self.formula))**0.5)
        elif operation == "log":
            self.formula = str(math.log(eval(self.formula)))
        elif operation == "sin":
            self.formula = str(math.sin(eval(self.formula)))
        elif operation == "cos":
            self.formula = str(math.cos(eval(self.formula)))
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x630+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    root.mainloop()