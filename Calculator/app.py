from tkinter import *
import winsound

def retEval(event):
    userInput.set(eval(userInput.get()))

def click(event):
    try:
        symbol = event.widget.cget("text")
        if symbol == "=":
            result = eval(userInput.get())
            userInput.set(result)
        elif symbol == "C":
            userInput.set("")
        elif symbol == "←":
            userInput.set(userInput.get()[:-1])
        else:
            userInput.set(userInput.get() + symbol)
        root.update()
    except (SyntaxError, NameError, ValueError):
        pass
    

root = Tk()
root.title("Calculator")
root.config(bg="black", padx=10, pady=10)
root.resizable(0, 0)

symbols = [["C", "", "←", ""],
           ["7", "8", "9", "+"], 
           ["4", "5", "6", "-"], 
           ["1", "2", "3", "*"], 
           ["0", "00", ".", "/"], 
           ["=", "", "", "%"]]

userInput = StringVar()

calcWindow = Entry(textvariable=userInput, font=("Ds-Digital Bold Italic", 20), bg="green", relief="sunken")
calcWindow.pack(fill="x", padx=5, pady=5)
calcWindow.bind("<Return>", retEval)

keyFrame = Frame(root, bg="black")
keyFrame.pack()

for i in range(len(symbols)):
    for j in range(len(symbols[i])):
        if symbols[i][j] == "":
            continue

        if symbols[i][j] == "=":
            btn = Button(keyFrame, text=f"{symbols[i][j]}", width=10, height=2, font=("Arial", 12, "bold"), bg="#121212", fg="white", activebackground="#080808", activeforeground="white", relief="groove")
            btn.grid(row=i, column=0, padx=5, pady=5, sticky="ew", columnspan=3)
            btn.bind("<Button-1>", click)

        elif symbols[i][j] == "←":
            btn = Button(keyFrame, text=f"{symbols[i][j]}", width=10, height=2, font=("Arial", 12, "bold"), bg="#121212", fg="white", activebackground="#080808", activeforeground="white", relief="groove")
            btn.grid(row=i, column=2, padx=5, pady=5, sticky="ew", columnspan=2)
            btn.bind("<Button-1>", click)

        elif symbols[i][j] == "C":
            btn = Button(keyFrame, text=f"{symbols[i][j]}", width=10, height=2, font=("Arial", 12, "bold"), bg="#121212", fg="white", activebackground="#080808", activeforeground="white", relief="groove")
            btn.grid(row=i, column=0, padx=5, pady=5, sticky="ew", columnspan=2)
            btn.bind("<Button-1>", click)            

        else:
            btn = Button(keyFrame, text=f"{symbols[i][j]}", width=10, height=2, font=("Arial", 12, "bold"), bg="#121212", fg="white", activebackground="#080808", activeforeground="white", relief="groove")
            btn.grid(row=i, column=j, padx=5, pady=5)
            btn.bind("<Button-1>", click)

root.mainloop()
