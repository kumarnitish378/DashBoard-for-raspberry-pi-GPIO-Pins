#import RPi.GPIO as g
import time
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("RASPBERRY PI GPIO PIN CONTROLLER")
root.geometry("1200x650")
root.config(bg="#132458")
#functions
counter =IntVar()
counter1 =IntVar()
counter2 =IntVar()
counter3=IntVar()
counter4 =IntVar()
counter5 =IntVar()
counter6 =IntVar()
counter7 =IntVar()
counter8 =IntVar()
counter9 =IntVar()
counter10 =IntVar()
counter11 =IntVar()


#Variable for GPIO PIN Indicator
gpio=IntVar()
gpio1=IntVar()
gpio2=IntVar()
gpio3=IntVar()
gpio4=IntVar()
gpio5=IntVar()
gpio6=IntVar()
gpio7=IntVar()
gpio8=IntVar()
gpio9=IntVar()
gpio10=IntVar()
gpio11=IntVar()




#a.set("GPIO-1 PIN is OFF")
lst=["ON","OFF"]
counter.set(0)
counter1.set(0)
counter2.set(0)
counter3.set(0)
counter4.set(0)
counter5.set(0)
counter6.set(0)
counter7.set(0)
counter8.set(0)
counter9.set(0)
counter10.set(0)
counter11.set(0)

#GPIO 1
def GPIO1(var,value):
    counter.set(var.get()+value)
    if counter.get()%2 != 0:
        gpio.set("GPIO-1 PIN is ON ")
        label = Label(f3, textvariable=gpio, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=1, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="BLOCK A", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,command=lambda: GPIO1(counter, 1))
        l2.grid(row=1, column=1, ipadx=15, ipady=5, padx=10, pady=7)

    else:
        gpio.set("GPIO-1 PIN is OFF")
        label = Label(f3, textvariable=gpio, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=1, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="BLOCK A", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,command=lambda: GPIO1(counter, 1))
        l2.grid(row=1, column=1, ipadx=15, ipady=5, padx=10, pady=7)

