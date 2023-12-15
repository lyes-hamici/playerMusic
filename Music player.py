import tkinter as tk
from tkinter import *
from pygame import mixer
import os
import fnmatch



canvas = tk.Tk()
canvas.title("Lecteur musique LH")
canvas.geometry("500x500")
canvas.config(bg='grey')


rootpath = "C:\\playerMusic\music"
pattern = "*.mp3"

mixer.init()

prec_img = tk.PhotoImage(file="img/prev.png")

stop_img = tk.PhotoImage(file="img/stop.png")

play_img = tk.PhotoImage(file="img/play.png")

suiv_img = tk.PhotoImage(file="img/next.png")

pause_img = tk.PhotoImage(file="img/pause.png")

loop_img = tk.PhotoImage(file="img/music3.png")


def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath +"\\"+ listbox.get("anchor"))
    mixer.music.play()
    mixer.music.set_volume(vol.get()) #À chaque action (appuyer sur un bouton) le volume s'actualisera au volume défini.Le volume ne change pas en temps réel.

vol = Scale(
    canvas,
    from_ = 0,
    to = 1,
    orient = HORIZONTAL ,
    resolution = .1,
)
vol.pack(padx=20,pady=20)

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def next():
    next_song = listbox.curselection()

    next_song = next_song[0] + 1

    next_song_name = listbox.get(next_song)

    label.config(text=next_song_name)

    mixer.music.load(rootpath +"\\"+ next_song_name)

    mixer.music.play()

    listbox.select_clear(0,'end')

    listbox.activate(next_song)

    listbox.select_set(next_song)
    mixer.music.set_volume(vol.get())


def last():
    last_song = listbox.curselection()

    last_song = last_song[0] - 1

    last_song_name = listbox.get(last_song)

    label.config(text=last_song_name)

    mixer.music.load(rootpath +"\\"+ last_song_name)

    mixer.music.play()

    listbox.select_clear(0,'end')

    listbox.activate(last_song)

    listbox.select_set(last_song)
    mixer.music.set_volume(vol.get())



def pause():

    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"

    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"
    mixer.music.set_volume(vol.get())

mixer.music.set_volume(vol.get())


def loop():

    label.config(text=listbox.get("anchor")) 
    mixer.music.load(rootpath +"\\"+ listbox.get("anchor"))
    mixer.music.play(-1)
    mixer.music.set_volume(vol.get())
    






listbox = tk.Listbox(canvas, fg="white",bg="black",width=100,font=('Arial',14))
listbox.pack(padx=15,pady=15)



label = tk.Label(canvas,text="",bg='white',fg='black',font=('Arial',18))
label.pack(pady=15)



top = tk.Frame(canvas,bg='gray')
top.pack(padx=10,pady=5, anchor="center")



prescButton = tk.Button(canvas,text="presc",image=prec_img,bg='white',borderwidth=0,command=last)
prescButton.pack(pady=15, in_=top,side="left")



stopButton = tk.Button(canvas,text="stop" , image=stop_img,bg='white',borderwidth=0,command=stop)
stopButton.pack(pady=15,in_=top,side="left")



playButton = tk.Button(canvas,text="play",image=play_img,bg='white',borderwidth=0,command=select)
playButton.pack(pady=15, in_=top,side="left")



pauseButton = tk.Button(canvas,text="pause",image=pause_img,bg='white',borderwidth=0,command=pause)
pauseButton.pack(pady=15,in_=top,side="left")



suivButton = tk.Button(canvas,text="suivant",image=suiv_img,bg='white',borderwidth=0,command=next)
suivButton.pack(pady=15, in_=top,side="left")



loopButton = tk.Button(canvas,text="loop",image=loop_img,bg='white',borderwidth=0,command=loop)
loopButton.pack(pady=15, in_=top,side="left")


for root , dir , files in os.walk(rootpath):
    for filesnames in fnmatch.filter(files,pattern):

        listbox.insert('end',filesnames)

canvas.mainloop()