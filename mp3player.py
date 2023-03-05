from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
i = 0
root = Tk()
root.title('mp3player')
root.geometry("325x125")
backgroundc = ImageTk.PhotoImage(Image.open("background.png"))
icon1 = ImageTk.PhotoImage(Image.open("icon1.png"))
icon2 = ImageTk.PhotoImage(Image.open("icon2.png"))
icon3 = ImageTk.PhotoImage(Image.open("icon3.png"))
icon4 = ImageTk.PhotoImage(Image.open("icon4.png"))
file = ImageTk.PhotoImage(Image.open("file.png"))
icon = ImageTk.PhotoImage(Image.open("mediaplayer.ico"))
root.iconphoto(True, icon)
background = Label(root, image = backgroundc).place(x=0,y=0)
rights = messagebox.askokcancel("rights","this app was made for my learning")
if rights != 1:
        root.destroy()
        exit()
root.filename = filedialog.askopenfilename(initialdir="~/Documents", title='choose file', filetypes=(('music', '*.mp3'),))
filechanged = 0
filename = root.filename
def choose():
        global filename
        global filechanged
        root.filename = filedialog.askopenfilename(initialdir="~/Documents", title='choose file', filetypes=(('music', '*.mp3'),))
        filechanged = 1
        filename = root.filename
change = Button(root, image=file, bg = '#000000', command=choose).grid(row=0, column=0)
paused = 0
def mustart():
        global filename
        global paused
        global filechanged
        global i
        if filename:
                if filechanged == 1:
                        i=0
                        filechanged=0
                        paused=0
                if mixer.get_init() == 'None':
                        i = 0
                if i == 0:
                        mixer.init()
                        mixer.music.load(root.filename)
                        mixer.music.play(-1)
                        i = 1
                        paused=0
                        start = Button(root, image=icon2, bg = '#000000', command=mustart).grid(row=0, column=1)
                elif i != 0 and paused == 0:
                        mixer.music.pause()
                        paused=1
                        start = Button(root, image=icon1, bg = '#000000', command=mustart).grid(row=0, column=1)
                elif i != 0 and paused != 0:
                        mixer.music.unpause()
                        paused=0
                        start = Button(root, image=icon2, bg = '#000000', command=mustart).grid(row=0, column=1)
        else:
                response = messagebox.showwarning("error", "please choose a file")
start = Button(root, image=icon1, bg = '#000000', command=mustart).grid(row=0, column=1)
def musquit():
        global filename
        global paused
        global filechanged
        global i
        if filename:
                if i == 1:
                        mixer.music.unload()
                        mixer.quit()
                        i = 0
                        filechanged = 1
                        paused=1
                        start = Button(root, image=icon1, bg = '#000000', command=mustart).grid(row=0, column=1)
        else:
                response = messagebox.showwarning("error","please choose a file")
restart = Button(root, image=icon3, bg = '#000000', command=musquit).grid(row=1, column=1)
def stopp():
        root.destroy()
        mixer.quit()
bum = Button(root, image=icon4, bg = '#000000', command=stopp).grid(row=0, column=2)
root.mainloop()
