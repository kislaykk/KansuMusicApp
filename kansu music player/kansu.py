from tkinter import *
from tkinter import filedialog
import os
from pygame import mixer

root=Tk()
root.title("Kansu player")
root.geometry("300x150")
global songnumber
songnumber=0
def playlist(songnum):
    global song
    global songs
    song.grid_forget()
    global songnumber
    if songnumber+songnum==len(songs):songnumber=0
    elif songnumber+songnum==-1:songnumber=len(songs)-1
    else:songnumber=songnum+songnumber
    
    song=Label(root,text=songs[songnumber])
    song.grid(row=1,column=1)
    playSong()
    
def getMp3FromFolder():
    global songpath
    global songs
    
    global songnumber
    root.filename=filedialog.askopenfilename(initialdir="C:/" ,title="select a file",filetypes=(("mp3 files","*.mp3"),("all files","*.*")))
    
    path=root.filename[:root.filename.rfind("/")]
    songpath=[root.filename]
    for songe in os.listdir(path):
        if path+"/"+songe!=root.filename:songpath.append(path+"/"+songe)

    songs=[root.filename[root.filename.rfind("/")+1:]]
    for songe in os.listdir(path):
        if songe!=root.filename[root.filename.rfind("/")+1:]:songs.append(songe)
    songnumber=0
    playlist(0)

def resumeSong():
    mixer.music.unpause()
    global play
    play.grid_forget()
    play=Button(root,text="pause",command=pauseSong,anchor=W,fg="white",bg="#ff0033")
    play.grid(row=4,column=0)

def playSong():
    global songnumber
    global songpath
    global play
    
    

    try:
        mixer.init()
        
        mixer.music.load(songpath[songnumber])
        mixer.music.play(-1)
    except:
        playlist(1)
    
    play.grid_forget()
    play=Button(root,text="pause",command=pauseSong,anchor=W,fg="white",bg="#ff0033")
    play.grid(row=4,column=0)


def pauseSong():
    global play
    mixer.music.pause()
    play.grid_forget()
    play=Button(root,text="play",command=resumeSong,anchor=W,fg="white",bg="#ff0033")
    play.grid(row=4,column=0)

folder=Button(root,text="select song",command=getMp3FromFolder,anchor=W,fg="white",bg="#ff0033")


#####creating buttons and labels and sliders #####
musicLabel=Label(root,text="song:",anchor=W)
global song
global play

song=Label(root,text="--",anchor=E)

back=Button(root,text="<<",command=lambda:playlist(-1),anchor=W,fg="white",bg="#ff0033")
play=Button(root,text="play",state=DISABLED,anchor=W,fg="white",bg="#ff0033")
next=Button(root,text=">>",command=lambda:playlist(1),anchor=W,fg="white",bg="#ff0033")


#####putting them on the window ########
folder.grid(row=0,column=0)
musicLabel.grid(row=1,column=0)
song.grid(row=1,column=1)
back.grid(row=3,column=0)
play.grid(row=4,column=0)
#pause.grid(row=5,column=0)
next.grid(row=5,column=0)



root.mainloop()