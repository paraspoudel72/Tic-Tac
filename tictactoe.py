#importing modules and setting tittle, box size and color
from tkinter import *
import tkinter.messagebox
import random
root=Tk()
root.geometry("1350x750+0+0")
root.maxsize(width=1350, height=750)
root.minsize(width=1350, height=750)
root.configure(background="grey11")
Top=Frame(root, pady=2,width=1350, height=100, bg="cadet blue", relief=RIDGE)
Top.grid(row=0, column=0)
top_title=Label(Top, text="Advanced Tic Tac Toe Game", font=("arial", 25, "bold"), bd=21, bg="grey11", fg="mediumpurple4", justify=CENTER)
top_title.grid(row=0,column=0)
#for modes of paly
a=0
#deffining windows for different modes
def play():
	global a
	a=1
	Menuframe.grid_forget()
	exit.grid_forget()
	Play1.grid_forget()
	Play2.grid_forget()
	Mainframe.grid(row=1, column=0)
	LeftFrame.pack(side=LEFT)
	rightFrame.pack(side=RIGHT)
	right1.grid(row=0, column=0)
	right2.grid(row=1, column=0)

def play2():
	global a
	a=2
	Menuframe.grid_forget()
	Play1.grid_forget()
	exit.grid_forget()
	Play2.grid_forget()
	Mainframe.grid(row=1, column=0)
	LeftFrame.pack(side=LEFT)
	rightFrame.pack(side=RIGHT)
	right1.grid(row=0, column=0)
	right2.grid(row=1, column=0)
#for menu
Menuframe=Frame(root, width=1350, height=600, bg="grey11", relief=RIDGE)
Menuframe.grid(row=1, column=0)
Play1=Button(Menuframe, width=25, height=2, bg="grey11",fg="mediumpurple4", text="Play Human vs Human", font=("Times 26 bold"),command=play)
Play1.grid(row=0,column=0)
Play2=Button(Menuframe, width=25, height=2, bg="grey11",fg="mediumpurple4", text="Play Human vs Computer", font=("Times 26 bold"), command=play2)
Play2.grid(row=0, column=1)
exit=Button(Menuframe,text="Exit Game", font=("Times 26 bold"), bg="grey11",fg="mediumpurple4",width=25,height=2, command= quit)
exit.grid(row=1,column=0, columnspan=2)

#For menu inside modes
Mainframe=Frame(root,pady=2, width=1350, height=600, bg="powder Blue", relief=RIDGE)
LeftFrame=Frame(Mainframe, bd=10, width=750, height=500, pady=2, padx=10, bg="grey11", relief=RIDGE)
rightFrame=Frame(Mainframe, bd=10, width=560, height=500, pady=2, padx=10, bg="grey11", relief=RIDGE)
right1=Frame(rightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg="grey11", relief=RIDGE)
right2=Frame(rightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg="grey11", relief=RIDGE)
#for rset button
def reset():
	global winner
	global checkgame
	checkgame=True
	but1["text"]=""
	but2["text"]=""
	but3["text"]=""
	but4["text"]=""
	but5["text"]=""
	but6["text"]=""
	but7["text"]=""
	but8["text"]=""
	but9["text"]=""
	but1.configure(background="grey11", state=NORMAL)
	but2.configure(background="grey11", state=NORMAL)
	but3.configure(background="grey11", state=NORMAL)
	but4.configure(background="grey11", state=NORMAL)
	but5.configure(background="grey11", state=NORMAL)
	but6.configure(background="grey11", state=NORMAL)
	but7.configure(background="grey11", state=NORMAL)
	but8.configure(background="grey11", state=NORMAL)
	but9.configure(background="grey11", state=NORMAL)
	winner=False
#for new game button
def newgame():
	reset()
	PlayerX.set(0)
	PlayerO.set(0)
