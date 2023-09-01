from tkinter import *
#celcius to fahrenheit
def f():
    c= float(c_entry.get())
    f=c*9/5 + 32
    f_entry.delete(0,"end")
    f_entry.insert(0, str(f))
#fahrenheit to celcius    
def c():
    f=float(f_entry.get())
    c=5/9 *(f-32)
    c_entry.delete(0,"end")
    c_entry.insert(0,str(c))

root =Tk()
root.title("temperature converter")
# labels
label1=Label(root,text="celcius").grid(row = 0, column = 0)
label2=Label(root,text="fahrenheit").grid(row = 0, column = 1)

#input entry points
c_entry=Entry(root)
c_entry.grid(row=1,column=0)

f_entry=Entry(root)
f_entry.grid(row = 1, column = 1)

#buttons
ctof=Button(root, text="convert c to f",command=f).grid(row = 2, column = 0)
ftoc=Button(root, text="convert f to c",command=c).grid(row = 2, column = 1)

root.mainloop()