import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def searchFiles():
    global filename
    try:
        filename = filedialog.askdirectory(title="Choose directory")
        if filename == "":
            return
        chosenDirectory.config(text=f"Chosen directory: {filename}")
        sortBtn.grid(row=0, column=0, padx=5)
    except Exception as e:
        messagebox.showerror(title="Error", message=e)

def sortFiles():
    file_list = {
        ".exe": "Executables",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".py": "Python",
        ".mp3": "Music",
        ".mp4": "Videos",
        ".html": "HTML",
        ".docx": "Documents",
        ".pptx": "Presentation",
        ".txt": "Text Documents"
    }
    filelist = os.listdir(filename)
    for i in filelist:
        extension = os.path.splitext(f"{filename}/{i}")[1]
        if i == "app.py" or extension == ".lnk":
            continue        
        if extension != "":
            try:
                if extension in file_list.keys():
                    if not os.path.exists(f"{filename}/{file_list[extension]}"):
                        os.mkdir(f"{filename}/{file_list[extension]}")
                    
                    os.rename(f"{filename}/{i}", f"{filename}/{file_list[extension]}/{i}")
                
                else:
                    if not os.path.exists(f"{filename}/{extension} Files"):
                        os.mkdir(f"{filename}/{extension} Files")
                    os.rename(f"{filename}/{i}", f"{filename}/{extension} Files/{i}")
                    
            except Exception as e:
                messagebox.showerror(title="Error", message=f"{e}")
            
        else:
            continue
    
    messagebox.showinfo(title="Files Sorted", message="Files sorted successfully.")
    
root = Tk()
root.geometry("800x600")
root.title("File Sorter")
root.config(bg="#121212")

headingLabel = Label(root, text="File Sorter", bg="#001a33", fg="white", font=("Calibri", 20, "bold"))
headingLabel.pack(fill=X, padx=5, pady=5)

searchButton = Button(text="Choose Directory", padx=2, pady=2, bg="#113768", fg="white", relief=FLAT, activebackground="#001a33", activeforeground="white", font=("Calibri", 12), command=searchFiles)
searchButton.pack(pady=5)

mainFrame = Frame(root, bg="#121212")
mainFrame.pack(pady=30)

chosenDirectory = Label(mainFrame, bg="#121212", fg="white", font=("Calibri", 14, "bold"))
chosenDirectory.pack()

btnFrame = Frame(mainFrame, bg="#121212")
btnFrame.pack()

sortBtn = Button(btnFrame, text="Sort Files", padx=2, pady=2, bg="#0598ce", fg="white", relief=FLAT, activebackground="#113768", activeforeground="white", font=("Calibri", 12), command=sortFiles)
root.mainloop()
