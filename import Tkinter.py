from tkinter import * 

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('lmao')
tkWindow.geometry("400x350")
l = Text(tkWindow, height = 2, width = 20)

def red():
    l.delete('1.0', END)
    l.insert(END, "#ff1100")
def red_d():
    l.delete('1.0', END)
    l.insert(END, "#bd0e02")   
def yel():
    l.delete('1.0', END)
    l.insert(END, "#c6fc00")  
def w_g():
    l.delete('1.0', END)
    l.insert(END, "#5dfc00")  
def w_blue():
    l.delete('1.0', END)
    l.insert(END, "#00b1fc") 
def blue():
    l.delete('1.0', END)
    l.insert(END, "#000dfc") 
def pm():
    l.delete('1.0', END)
    l.insert(END, "#7600fc") 
  
button_red = Button(tkWindow, text = '', bg='#ff1100', fg='white', command=red, width=10, height=2)
button_d_red = Button(tkWindow, text = '', bg='#bd0e02', fg='white', command=red_d, width=10, height=2)
button_yel= Button(tkWindow, text = '', bg='#c6fc00', fg='white', command=yel, width=10, height=2)
button_w_g= Button(tkWindow, text = '', bg='#5dfc00', fg='white', command=w_g, width=10, height=2)
button_w_blue= Button(tkWindow, text = '', bg='#00b1fc', fg='white', command=w_blue, width=10, height=2)
button_blue= Button(tkWindow, text = '', bg='#000dfc', fg='white', command=blue, width=10, height=2)
button_pm= Button(tkWindow, text = '', bg='#7600fc', fg='white', command=pm, width=10, height=2)

button_red.pack()  
button_d_red.pack()
button_yel.pack()
button_w_g.pack()
button_w_blue.pack()
button_blue.pack()
button_pm.pack()
l.pack()
  
tkWindow.mainloop()