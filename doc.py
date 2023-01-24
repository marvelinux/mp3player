from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#import sqlite3
from PIL import ImageTk, Image
from pygame import mixer
i = 0
root = Tk()
root.title('linux')
root.geometry("325x225")
top = Toplevel()
imge = ImageTk.PhotoImage(Image.open("niji-ink.png"))
icon1 = ImageTk.PhotoImage(Image.open("icon1.png"))
icon2 = ImageTk.PhotoImage(Image.open("icon2.png"))
icon3 = ImageTk.PhotoImage(Image.open("icon3.png"))
icon4 = ImageTk.PhotoImage(Image.open("icon4.png"))
file = ImageTk.PhotoImage(Image.open("file.png"))
back = Label(top, image=imge).pack()
#def popup():
#	response = messagebox.askquestion("popup","kys kys kys kys kys kys kys kys kys kys ")
#	if response == 'yes':
#		t = Label(root, text=response).pack()
#	else:
#		t = Label(root, text='You idiot why did you click no').pack()
c = Label(text='test linux').grid(row=0, column=1)
root.filename = filedialog.askopenfilename(initialdir="~/Documents", title='choose file', filetypes=(('music', '*.mp3'),))
#button = Button(text='pop up!', command=popup).pack()
destroy = Button(text='destroy ink!sans', command=top.destroy).grid(row=1, column=1)
filechanged = 0
def choose():
	global filechanged
	root.filename = filedialog.askopenfilename(initialdir="~/Documents", title='choose file', filetypes=(('music', '*.mp3'),))
	filechanged = 1
change = Button(root, image=file, command=choose).grid(row=2, column=1)
#abel = Label(text=root.filename).pack()
def mustart():
	global filechanged
	global i
	if filechanged == 1:
		i=0
		filechanged=0
	if mixer.get_init() == 'None':
		i = 0
	if i == 0:
		mixer.init()
		mixer.music.load(root.filename)
		mixer.music.play()
		i = 1
	else:
		mixer.music.unpause()
start = Button(root, image=icon1, command=mustart).grid(row=3, column=1)
def mustop():
	global i
	if i != 0:
		mixer.music.pause()
def musquit():
	global filechanged
	global i
	if i == 1:
		mixer.stop()
		mixer.init()
		mixer.music.load(root.filename)
		mixer.music.play()
		i = 1
		filechanged = 0
	else:
		mixer.init()
		mixer.music.load(root.filename)
		mixer.music.play()
		i=1
		filechanged=0
stop = Button(root, image=icon2, command=mustop).grid(row=3, column=0)
quit = Button(root, image=icon3,command=musquit).grid(row=3, column=2)
bum = Button(root, image=icon4, command=root.destroy).grid(row=4, column=1)
root.mainloop()