#for exit button
def exit1():
	global a
	Mainframe.grid_forget()
	LeftFrame.pack_forget()
	rightFrame.pack_forget()
	right1.grid_forget()
	right2.grid_forget()
	Menuframe.grid(row=1, column=0)
	exit.grid(row=1,column=0, columnspan=2)
	Play2.grid(row=0, column=1)
	Play1.grid(row=0,column=0)
	a=0
	but1["text"]=""
	but2["text"]=""
	but3["text"]=""
	but4["text"]=""
	but5["text"]=""
	but6["text"]=""
	but7["text"]=""
	but8["text"]=""
	but9["text"]=""
	but1.configure(background="grey11", state=NORMAL)
	but2.configure(background="grey11", state=NORMAL)
	but3.configure(background="grey11", state=NORMAL)
	but4.configure(background="grey11", state=NORMAL)
	but5.configure(background="grey11", state=NORMAL)
	but6.configure(background="grey11", state=NORMAL)
	but7.configure(background="grey11", state=NORMAL)
	but8.configure(background="grey11", state=NORMAL)
	but9.configure(background="grey11", state=NORMAL)
	PlayerX.set(0)
	PlayerO.set(0)
	global winner
	global checkgame
	checkgame=True
	winner=False

PlayerX=IntVar()
PlayerO=IntVar()
PlayerX.set(0)
PlayerO.set(0)
buttons= StringVar()
checker=True
winner=False

