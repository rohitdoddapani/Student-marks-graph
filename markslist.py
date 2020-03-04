import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.figure import Figure
#from PIL import Image,ImageTk


flag=0

def view():
    global flag
    conn=sqlite3.connect('markslist.db')
    c=conn.cursor()
    name=name_text.get()
    regd=regd_no.get()
    xv=[]
    
    c.execute('SELECT * FROM marks WHERE name=? and regd=?',(name,regd))
    res=c.fetchall()
    if res:
        
        for row in res:
            print(row)
            for j in range(6):
                s=StringVar()
                b=Entry(window,textvariable=s,width=10)
                s.set(row[j])
                b.grid(row=5,column=j)
            flag=1
    else:
        messagebox.showerror('no record found','please enter a valid details')

    
    yv=[]
    xaxis=['I-1','I-2','II-1','II-2']
    for row in res:
        yv=[row[2],row[3],row[4],row[5]]
        
  
    fig=plt.figure(figsize=(4,4),dpi=70)
    fig.suptitle('performance Graph')
    #fig.add_subplot(111)
    plt.plot(xaxis,yv,linewidth=5)
    plt.xlabel('SEM')
    plt.ylabel('CGPA')
    #plt.xticks(xv,xaxis)
    plt.grid()

    canvas=FigureCanvasTkAgg(fig,master=window)
    canvas.draw()

    graph_widget=canvas.get_tk_widget()
    '''load=Image.open(fname)
    render=ImageTk.PhotoImage(load)
    img=Label(image=render)
    img.image=render
    img.grid(row=2,column=12)
    '''
    graph_widget.grid(row=1,column=8,columnspan=2,rowspan=18)






 
window=Tk()
window.title('marks')
window.geometry('800x400+30+30')
l1=Label(window,text='Name')
l1.grid(row=0,column=0,sticky=W)

l2=Label(window,text='regd No')
l2.grid(row=1,column=0,sticky=W)
'''####space labels
l1=Label(window,text=' ')
l1.grid(row=0,column=2)
'''
l1=Label(window,text='         ')
l1.grid(row=4,column=6)

l1=Label(window,text='                ')
l1.grid(row=3,column=0)
####

name_text=StringVar()
e1=Entry(window,textvariable=name_text,width=11)
e1.grid(row=0,column=1,sticky=W)

regd_no=StringVar()
e2=Entry(window,textvariable=regd_no,width=11)
e2.grid(row=1,column=1,sticky=W)

b1=ttk.Button(window,text='Submit',command=view,width=10)
b1.grid(row=2,column=1,sticky=W)

v0=StringVar()
en1=Entry(window,textvariable=v0,state='readonly',width=10)
v0.set('Name')
en1.grid(row=4,column=0)

v1=StringVar()
en2=Entry(window,textvariable=v1,state='readonly',width=10)
v1.set('Regd No')
en2.grid(row=4,column=1)

v2=StringVar()
en2=Entry(window,textvariable=v2,state='readonly',width=10)
v2.set('1-1')
en2.grid(row=4,column=2)

v3=StringVar()
en3=Entry(window,textvariable=v3,state='readonly',width=10)
v3.set('1-2')
en3.grid(row=4,column=3)

v4=StringVar()
en4=Entry(window,textvariable=v4,state='readonly',width=10)
v4.set('2-1')
en4.grid(row=4,column=4)

v5=StringVar()
en5=Entry(window,textvariable=v5,state='readonly',width=10)
v5.set('2-2')
en5.grid(row=4,column=5)

window.mainloop()
