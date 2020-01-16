from tkinter import *



class bill(Frame):
    def __init__(self,master):
        master.title('billing')
        Frame.__init__(self,master)
        self.l1 = Label(master, text="welcome to payment system", fg="red", font=("Areal", 15)).grid(row=0, column=1)
        self.l2 = Label(master, text="Enter Order", fg="green", font=("Areal", 15)).grid(row=1, column=1)
        self.l3 = Label(master, text="Sr No.", fg="blue", font=("Areal", 15)).grid(row=2, column=0)
        self.l3 = Label(master, text="Burgers", fg="blue", font=("Areal", 15)).grid(row=2, column=1)
        self.l4 = Label(master, text="Price", fg="blue", font=("Areal", 15)).grid(row=2, column=2)
        self.l5 = Label(master, text="Quantity", fg="blue", font=("Areal", 15)).grid(row=2, column=3)
        self.l6 = Label(master, text="1", fg="black", font=("Areal", 15)).grid(row=3, column=0)
        self.l7 = Label(master, text="2", fg="black", font=("Areal", 15)).grid(row=4, column=0)
        self.l8 = Label(master, text="3", fg="black", font=("Areal", 15)).grid(row=5, column=0)
        self.l9 = Label(master, text="4", fg="black", font=("Areal", 15)).grid(row=6, column=0)
        self.l10 = Label(master, text="Cheese Burger", fg="black", font=("Areal", 15)).grid(row=3, column=1)
        self.l11 = Label(master, text="Veg Cheese Burger", fg="black", font=("Areal", 15)).grid(row=4, column=1)
        self.l12 = Label(master, text="Non Veg Burger", fg="black", font=("Areal", 15)).grid(row=5, column=1)
        self.l13 = Label(master, text="Mix Veg Burger", fg="black", font=("Areal", 15)).grid(row=6, column=1)
        self.l14 = Label(master, text="50 Rs", fg="black", font=("Areal", 15)).grid(row=3, column=2)
        self.l15 = Label(master, text="60 Rs", fg="black", font=("Areal", 15)).grid(row=4, column=2)
        self.l16 = Label(master, text="70 Rs", fg="black", font=("Areal", 15)).grid(row=5, column=2)
        self.l17 = Label(master, text="80 Rs", fg="black", font=("Areal", 15)).grid(row=6, column=2)
        self.e1=Entry(master)
        self.e1.grid(row=3,column=3)
        self.e2 = Entry(master)
        self.e2.grid(row=4, column=3)
        self.e3 = Entry(master)
        self.e3.grid(row=5, column=3)
        self.e4 = Entry(master)
        self.e4.grid(row=6, column=3)
        self.l18 = Label(master, text="Sr No.", fg="blue", font=("Areal", 15)).grid(row=8, column=0)
        self.l19 = Label(master, text="Shakes", fg="blue", font=("Areal", 15)).grid(row=8, column=1)
        self.l20 = Label(master, text="Price", fg="blue", font=("Areal", 15)).grid(row=8, column=2)
        self.l21 = Label(master, text="Quantity", fg="blue", font=("Areal", 15)).grid(row=8, column=3)
        self.l22 = Label(master, text="1", fg="black", font=("Areal", 15)).grid(row=9, column=0)
        self.l23 = Label(master, text="2", fg="black", font=("Areal", 15)).grid(row=10, column=0)
        self.l24 = Label(master, text="3", fg="black", font=("Areal", 15)).grid(row=11, column=0)
        self.l25 = Label(master, text="4", fg="black", font=("Areal", 15)).grid(row=12, column=0)
        self.l26 = Label(master, text="Milk Shake", fg="black", font=("Areal", 15)).grid(row=9, column=1)
        self.l27 = Label(master, text="Chocolate Shake", fg="black", font=("Areal", 15)).grid(row=10, column=1)
        self.l28 = Label(master, text="Pineapple Shake", fg="black", font=("Areal", 15)).grid(row=11, column=1)
        self.l29 = Label(master, text="Strawberry Shake", fg="black", font=("Areal", 15)).grid(row=12, column=1)
        self.l30 = Label(master, text="50 Rs", fg="black", font=("Areal", 15)).grid(row=9, column=2)
        self.l31 = Label(master, text="60 Rs", fg="black", font=("Areal", 15)).grid(row=10, column=2)
        self.l32 = Label(master, text="70 Rs", fg="black", font=("Areal", 15)).grid(row=11, column=2)
        self.l33 = Label(master, text="80 Rs", fg="black", font=("Areal", 15)).grid(row=12, column=2)
        self.e5 = Entry(master)
        self.e5.grid(row=9, column=3)
        self.e6 = Entry(master)
        self.e6.grid(row=10, column=3)
        self.e7 = Entry(master)
        self.e7.grid(row=11, column=3)
        self.e8 = Entry(master)
        self.e8.grid(row=12, column=3)
        self.b1=Button(master,text="Total bill",width=10,height=2,bg="orange",padx=10,command=self.calculate).grid(row=14, column=1)
        self.b2=Button(master,text="Clear",width=10,height=2,bg="orange",padx=10,command=self.clear).grid(row=14, column=3)
        self.e9 = Entry(master)
        self.e9.grid(row=14, column=2)

    def calculate(self):
        cb=int(self.e1.get())
        vc=int(self.e2.get())
        nvc=int(self.e3.get())
        mv=int(self.e4.get())
        ms=int(self.e5.get())
        cs=int(self.e6.get())
        ps=int(self.e7.get())
        ss=int(self.e8.get())

        cd_quantity=50*cb
        vc_quantity=60*vc
        nvc_quantity=70*nvc
        mv_quantity=80*mv
        ms_quantity=50*ms
        cs_quantity=60*cs
        ps_quantity=70*ps
        ss_quantity=70*ss

        total_value=cd_quantity+vc_quantity+nvc_quantity+mv_quantity+ms_quantity+cs_quantity+ps_quantity+ss_quantity

        self.e9.insert(END,total_value)
    def clear(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        self.e7.delete(0,END)
        self.e8.delete(0,END)
        self.e9.delete(0,END)


    


obj=Tk()
app=bill(obj)
obj.mainloop()
