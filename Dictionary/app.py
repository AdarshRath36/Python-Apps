from tkinter import *
from tkinter import messagebox
import requests
import os

bg_color = "#0D1B2A"
header_color = "#1B263B"
primary_text = "#E0E1DD"
secondary_text = "#A9B4C2"
input_bg = "#1B263B"
input_border = "#415A77"
button_color = "#415A77"
button_hover = "#778DA9"
result_bg = "#132137"
error_color = "#EF5350"


def hover_on(e):
    searchButton.config(bg=button_hover)


def hover_off(e):
    searchButton.config(bg=button_color)


def search(e=None):
    word = userInput.get().strip()

    if not word:
        messagebox.showerror("No Word", "Please enter a word")
        return

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        response = requests.get(url)
        status = response.status_code

        if status == 200:
            data = response.json()
            result_text.config(state=NORMAL)
            result_text.delete(1.0, END)

            count = 1  # continuous numbering

            for h in range(len(data)):
                for i in range(len(data[h]["meanings"])):

                    if count == 1:
                        result_text.insert(
                            END,
                            f"{count}. {data[h]['meanings'][i]['partOfSpeech'].capitalize()}\n",
                            "bold_tag",
                        )
                    else:
                        result_text.insert(
                            END,
                            f"\n\n{count}. {data[h]['meanings'][i]['partOfSpeech'].capitalize()}\n",
                            "bold_tag",
                        )

                    for j in range(len(data[h]["meanings"][i]["definitions"])):
                        result_text.insert(
                            END,
                            f"  • {data[h]['meanings'][i]['definitions'][j]['definition']}\n",
                        )

                    count += 1
            result_text.config(state=DISABLED)

        elif status == 404:
            messagebox.showerror("Not Found", "Word not found")

        elif status == 403:
            messagebox.showerror("Forbidden", "Access is denied")

        elif status == 503:
            messagebox.showerror("Service Unavailable", "Server is down")

        else:
            messagebox.showerror("Error", f"Unexpected error: {status}")

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Connection Error", "Check your internet connection")


root = Tk()
root.title("Python Dictionary")
root.config(bg=bg_color)
root.geometry("800x800")
root.resizable(0, 0)

icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)

userInput = StringVar()

Label(
    text="Python Dictionary",
    bg=header_color,
    fg="white",
    font=("Arial", 30, "bold"),
    relief=RIDGE,
    borderwidth=6,
    padx=25,
    pady=25,
).pack(padx=15, pady=15, fill=X)

frame1 = Frame(root, bg=bg_color)
frame1.pack(fill="x")

heading = Label(
    frame1,
    text="Enter a word:",
    fg=primary_text,
    bg=bg_color,
    font=("Arial", 18, "bold"),
)
heading.pack(side="left", padx=10, pady=10)

entry = Entry(
    frame1,
    textvariable=userInput,
    font=("Arial", 18),
    bg=input_bg,
    fg=secondary_text,
    insertbackground="white",
)
entry.pack(side="left", fill="x", expand=True, padx=10)

entry.bind("<Return>", search)
entry.focus()

searchButton = Button(
    root,
    text="Search",
    bg=button_color,
    fg=primary_text,
    font=("Arial", 15),
    pady=5,
    activebackground=button_color,
    activeforeground="white",
    width=20,
    relief="ridge",
    command=search,
)
searchButton.pack(anchor="center", pady=10)

searchButton.bind("<Enter>", hover_on)
searchButton.bind("<Leave>", hover_off)

frame2 = Frame(root, bg=result_bg)
frame2.pack(fill="both", expand=True, padx=25, pady=25)

scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=Y)

result_text = Text(
    frame2,
    wrap=WORD,
    font=("Arial", 14),
    bg=result_bg,
    fg=secondary_text,
    yscrollcommand=scrollbar.set,
    relief=FLAT,
    padx=10,
    pady=10,
    insertbackground=primary_text,
    state=DISABLED
)

result_text.tag_configure(
    "bold_tag", font=("Arial", 14, "bold"), foreground="#E0E1DD"
)

result_text.pack(fill=BOTH, expand=True)
scrollbar.config(command=result_text.yview)

root.mainloop()
