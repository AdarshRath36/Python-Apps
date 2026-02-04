from tkinter import *
from tkinter import messagebox
import requests
import os

background = "#FFF4E6"
header = "#FF6B00"
primary = "#2C2C2C"
secondary = "#7A6A5F"
buttonc = "#FFA500"
activebuttonc = "#E67300"

def create_image(filename):
    wttrEmoji.image = PhotoImage(file=fr"{os.getcwd()}\assets\{filename}")
    wttrEmoji.config(image=wttrEmoji.image)

def get_weather(event=None):
    key = "cc5b4133252dc0ca7001ebfcbb2b837c"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={userInput.get()}&appid={key}"
    try:
        response = requests.get(url)
        info = response.json()
        status = response.status_code

        if status == 200:
            id = info['weather'][0]['id']
            temp = info['main']['temp']
            feels = info['main']['feels_like']
            humidity = info['main']['humidity']

            wttrMain.config(text=info['weather'][0]['main'])
            wttrDesc.config(text=info['weather'][0]['description'])

            if 200 <= id <= 232:
                create_image("thunder.png")
            
            elif 300 <= id <= 321:
                create_image("sunnyrain.png")
            
            elif 500 <= id <= 531:
                create_image("rain.png")
            
            elif 600 <= id <= 622:
                create_image("snow.png")
            
            elif 701 <= id <= 741:
                create_image("fog.png")
            
            elif id == 762:
                create_image("volcano.png")
            
            elif id == 781:
                create_image("tornado.png")
            
            elif id == 771:
                create_image("wind.png")
            
            elif id == 800:
                create_image("sunny.png")
            
            elif 801 <= id <= 804:
                create_image("cloud.png")
            
            wttrTemp.config(text="Temperature:")
            wttrTempVal.config(text=f"{temp-273.15:.1f}°C")

            wttrFeels.config(text="Feels Like:")
            wttrFeelsVal.config(text=f"{feels-273.15:.1f}°C")

            wttrHumidity.config(text="Humidity:")
            wttrHumidityVal.config(text=f"{humidity}%")
            
        
        elif status == 404:
            messagebox.showerror(title="Not Found", message="City not found")
        
        elif status == 401:
            messagebox.showerror(title="Invalid", message="Invalid API key")
        
        elif status == 403:
            messagebox.showerror(title="Forbidden", message="Access is denied")

        elif status == 503:
            messagebox.showerror(title="Service Unavailable", message="Server is down")
    
    except requests.exceptions.ConnectionError:
        messagebox.showerror(title="Connection Error", message="Check your internet connection")

root = Tk()
root.geometry("900x800")
root.title("Python Weather")
root.config(bg=background)
root.resizable(0, 0)

icon = PhotoImage(file=fr"{os.getcwd()}\assets\icon.png")
root.iconphoto(False, icon)

userInput = StringVar()

Label(text="Python Weather", bg=header, fg="white",font=("Arial", 30, "bold"), relief=RIDGE, borderwidth=6, padx=25, pady=25).pack(padx=15, pady=15, fill=X)

frame1 = Frame(root, bg=background)
frame1.pack(fill="x")

entryPrompt = Label(frame1, text="Enter the name of a city:", fg=primary, bg=background, font=("Arial", 18, "bold"))
entryPrompt.pack(side="left", padx=10, pady=10)

entry = Entry(frame1, textvariable=userInput, font=("Arial", 18))
entry.pack(side="left", fill="x", expand=True, padx=10)
entry.bind("<Return>", get_weather)
entry.insert(0, "Delhi")
entry.focus()

searchButton = Button(root, text="Search", bg=buttonc, fg=primary, font=("Arial", 15), pady=5, activebackground=activebuttonc, activeforeground="white", width=20, relief="ridge", command=get_weather)
searchButton.pack(anchor="center", pady=10)

frame2 = Frame(root, bg=background)
frame2.pack(fill="both", padx=45, pady=45)

wttrMain = Label(frame2, font=("Arial", 30, "bold"), bg=background, fg=primary)
wttrMain.pack(anchor="center")

wttrDesc = Label(frame2, font=("Arial", 18, "bold"), bg=background, fg=secondary)
wttrDesc.pack(anchor="center")

wttrEmoji = Label(frame2, font=("Arial", 50, "bold"), bg=background)
wttrEmoji.pack(anchor="center", pady=10)

frame3 = Frame(frame2, bg=background)
frame3.pack(pady=20)

wttrTemp = Label(frame3, font=("Arial", 14, "bold"), bg=background, fg=primary)
wttrTemp.grid(row=0, column=0, padx=20)

wttrTempVal = Label(frame3, font=("Arial", 14, "bold"), bg=background, fg=secondary)
wttrTempVal.grid(row=1, column=0, padx=20)

wttrFeels = Label(frame3, font=("Arial", 14, "bold"), bg=background, fg=primary)
wttrFeels.grid(row=0, column=1, padx=20)

wttrFeelsVal = Label(frame3, font=("Arial", 14, "bold"), bg=background, fg=secondary)
wttrFeelsVal.grid(row=1, column=1, padx=20)

wttrHumidity = Label(frame3, font=("Arial", 14, "bold"), bg=background, fg=primary)
wttrHumidity.grid(row=0, column=2, padx=20)

wttrHumidityVal = Label(frame3, font=("Arial", 14, "bold"), bg=background, fg=secondary)
wttrHumidityVal.grid(row=1, column=2, padx=20)

get_weather()

root.mainloop()
