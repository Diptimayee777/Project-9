from tkinter import *
from tkinter import ttk
import requests

def data_get():
    global w_label1, wb_label1, temp_label1, per_label1
    city=city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8dc5dcfd740f9fc67610bcf75d464891").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win= Tk()
win.title("WEATHER APP")
win.config(bg="navyblue")
win.geometry("500x570")

name_label=Label(win, text=("WEATHER APP"),
                 font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_label=Label(win, text="Enter City Name:",
              font=("Time New Roman", 17))
city_label.place(x=25, y=120, height=50, width=200)

city_name = StringVar()
city_entry=Entry(win, textvariable=city_name, font=("Time New Roman", 20))
city_entry.place(x=250, y=120, height=50, width=210)

done_button= Button(win, text="Done", 
                    font=("Time New Roman", 20, "bold"), command=data_get)
done_button.place(y=190, height=50, width=100, x=200)  

w_label=Label(win, text="Weather Climate:",
              font=("Time New Roman", 17))
w_label.place(x=25, y=260, height=50, width=210)

w_label1=Label(win, text="",
              font=("Time New Roman", 17))
w_label1.place(x=250, y=260, height=50, width=210)

wb_label=Label(win, text="Weather Description:",
              font=("Time New Roman", 16))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1=Label(win, text="",
              font=("Time New Roman", 17))
wb_label1.place(x=250, y=330, height=50, width=210)


temp_label=Label(win, text="Temperature:",
              font=("Time New Roman", 17))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1=Label(win, text="",
              font=("Time New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)


per_label=Label(win, text="Pressure:",
              font=("Time New Roman", 17))
per_label.place(x=25, y=470, height=50, width=210)

per_label1=Label(win, text="",
              font=("Time New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

win.mainloop()
