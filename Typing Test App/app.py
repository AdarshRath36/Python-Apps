from tkinter import *
from tkinter import messagebox
import random
import os

root = Tk()
root.geometry("800x600")
root.title("Python Typing Test")
root.config(bg="#e0f7fa")
root.resizable(0, 0)

user = os.environ.get('USERNAME')
textFile = f"C:/Users/{user}/Desktop/highscore.txt"

if not os.path.isfile(textFile):
    with open("highscore.txt", "w") as file:
        texts = ["0\n", "0\n", "0"]
        for i in texts:
            file.write(i)

global username
username = StringVar()
username.set("Username")

global revList
revList = []
with open("highscore.txt", "r") as file:
    for line in file:
        revList.append(line.strip())

def createUser():
    global username
    userPrompt = Toplevel(root)
    userPrompt.geometry("300x200")
    userPrompt.resizable(False, False)
    userPrompt.config(bg="#e0f7fa")
    Label(userPrompt, text="Create New User", fg="white", bg="#0288d1", relief=RIDGE, padx=5, pady=10, font=("Arial", 18, "bold")).pack(padx=5, pady=5, anchor=N, fill="x")
    frame3 = Frame(userPrompt, bg="#e0f7fa")
    frame3.pack()
    Label(frame3, text="Name:", fg="#003b64", font=("Arial", 12, "bold"), bg="#e0f7fa").pack(side="left", padx=5)
    enterUsername = Entry(frame3, textvariable=username, font=("Arial", 12, "bold"), fg="#0d47a1")
    enterUsername.pack(side="left", padx=5)
    enterUsername.focus_set()
    enterUsername.bind("<Return>", lambda event: userPrompt.destroy())
    Button(userPrompt, text="Create", bg="#0097a7", fg="white", padx=5, pady=5, relief="ridge", width=10, font=("Arial", 12, "bold"), activebackground="#007c91", activeforeground="white", command=userPrompt.destroy).pack(side="bottom", padx=5, pady=5)

def saveHighScore(event=None):
    global wpm, accuracy
    global revList
    global username

    ogList = [f"{username.get()}\n", f"{wpm:.2f}\n", f"{accuracy:.2f}"]

    if wpm > float(revList[1]) and accuracy > float(revList[2]):
        with open("highscore.txt", "w") as file:
            file.write(f"{username.get()}\n{wpm:.2f}\n{accuracy:.2f}")
        revList.clear()
        for item in ogList:
            revList.append(item.strip())
    messagebox.showinfo(title="High Score Saved", message="High Score has been saved successfully!")

root.bind("<Control-s>", saveHighScore)

def viewHighScore():
    global revList
    highScoreWindow = Toplevel(root)
    highScoreWindow.geometry("300x400")
    highScoreWindow.resizable(False, False)
    highScoreWindow.config(bg="#e0f7fa")
    Label(highScoreWindow, text="High Score", fg="white", bg="#0288d1", relief=RIDGE, padx=5, pady=10, font=("Arial", 18, "bold")).pack(padx=5, pady=5, anchor=N, fill="x")
    frame4 = Frame(highScoreWindow, bg="#e0f7fa")
    frame4.pack()
    Label(frame4, text="Name:", fg="#003b64", font=("Arial", 12, "bold"), bg="#e0f7fa").pack(side="left", padx=5)
    Label(frame4, text=revList[0], fg="#0d47a1", font=("Arial", 12, "bold"), bg="#e0f7fa").pack(side="right", padx=5)

    frame5 = Frame(highScoreWindow, bg="#e0f7fa")
    frame5.pack()
    Label(frame5, text="WPM:", fg="#003b64", font=("Arial", 12, "bold"), bg="#e0f7fa").pack(side="left", padx=5)
    Label(frame5, text=revList[1], fg="#0d47a1", font=("Arial", 12, "bold"), bg="#e0f7fa").pack(side="right", padx=5)

    frame6 = Frame(highScoreWindow, bg="#e0f7fa")
    frame6.pack()
    Label(frame6, text="Accuracy:", fg="#003b64", font=("Arial", 12, "bold"), bg="#e0f7fa").pack(side="left", padx=5)
    Label(frame6, text=revList[2], fg="#0d47a1", font=("Arial", 12, "bold"), bg="#e0f7fa").pack(side="right", padx=5)
    highScoreWindow.mainloop()

def exitWindow():
    if messagebox.askyesno(title="Exit Program", message="Are you sure you want to exit this program?"):
        exit()
    else:
        return