#function for score keeping and check for tie
def scorekeeper():
	global winner
	if but1["text"]==but2["text"]==but3["text"]!="" and winner==False:
		if but1["text"]=="X":
			n=int(PlayerX.get())
			PlayerX.set(n+1)
			but1.configure(background="green")
			but2.configure(background="green")
			but3.configure(background="green")
			winner=True
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player X")
		elif but1["text"]=="O":
			n=int(PlayerO.get())
			PlayerO.set(n+1)
			but1.configure(background="green")
			but2.configure(background="green")
			but3.configure(background="green")
			winner=True			
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player O")
		but4["state"]=DISABLED
		but5["state"]=DISABLED
		but6["state"]=DISABLED
		but7["state"]=DISABLED
		but8["state"]=DISABLED
		but9["state"]=DISABLED
	if but4["text"]==but5["text"]==but6["text"]!="" and winner==False:
		if but6["text"]=="X":
			n=int(PlayerX.get())
			PlayerX.set(n+1)
			but4.configure(background="green")
			but5.configure(background="green")
			but6.configure(background="green")	
			winner=True
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player X")
		elif but4["text"]=="O":
			n=int(PlayerO.get())
			PlayerO.set(n+1)
			but4.configure(background="green")
			but5.configure(background="green")
			but6.configure(background="green")	
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player O")
			winner=True
		but1["state"]=DISABLED
		but2["state"]=DISABLED
		but3["state"]=DISABLED
		but7["state"]=DISABLED
		but8["state"]=DISABLED
		but9["state"]=DISABLED
			
	if but7["text"]==but8["text"]==but9["text"]!="" and winner==False:
		if but8["text"]=="X":
			n=int(PlayerX.get())
			but7.configure(background="green")
			but8.configure(background="green")
			but9.configure(background="green")	
			PlayerX.set(n+1)
			winner=True
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player X")
		elif but7["text"]=="O":
			n=int(PlayerO.get())
			PlayerO.set(n+1)
			but7.configure(background="green")
			but8.configure(background="green")
			but9.configure(background="green")	
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player O")
			winner=True
		but4["state"]=DISABLED
		but5["state"]=DISABLED
		but6["state"]=DISABLED
		but1["state"]=DISABLED
		but2["state"]=DISABLED
		but3["state"]=DISABLED
	if but1["text"]==but4["text"]==but7["text"]!="" and winner==False:
		if but1["text"]=="X":
			n=int(PlayerX.get())
			PlayerX.set(n+1)
			but1.configure(background="green")
			but4.configure(background="green")
			but7.configure(background="green")	
			winner=True
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player X")
		elif but1["text"]=="O":
			n=int(PlayerO.get())
			PlayerO.set(n+1)
			but1.configure(background="green")
			but4.configure(background="green")
			but7.configure(background="green")	
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player O")
			winner=True
		but2["state"]=DISABLED
		but5["state"]=DISABLED
		but6["state"]=DISABLED
		but3["state"]=DISABLED
		but8["state"]=DISABLED
		but9["state"]=DISABLED
	if but2["text"]==but5["text"]==but8["text"]!="" and winner==False:
		if but5["text"]=="X":
			n=int(PlayerX.get())
			PlayerX.set(n+1)
			but2.configure(background="green")
			but5.configure(background="green")
			but8.configure(background="green")	
			winner=True
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player X")
		elif but2["text"]=="O":
			n=int(PlayerO.get())
			PlayerO.set(n+1)
			but2.configure(background="green")
			but5.configure(background="green")
			but8.configure(background="green")
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player O")
			winner=True
		but4["state"]=DISABLED
		but1["state"]=DISABLED
		but6["state"]=DISABLED
		but7["state"]=DISABLED
		but3["state"]=DISABLED
		but9["state"]=DISABLED
			
	if but3["text"]==but6["text"]==but9["text"]!="" and winner==False:
		if but3["text"]=="X":
			n=int(PlayerX.get())
			PlayerX.set(n+1)
			but3.configure(background="green")
			but6.configure(background="green")
			but9.configure(background="green")
			winner=True
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player X")
		elif but3["text"]=="O":
			n=int(PlayerO.get())
			PlayerO.set(n+1)
			but3.configure(background="green")
			but6.configure(background="green")
			but9.configure(background="green")
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player O")
			winner=True
		but4["state"]=DISABLED
		but5["state"]=DISABLED
		but1["state"]=DISABLED
		but7["state"]=DISABLED
		but8["state"]=DISABLED
		but2["state"]=DISABLED
			
	if but1["text"]==but5["text"]==but9["text"]!="" and winner==False:
		if but1["text"]=="X":
			n=int(PlayerX.get())
			PlayerX.set(n+1)
			but1.configure(background="green")
			but5.configure(background="green")
			but9.configure(background="green")
			winner=True
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player X")
		elif but1["text"]=="O":
			n=int(PlayerO.get())
			PlayerO.set(n+1)
			but1.configure(background="green")
			but5.configure(background="green")
			but9.configure(background="green")
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player O")
			winner=True
		but4["state"]=DISABLED
		but2["state"]=DISABLED
		but6["state"]=DISABLED
		but7["state"]=DISABLED
		but8["state"]=DISABLED
		but3["state"]=DISABLED
			
	if but3["text"]==but5["text"]==but7["text"]!="" and winner==False:
		if but3["text"]=="X":
			n=int(PlayerX.get())
			PlayerX.set(n+1)
			but3.configure(background="green")
			but5.configure(background="green")
			but7.configure(background="green")
			winner=True
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player X")
		elif but3["text"]=="O":
			n=int(PlayerO.get())
			PlayerO.set(n+1)
			but3.configure(background="green")
			but5.configure(background="green")
			but7.configure(background="green")
			winner=True
			tkinter.messagebox.showinfo("Yeah we got a winner","Winner is Player O")
		but4["state"]=DISABLED
		but1["state"]=DISABLED
		but6["state"]=DISABLED
		but2["state"]=DISABLED
		but8["state"]=DISABLED
		but9["state"]=DISABLED
checkgame=True
def checkgames():
	global checkgame
	if but1["text"]!= "" and but2["text"]!= "" and but3["text"]!= "" and but4["text"]!= "" and but5["text"]!= "" and but6["text"] != "" and but7["text"] != "" and but8["text"] != "" and but9["text"] != "":
		checkgame=False