#GPIO 2
def GPIO2(var,value):
    counter1.set(var.get()+value)
    if counter1.get()%2 != 0:
        gpio1.set("GPIO-2 PIN is ON ")
        label = Label(f3, textvariable=gpio1, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=1, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-2", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,command=lambda: GPIO2(counter1, 1))
        l2.grid(row=1, column=3, ipadx=15, ipady=5, padx=10, pady=7)

    else:
        gpio1.set("GPIO-2 PIN is OFF")
        label = Label(f3, textvariable=gpio1, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=1, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-2", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,command=lambda: GPIO2(counter1, 1))
        l2.grid(row=1, column=3, ipadx=15, ipady=5, padx=10, pady=7)


#GPIO 3
def GPIO3(var,value):
    counter2.set(var.get()+value)
    if counter2.get()%2 != 0:
        gpio2.set("GPIO-3 PIN is ON ")
        label = Label(f3, textvariable=gpio2, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=2, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-3", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO3(counter2, 1))
        l2.grid(row=2, column=1, ipadx=15, ipady=5, padx=10, pady=7)


    else:
        gpio2.set("GPIO-3 PIN is OFF")
        label = Label(f3, textvariable=gpio2, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=2, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-3", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,command=lambda: GPIO3(counter2, 1))
        l2.grid(row=2, column=1, ipadx=15, ipady=5, padx=10, pady=7)


#GPIO 4
def GPIO4(var,value):
    counter3.set(var.get()+value)
    if counter3.get()%2 != 0:
        gpio3.set("GPIO-4 PIN is ON ")
        label = Label(f3, textvariable=gpio3, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=2, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-4", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO4(counter3, 1))
        l2.grid(row=2, column=3, ipadx=15, ipady=5, padx=10, pady=7)


    else:
        gpio3.set("GPIO-4 PIN is OFF")
        label = Label(f3, textvariable=gpio3, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=2, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-4", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO4(counter3, 1))
        l2.grid(row=2, column=3, ipadx=15, ipady=5, padx=10, pady=7)


#GPIO 5
def GPIO5(var,value):
    counter4.set(var.get()+value)
    if counter4.get()%2 != 0:
        gpio4.set("GPIO-5 PIN is ON ")
        label = Label(f3, textvariable=gpio4, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=3, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-5", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO5(counter4, 1))
        l2.grid(row=3, column=1, ipadx=15, ipady=5, padx=10, pady=7)

    else:
        gpio4.set("GPIO-5 PIN is OFF")
        label = Label(f3, textvariable=gpio4, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=3, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-5", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO5(counter4, 1))
        l2.grid(row=3, column=1, ipadx=15, ipady=5, padx=10, pady=7)



#GPIO 6
def GPIO6(var,value):
    counter5.set(var.get()+value)
    if counter5.get()%2 != 0:
        gpio5.set("GPIO-6 PIN is ON ")
        label = Label(f3, textvariable=gpio5, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=3, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-6", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO6(counter5, 1))
        l2.grid(row=3, column=3, ipadx=15, ipady=5, padx=10, pady=7)


    else:
        gpio5.set("GPIO-6 PIN is OFF")
        label = Label(f3, textvariable=gpio5, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=3, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-6", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO6(counter5, 1))
        l2.grid(row=3, column=3, ipadx=15, ipady=5, padx=10, pady=7)


#GPIO 7
def GPIO7(var,value):
    counter6.set(var.get()+value)
    if counter6.get()%2 != 0:
        gpio6.set("GPIO-7 PIN is ON ")
        label = Label(f3, textvariable=gpio6, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=4, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-7", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO7(counter6, 1))
        l2.grid(row=4, column=1, ipadx=15, ipady=5, padx=10, pady=7)


    else:
        gpio6.set("GPIO-7 PIN is OFF")
        label = Label(f3, textvariable=gpio6, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=4, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-7", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO7(counter6, 1))
        l2.grid(row=4, column=1, ipadx=15, ipady=5, padx=10, pady=7)


#GPIO 8
def GPIO8(var,value):
    counter7.set(var.get()+value)
    if counter7.get()%2 != 0:
        gpio7.set("GPIO-8 PIN is ON ")
        label = Label(f3, textvariable=gpio7, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=4, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-8", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO8(counter7, 1))
        l2.grid(row=4, column=3, ipadx=15, ipady=5, padx=10, pady=7)

    else:
        gpio7.set("GPIO-8 PIN is OFF")
        label = Label(f3, textvariable=gpio7, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=4, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-8", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO8(counter7, 1))
        l2.grid(row=4, column=3, ipadx=15, ipady=5, padx=10, pady=7)


#GPIO 9
def GPIO9(var,value):
    counter8.set(var.get()+value)
    if counter8.get()%2 != 0:
        gpio8.set("GPIO-9 PIN is ON ")
        label = Label(f3, textvariable=gpio8, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=5, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-9", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO9(counter8, 1))
        l2.grid(row=5, column=1, ipadx=15, ipady=5, padx=10, pady=7)


    else:
        gpio8.set("GPIO-9 PIN is OFF")
        label = Label(f3, textvariable=gpio8, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=5, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-9", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO9(counter8, 1))
        l2.grid(row=5, column=1, ipadx=15, ipady=5, padx=10, pady=7)


#GPIO 10
def GPIO10(var,value):
    counter9.set(var.get()+value)
    if counter9.get()%2 != 0:
        gpio9.set("GPIO-10 PIN is ON ")
        label = Label(f3, textvariable=gpio9, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=5, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-10", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO10(counter9, 1))
        l2.grid(row=5, column=3, ipadx=15, ipady=5, padx=10, pady=7)


    else:
        gpio9.set("GPIO-10 PIN is OFF")
        label = Label(f3, textvariable=gpio9, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=5, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-10", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO10(counter9, 1))
        l2.grid(row=5, column=3, ipadx=15, ipady=5, padx=10, pady=7)


#GPIO 11
def GPIO11(var,value):
    counter10.set(var.get()+value)
    if counter10.get()%2 != 0:
        gpio10.set("GPIO-11 PIN is ON ")
        label = Label(f3, textvariable=gpio10, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=6, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-11", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO11(counter10, 1))
        l2.grid(row=6, column=1, ipadx=15, ipady=5, padx=10, pady=7)


    else:
        gpio10.set("GPIO-11 PIN is OFF")
        label = Label(f3, textvariable=gpio10, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=6, column=0, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-11", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO11(counter10, 1))
        l2.grid(row=6, column=1, ipadx=15, ipady=5, padx=10, pady=7)


#GPIO 12
def GPIO12(var,value):
    counter11.set(var.get()+value)
    if counter11.get()%2 != 0:
        gpio11.set("GPIO-12 PIN is ON ")
        label = Label(f3, textvariable=gpio11, bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=6, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-12", bg="green", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO12(counter11, 1))
        l2.grid(row=6, column=3, ipadx=15, ipady=5, padx=10, pady=7)

    else:
        gpio11.set("GPIO-12 PIN is OFF")
        label = Label(f3, textvariable=gpio11, bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
        label.grid(row=6, column=1, pady=7,padx=10,ipadx=15,ipady=5)
        l2 = Button(f2, text="GPIO-12", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN,
                    command=lambda: GPIO12(counter11, 1))
        l2.grid(row=6, column=3, ipadx=15, ipady=5, padx=10, pady=7)


#all frames
f1 = Frame(root,bg="#132458",relief=SUNKEN,borderwidth=15)
f1.pack(side="left", fill="both")
f2=Frame(root,bg="#001245",borderwidth=6,relief=SUNKEN)
f2.pack(side="left", fill="both")
f3=Frame(root,bg="#001245",relief=SUNKEN,borderwidth=5)
f3.pack(side="right",fill="both")
#Initial condition of indi.
label = Label(f3, text="GPIO-1 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=1, column=0, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-2 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=1, column=1, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-3 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=2, column=0, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-4 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=2, column=1, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-5 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=3, column=0, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-6 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=3, column=1, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-7 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=4, column=0, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-8 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=4, column=1, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-9 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=5, column=0, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-10 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=5, column=1, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-11 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=6, column=0, pady=7,padx=10,ipadx=15,ipady=5)

label = Label(f3, text="GPIO-12 PIN is OFF", bg="red", font=('Comic Sans MS', 20, 'bold'), borderwidth=6, relief=SUNKEN)
label.grid(row=6, column=1, pady=7,padx=10,ipadx=15,ipady=5)

#dashboard

l2=Button(f2,text="Show GPIO",bg="#ffaa12",font=('Comic Sans MS',10,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :(GPIO1(counter,0),GPIO2(counter1,0),GPIO3(counter2,0),GPIO4(counter3,0),GPIO5(counter4,0),GPIO6(counter5,0),GPIO7(counter6,0),GPIO8(counter7,0),GPIO9(counter8,0),GPIO10(counter9,0),GPIO11(counter10,0),GPIO12(counter11,0)))
l2.grid(row=0,column=2,ipadx=1,ipady=1,padx=1,pady=1)
#l2=Button(f2,text="Show GPIO",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :(GPIO1(counter,1),GPIO2(counter1,1),GPIO3(counter2,1),GPIO4(counter3,1),GPIO5(counter4,1),GPIO6(counter5,1),GPIO7(counter6,1),GPIO8(counter7,1),GPIO9(counter8,1),GPIO10(counter9,1),GPIO11(counter10,1),GPIO12(counter11,1)))
#l2.grid(row=0,column=3,ipadx=5,ipady=5,padx=2,pady=2)


#label of all window
l = Label(f2,text="BUTTON",font=('Comic Sans MS',10,'bold'),borderwidth=6,relief=SUNKEN)
l.grid(row=0,column=1,pady=1)
l = Label(f3,text="GPIO PIN STATUS ",font=('Comic Sans MS',15,'bold'),borderwidth=6,relief=SUNKEN)
l.grid(row=0,column=0,pady=1)
#this code content the number of button
#this line can be use. if you want to show all the
#button in initial condition then you can use
'''
l2=Button(f2,text="GPIO-1",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO1(counter,1))
l2.grid(row=1,column=1,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-3",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO3(counter2,1))
l2.grid(row=2,column=1,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-5",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO5(counter4,1))
l2.grid(row=3,column=1,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-7",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO7(counter6,1))
l2.grid(row=4,column=1,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-9",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO9(counter8,1))
l2.grid(row=5,column=1,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-11",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO11(counter10,1))
l2.grid(row=6,column=1,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-2",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO2(counter1,1))
l2.grid(row=1,column=3,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-4",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO4(counter3,1))
l2.grid(row=2,column=3,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-6",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO6(counter5,1))
l2.grid(row=3,column=3,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-8",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO8(counter7,1))
l2.grid(row=4,column=3,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-10",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO10(counter9,1))
l2.grid(row=5,column=3,ipadx=15,ipady=5,padx=10,pady=7)

l2=Button(f2,text="GPIO-12",bg="#ffaa12",font=('Comic Sans MS',20,'bold'),borderwidth=6,relief=SUNKEN,command=lambda :GPIO12(counter11,1))
l2.grid(row=6,column=3,ipadx=15,ipady=5,padx=10,pady=7)'''
#button
root.mainloop()
