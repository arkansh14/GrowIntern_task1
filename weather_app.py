from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=51986b701ddfae105efcca1b2665529b").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)) + " °C")
    min_label1.config(text=str(int(data["main"]["temp_min"] - 273.15)) + " °C")
    max_label1.config(text=str(int(data["main"]["temp_max"] - 273.15)) + " °C")


win = Tk()
win.title ("The Weather App")
win.config(bg="royal blue1")
win.geometry("500x600")

name_label = Label(win, text="Arkansh Weather App", 
                   font=("Bookman Old Style", 27, "bold"))
name_label.place(x=25, y=50, height=50, width=450)


city_name = StringVar()

list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", 
             "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", 
             "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
             "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", 
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", 
             "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", 
             "Dadra and Nagar Haveli", "Daman and Diu", "Ladakh", "Lakshadweep", "Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Arial", 20, "bold"),textvariable=city_name)
com.place(x=25, y=120, height=50, width=450) 

w_label = Label(win, text="Weather Climate", 
                   font=("Times New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", 
                   font=("Times New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)


wb_label = Label(win, text="Weather Description", 
                   font=("Times New Roman", 18))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text="", 
                   font=("Times New Roman", 18))
wb_label1.place(x=250, y=330, height=50, width=210)


temp_label = Label(win, text="Temperature", 
                   font=("Times New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text="", 
                   font=("Times New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)


min_label = Label(win, text="Min. Temp", 
                   font=("Times New Roman", 20))
min_label.place(x=25, y=470, height=50, width=210)
min_label1 = Label(win, text="", 
                   font=("Times New Roman", 20))
min_label1.place(x=250, y=470, height=50, width=210)


max_label = Label(win, text="Max. Temp", 
                   font=("Times New Roman", 20))
max_label.place(x=25, y=540, height=50, width=210)
max_label1 = Label(win, text="", 
                   font=("Times New Roman", 20))
max_label1.place(x=250, y=540, height=50, width=210)

done_button = Button(win, text="Get Weather", 
                   font=("Calibri", 13, "bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()