#function for buttons on click
def click(buttons):
	global winner
	global checker
	global a
	if a==1:
		if buttons["text"]=="" and checker==True:
			buttons["text"]="X"
			checker=False
			scorekeeper()
			checkgames()
		elif buttons["text"]=="" and checker==False:
			buttons["text"]="O"
			checker=True
			scorekeeper()
			checkgames()
		if checkgame==False and winner==False:
			tkinter.messagebox.showinfo("Tie","There is a tie ")
	elif a==2:
		if buttons["text"]=="":
			buttons["text"]="X"
			scorekeeper()
			checkgames()
			if winner==False:
				list1=[but1,but2,but3,but4,but5,but6,but7,but8,but9]
				list2=[]
				for button in list1:
					if button["text"]=="":
						list2.append(button)
				try:
						random.choice(list2)["text"]="O"
						scorekeeper()
						checkgames()
				except:
						tkinter.messagebox.showinfo("Tie","There is a tie ")


	if checkgame==False and winner==False:
		tkinter.messagebox.showinfo("Tie","There is a tie ")

#buttons
but1=Button(LeftFrame, text="", font=("Times 26 bold"), height=3, width=8, bg="grey11",fg="mediumpurple4", command=lambda: click(but1))
but1.grid(row=1, column=0)
but2=Button(LeftFrame, text="", font=("Times 26 bold"), height=3, width=8, bg="grey11",fg="mediumpurple4", command=lambda: click(but2))
but2.grid(row=1, column=1)
but3=Button(LeftFrame, text="", font=("Times 26 bold"), height=3, width=8, bg="grey11",fg="mediumpurple4", command=lambda: click(but3))
but3.grid(row=1, column=2)
but4=Button(LeftFrame, text="", font=("Times 26 bold"), height=3, width=8, bg="grey11",fg="mediumpurple4", command=lambda: click(but4))
but4.grid(row=2, column=0)
but5=Button(LeftFrame, text="", font=("Times 26 bold"), height=3, width=8, bg="grey11",fg="mediumpurple4", command=lambda: click(but5))
but5.grid(row=2, column=1)
but6=Button(LeftFrame, text="", font=("Times 26 bold"), height=3, width=8, bg="grey11",fg="mediumpurple4", command=lambda: click(but6))
but6.grid(row=2, column=2)
but7=Button(LeftFrame, text="", font=("Times 26 bold"), height=3, width=8, bg="grey11",fg="mediumpurple4", command=lambda: click(but7))
but7.grid(row=3, column=0)
but8=Button(LeftFrame, text="", font=("Times 26 bold"), height=3, width=8, bg="grey11",fg="mediumpurple4", command=lambda: click(but8))
but8.grid(row=3, column=1)
but9=Button(LeftFrame, text="", font=("Times 26 bold"), height=3, width=8, bg="grey11",fg="mediumpurple4", command=lambda: click(but9))
but9.grid(row=3, column=2)
butt1=Button(right2, text="Reset", font=("Times 26 bold"), height=2, width=20, bg="grey11",fg="mediumpurple4", command=reset)
butt1.grid(row=0, column=0)
butt2=Button(right2, text="New Game", font=("Times 26 bold"), height=2, width=20, bg="grey11",fg="mediumpurple4", command=newgame)
butt2.grid(row=1, column=0)
butt3=Button(right2, text="Exit to menu", font=("Times 26 bold"), height=2, width=20, bg="grey11",fg="mediumpurple4", command=exit1)
butt3.grid(row=2,column=0)
#for score keeping
scorecard1=Label(right1, text="Player X : ", pady=2, padx=2, bg="grey11",fg="mediumpurple4", font=("arial 20 bold"))
scorecard1.grid(row=0, column=0, sticky=W+E)
forx=Entry(right1, font=("arial 20 bold"),bd=2,bg="grey11",fg="mediumpurple4", textvariable=PlayerX, width=14, justify=LEFT, state=DISABLED)
forx.grid(row=0, column=1)
scorecard2=Label(right1, text="Player O : ", pady=2, padx=2, bg="grey11",fg="mediumpurple4", font=("arial 20 bold"))
scorecard2.grid(row=1, column=0, sticky=W+E)
foro=Entry(right1, font=("arial 20 bold"),bd=2,bg="grey11",fg="mediumpurple4", textvariable=PlayerO, width=14, justify=LEFT, state= DISABLED)
foro.grid(row=1, column=1)

root.mainloop()