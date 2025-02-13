from tkinter import*
r=Tk()
r.geometry("500x500")
l=Label(r)
e1=Entry(r)
e2=Entry(r)
def bmi():
    h=float(e1.get())
    w=float(e2.get())
    h1=h/100
    c=w/(h1**2)
    l.config(text=f'BMI={c}')
    

n1=Label(r,text='Enter Height(cm)=')
n2=Label(r,text='Enter Weight(kg)=')
#n3=Label(r,text='Result')
b=Button(r,text="CALCULATE",command=bmi)
n1.grid(row=0)
n2.grid(row=1)
#n3.grid(row=3)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b.grid(row=2)
l.grid(row=3,column=1)
#w.pack()
r.mainloop()
