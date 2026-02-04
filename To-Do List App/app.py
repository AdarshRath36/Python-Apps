from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

def submit_task(event=None):
	task = entry1.get()
	if task.strip() != "":
		main_listbox.insert(END, task.strip())
		entry1.delete(0, END)
		entry1.focus()
		main_listbox.selection_clear(0, END)

	else:
		messagebox.showerror(title="An error occurred", message="Please enter a task to insert.")

def delete_tasks(event=None):
	if main_listbox.curselection():
		for i in reversed(main_listbox.curselection()):
			main_listbox.delete(i)
		main_listbox.selection_clear(0, END)

	else:
		messagebox.showerror(title="An error occurred", message="Please select the tasks to delete.")

def button_state(event):
	if main_listbox.curselection():
		button2.config(state="normal")
		button3.config(state="normal")
		button4.config(state="normal")

	else:
		button2.config(state="disabled")
		button3.config(state="disabled")
		button4.config(state="disabled")

def mark_tasks(event=None):
    if main_listbox.curselection():
        for i in reversed(main_listbox.curselection()):
            task_text = main_listbox.get(i)
            if "✔" not in task_text:
                main_listbox.delete(i)
                main_listbox.insert(i, f"{task_text} ✔")
            else:
                messagebox.showerror(title="An error occurred", message=f"The task - {task_text.removesuffix(' ✔')} is already marked.")
        main_listbox.selection_clear(0, END)

    else:
        messagebox.showerror(title="An error occurred", message="Please select the tasks to mark")

def unmark_tasks(event=None):
    if main_listbox.curselection():
        for i in reversed(main_listbox.curselection()):
            task_text = main_listbox.get(i)
            if "✔" in task_text:
                main_listbox.delete(i)
                main_listbox.insert(i, task_text.removesuffix(' ✔'))
            else:
                messagebox.showerror(title="An error occurred", message=f"The task - {task_text} is already unmarked.")
            main_listbox.selection_clear(0, END)

    else:
        messagebox.showerror(title="An error occurred", message="Please select the tasks to unmark")

def save_task(event=None):
        if not os.path.exists("Tasks"):
                os.mkdir("Tasks")

        else:
                file = filedialog.asksaveasfile(title="Save Tasks As", initialdir="Tasks", mode="w", defaultextension=".txt", filetypes=(("Text Document", ".txt"), ("All Files", ".*")))
                if file:
                        tasks = []
                        for i in main_listbox.get(0, END):
                                tasks.append(i)

                        for item in tasks:
                                file.write(f"{item.strip()}\n")
                        file.close()

def open_task(event=None):
	file = filedialog.askopenfilename(title="Open Tasks File", initialdir="Tasks", defaultextension=".txt", filetypes=(("Text Document", ".txt"), ("All Files", ".*")))
	if file:
		main_listbox.delete(0, END)
		with open(file, "r") as filename:
			for index, line in enumerate(filename):
				main_listbox.insert(index, line.strip())

def clear_all(event=None):
	if messagebox.askyesno(title="Clear all tasks", message="Are you sure that you want to clear all tasks?"):
		main_listbox.delete(0, END)
		entry1.focus()
	else:
		return

root = Tk()
root.title("To-Do List App")
root.geometry("920x600")
root.config(bg="light yellow")

icon = PhotoImage(file=fr"Icons\icon.png")
root.iconphoto(True, icon)

root.bind("<Return>", submit_task)
root.bind("<Delete>", delete_tasks)
root.bind("<Control-s>", save_task)
root.bind("<Control-o>", open_task)
root.bind("<Control-Delete>", clear_all)

menu1 = Menu(root)
root.config(menu = menu1)

filemenu = Menu(menu1, tearoff=0)
menu1.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save Tasks As", command=save_task)
filemenu.add_command(label="Open Tasks File", command=open_task)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
editmenu = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Clear All Tasks", command=clear_all)

head = Label(root, text="Python To-Do List App", relief="ridge", bg="red", fg="white", bd=3, font=("Calibri", 25, "bold"))
head.pack(pady=15, padx=15, fill="x")

frame1 = Frame(root, bg="light yellow")
frame1.pack(anchor="n", padx=15)

input_frame = Frame(frame1, bg="light yellow")
input_frame.pack()

buttons_frame = Frame(frame1, bg="light yellow")
buttons_frame.pack()

label1 = Label(input_frame, text="Enter a task:", font=("Calibri", 15), bg="light yellow")
label1.pack(side="left", padx=10)

entry1 = Entry(input_frame, font=("Calibri", 15), width=30)
entry1.pack(side="right", padx=10)
entry1.focus()

button1 = Button(buttons_frame, text="Add Task", font=("Calibri", 15, "bold"), bg="green", fg="white", activebackground="dark green", activeforeground="white", command=submit_task, relief="ridge", width=20, bd=3)
button1.pack(pady=15, side="left", padx=5)

button2 = Button(buttons_frame, text="Delete Selected", font=("Calibri", 15, "bold"), fg="white", bg="red", activebackground="dark red", activeforeground="white", command=delete_tasks, relief="ridge", width=20, bd=3)
button2.pack(pady=15, side="left", padx=5)

button3 = Button(buttons_frame, text="Mark as Done", font=("Calibri", 15, "bold"), fg="white", bg="blue", activebackground="dark blue", activeforeground="white", command=mark_tasks, relief="ridge", width=20, bd=3)
button3.pack(pady=15, side="left", padx=5)

button4 = Button(buttons_frame, text="Unmark Selected", font=("Calibri", 15, "bold"), fg="black", bg="yellow", activebackground="#B8860B", activeforeground="white", command=unmark_tasks, relief="ridge", width=20, bd=3)
button4.pack(pady=15, side="left", padx=5)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

main_listbox = Listbox(root, fg="black", font=("Ink Free", 18), selectmode="multiple", yscrollcommand=scrollbar.set)
main_listbox.pack(fill="both", padx=15, pady=15, expand=True)

scrollbar.config(command=main_listbox.yview)

button2.config(state="disabled")
button3.config(state="disabled")
button4.config(state="disabled")

main_listbox.bind("<<ListboxSelect>>", button_state)
main_listbox.bind("<Control-m>", mark_tasks)
main_listbox.bind("<Control-u>", unmark_tasks)

root.mainloop()