refSentences = [
    "Homesickness became contagious in the young campers' cabin",
    "She wanted to be rescued, but only if it was Tuesday and raining",
    "Flesh-colored yoga pants were far worse than even he feared.",
    "Let's all be unique together until we realise we are all the same.",
    "The chic gangster liked to start the day with a pink scarf.",
    "As he looked out the window, he saw a clown walk by",
    "It's not often you find a soggy banana on the street",
    "I covered my friend in baby oil"
]

def reset():
    global timeSpent, timerRunning, finishedTest, randsen
    finishedTest = False
    timerRunning = False
    timeSpent = 0
    wpm = 0
    timeTaken.config(text=f"Time: {timeSpent}")
    wordsPerMinute.config(text=f"WPM: {wpm}")
    accuracyLive.config(text="Accuracy: 0")
    userText.set("")
    randsen = random.choice(refSentences)
    reference.config(text=f"{randsen}")
    userInput.focus_set()

timeSpent = 0
global wpm
wpm = 0
accuracy = 0
timerRunning = False
global finishedTest
finishedTest = False

randsen = random.choice(refSentences)

menuBar = Menu(root)
root.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0, bg="#ffffff", fg="#000000", activebackground="#001f3f", activeforeground="white")
fileMenu.add_command(label="Save High Score", command=saveHighScore)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitWindow)
menuBar.add_cascade(label="File", menu=fileMenu)

userMenu = Menu(menuBar, tearoff=0, bg="#ffffff", fg="#000000", activebackground="#001f3f", activeforeground="white")
userMenu.add_command(label="Create New User", command=createUser)
userMenu.add_command(label="View High Score", command=viewHighScore)
menuBar.add_cascade(label="User", menu=userMenu)

userText = StringVar()

Label(
    root, text="Python Typing Test", fg="white", bg="#0288d1",
    relief=RIDGE, padx=5, pady=10, font=("Arial", 22, "bold")
).pack(padx=5, pady=5, anchor=N, fill="x")

reference = Label(
    root, text=randsen, padx=10, pady=10, anchor="n",
    font=("Arial", 16, "bold"), fg="#01579b", bg="#e0f7fa", wraplength=750, justify="center"
)
reference.pack(padx=20, pady=10)

userInput = Entry(
    root, font=("Arial", 18), textvariable=userText, justify="center",
    bg="#ffffff", fg="#0d47a1", relief=GROOVE
)
userInput.pack(padx=20, fill="x", pady=15)

frame2 = Frame(root, bg="#e0f7fa")
frame2.pack(padx=5, pady=30)

timeTaken = Label(frame2, text=f"Time: {timeSpent}", font=("Arial", 15, "bold"), bg="#e0f7fa", fg="#003b64")
timeTaken.pack(side="right", padx=50)

wordsPerMinute = Label(frame2, text=f"WPM: {wpm}", font=("Arial", 15, "bold"), bg="#e0f7fa", fg="#003b64")
wordsPerMinute.pack(side="right", padx=50)

accuracyLive = Label(frame2, text=f"Accuracy: {accuracy}", font=("Arial", 15, "bold"), bg="#e0f7fa", fg="#003b64")
accuracyLive.pack(side="right", padx=50)

def update_time():
    global finishedTest
    if not finishedTest:
        global timeSpent
        timeSpent += 1
        timeTaken.config(text=f"Time: {timeSpent}")
        root.after(1000, update_time)

def start(event=None):
    global timerRunning
    if not timerRunning:
        timerRunning = True
        update_time()

def finish(event):
    global finishedTest
    finishedTest = True
    global wpm, accuracy
    global revList
    global username
    userTextChars = userText.get()
    userTextSplit = len(userTextChars.split())

    wpm = (userTextSplit / (timeSpent / 60))

    correctChars = 0
    for i in range(min(len(userTextChars), len(randsen))):
        if userTextChars[i] == randsen[i]:
            correctChars += 1

    accuracy = (correctChars / len(randsen)) * 100

    wordsPerMinute.config(text=f"WPM: {wpm:.2f}")
    accuracyLive.config(text=f"Accuracy: {accuracy:.2f}%")

frame1 = Frame(root, bg="#e0f7fa")
frame1.pack(padx=10, pady=5, fill="x", side="bottom")

startTest = Button(
    frame1, text="Start", bg="#0097a7", fg="white", padx=5, pady=5, relief="ridge",
    width=10, font=("Arial", 12, "bold"), activebackground="#007c91", activeforeground="white",
    command=start
)
startTest.pack(side="left", padx=10)

resetTest = Button(
    frame1, text="Reset", bg="#00acc1", fg="white", padx=5, pady=5, relief="ridge",
    width=10, font=("Arial", 12, "bold"), activebackground="#008b9a", activeforeground="white",
    command=reset
)
resetTest.pack(side="left", padx=10)

userInput.bind("<Key>", start)
userInput.bind("<Return>", finish)

root.mainloop()
