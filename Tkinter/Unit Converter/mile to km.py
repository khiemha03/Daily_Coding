from tkinter import *

def mile_conversion():
    kilometer_input.delete(0, END)
    value = float(mile_input.get()) * 1.609344
    kilometer_input.insert(END, f"{round(value,4)}")
def kilometer_conversion():
    mile_input.delete(0,END)
    value = float(kilometer_input.get())*0.621371192
    mile_input.insert(END,f"{round(value,4)}")

def clear():
    kilometer_input.delete(0, END)
    mile_input.delete(0,END)
window = Tk()

label_km = Label(window,text="Kilometer: ",font=("Times",20,"normal"))
label_km.grid(column=0,row=0)

label_mile= Label(window,text="Mile: ",font=("Times",20,"normal"))
label_mile.grid(column=0,row=1)

kilometer_input = Entry(window,width=15)
kilometer_input.grid(column= 1,row = 0)

mile_input = Entry(window,width=15)
mile_input.grid(column= 1,row = 1)

kilometer_button = Button(window,text="Convert to mile",command= kilometer_conversion,bd =5,padx = 39)
kilometer_button.grid(column=2, row =0, padx = 20)

convert_mile_button = Button(window,text="Convert to kilometer",command= mile_conversion,bd =5,padx = 25)
convert_mile_button.grid(column=2, row =1, padx = 20)

clear_button = Button(window,text="Clear all",command=clear,padx=170,bd=5)
clear_button.grid(column=0,row=3, columnspan=3)
window.mainloop()