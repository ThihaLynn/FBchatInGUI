import tkinter as tk
from tkinter import * 
from tkinter.ttk import *

def plus():
	numOfCmtLbel2.config(text =numOfCmtLbel2['text']+1)
def minus():
	numOfCmtLbel2.config(text= numOfCmtLbel2['text']-1)
from fbchat import Client
import fbchat
import time
def sub():
	client1= Client(userent.get(),passent.get())
	if client1.isLoggedIn():
		luuv = 1
		mess=coment.get("1.0","end")
		fbid =friendent.get()
		while luuv <= numOfCmtLbel2['text']:
			client1.send(fbchat.models.Message(mess),fbid )
			# if luuv%10 == 0:
			# 	time.sleep(10)  
			luuv+=1
root =tk.Tk()
wallpaper= tk.PhotoImage(file='D:\\PYthon GUI\\honey.png')
w = wallpaper.width()
h = wallpaper.height()
root.geometry("%dx%d+0+0" % (w, h))

panel1 = tk.Label(root, image=wallpaper,bg='black')
panel1.pack( fill='both',side =BOTTOM,)

panel1.image = wallpaper
down= tk.PhotoImage(file='arrow.png')
up  = tk.PhotoImage(file='up.png')


pane = Frame(root) 
root.title('Welcome TO FBChat <3!!!')
root.config(bg='black')
root.geometry('300x200')


userbut=tk.Label(root,text='Enter your Fb Phno Or Email :' ,compound='center',font=('Arials',13),bg='green' )
userent=tk.Entry(root, width=18,bg='white', font=('Arials',13))

passbut =tk.Label(root,text ='Enter  your  Fb  passw0rd  :',compound='center',font=('Arials',13),bg='green',width=25)
passent =tk.Entry(root, width=18,bg='white', font=('Arials',13),show='*')

friendbut=tk.Label(root,text='Enter your Friend\'s Profile id:' ,compound='center',font=('Arials',13),bg='green' )
friendent=tk.Entry(root, width=18,bg='white', font=('Arials',13))

combut= tk.Label(root,text='Enter your Message:' ,compound='center',font=('Arials',13),bg='green' )
coment= tk.Text(root, width=30,height=5,bg='white', font=('Arials',13))

numOfCmtLbel1= tk.Label(root,text='Number of Messages:' ,compound='center',font=('Arials',13),bg='green' )
numOfCmtBut1= tk.Button(root ,font=('Arials',15), image =up , command = plus)
numOfCmtLbel2= tk.Label(root,text=10 ,compound='center',font=('Arials',13),bg='green' )
numOfCmtBut2= tk.Button(root ,font=('Arials',15),image =down, command = minus)

submit = tk.Button(root , font=('Arials',15) ,text='Let\'s Go!!' ,command = sub)
userbut.pack(pady=10)
userent.pack()

passbut.pack(pady=10)
passent.pack()

friendbut.pack(pady=20)
friendent.pack()
combut.pack(pady=20)
coment.pack(side=TOP)
numOfCmtLbel1.pack()
numOfCmtBut1.pack()
numOfCmtLbel2.pack(pady=10)
numOfCmtBut2.pack()
submit.pack()



#client1= Client()


root.mainloop() 
