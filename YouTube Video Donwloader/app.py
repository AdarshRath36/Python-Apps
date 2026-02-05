from tkinter import *
from tkinter import messagebox
from yt_dlp import YoutubeDL

root = Tk()
root.title("YouTube Video Downloader")
root.geometry("800x600")
root.config(bg="#121212")

userFileName = StringVar()
userFileName.set("")
userVideoURL = StringVar()

def downloadvideo():
    url = userVideoURL.get().strip()
    filename = userFileName.get().strip()

    if not url:
        messagebox.showerror("Invalid URL", "Please enter a YouTube URL.")
        return

    if filename and not filename.endswith(".mp4"):
        messagebox.showerror("Invalid Filename", "Filename must end with .mp4")
        return

    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": filename if filename else "%(title)s.%(ext)s",
            "quiet": True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Download Completed", "Download completed successfully.")

    except Exception as e:
        messagebox.showerror("Error", "Failed to download video.")

label1 = Label(
    root,
    text="YouTube Video Downloader",
    bg="#CC181E",
    fg="white",
    font=("Calibri", 18, "bold"),
    padx=5,
    pady=5
)
label1.pack(pady=5, fill=X)

borderFrame = Frame(root, bg="#CC181E")
borderFrame.pack(padx=10, pady=5, fill=BOTH, expand=TRUE)

formFrame = Frame(borderFrame, bg="#303030")
formFrame.pack(padx=5, pady=5, fill=BOTH, expand=TRUE)

field1 = Frame(formFrame, bg="#303030")
field1.pack(padx=5, pady=10)

fieldLabel1 = Label(field1, text="Enter url:", font=("Calibri", 15, "bold"), bg="#303030", fg="white")
fieldLabel1.grid(row=0, column=0, padx=5)

fieldInput1 = Entry(field1, font=("Calibri", 12), width=45, textvariable=userVideoURL)
fieldInput1.grid(row=0, column=1)

fieldLabel2 = Label(field1, text="Save as (optional):", font=("Calibri", 15, "bold"), bg="#303030", fg="white")
fieldLabel2.grid(row=1, column=0, padx=5, pady=10)

fieldInput2 = Entry(field1, font=("Calibri", 12), width=45, textvariable=userFileName)
fieldInput2.grid(row=1, column=1)

fieldButton1 = Button(
    formFrame,
    text="Download",
    font=("Calibri", 12),
    bg="#CC181E",
    fg="white",
    padx=5,
    pady=5,
    activebackground="brown",
    activeforeground="white",
    relief=FLAT,
    width=10,
    command=downloadvideo
)
fieldButton1.pack()

root.mainloop()
