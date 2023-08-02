import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import pafy
from random import sample
from time import sleep
from tkinter import *
from tkinter import messagebox

url = ""
n = 0
r = 0
player = None
video = None


window=Tk()
window.geometry("573x200")
window.title('Youtube Music Player')
window.iconbitmap('C:\\Users\\ASUS\\Downloads\\youtube.ico')

var1 = IntVar()
Checkbutton(window, text="Shuffle", variable=var1,onvalue = 1, offvalue = 0,activeforeground='red',activebackground='blue',selectcolor="yellow",font='Helvetica 10 bold').grid(row=6,column=2, sticky=W)
with open('SongsList.txt') as f:
    info = f.read()
songs = list(info.split('\n'))
print(songs)
#songs.pop()
num = len(songs)


def Prev():
    global r
    r -= 1
    Prabhas()
def Next():
    global r
    r += 1
    Prabhas()

def message(event=""):
    messagebox.showinfo("Info","Made by Prabhas")

def Prabhas():
    global player,video,window,v,songs,r,new_songs
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    if(r == 0):
        if(var1.get()):
            new_songs = sample(songs,len(songs))
        else:
            new_songs = songs
        b5['state'] = DISABLED
    if(r == len(songs) - 1):
        b4['state'] = DISABLED
    if(player != None):
        player.stop()
    player = None
    song = new_songs[r]
    v.set(song)
    sleep(1)
    start_reset()
    
    
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Playlists',menu=filemenu)
filemenu.add_command(label='Prabhas - '+ str(num) ,command=Prabhas)
helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='Creator',command=message)
helpmenu.add_separator()
helpmenu.add_command(label='Exit',command=window.quit)
    
def clip(event=""):
    global window,v
    v.set(window.clipboard_get())
    
def start_reset():
    global n,player,r
    n = 0
    if(player != None):
        player.stop()
    player = None
    start()
    
def volume(var):
    global player
    vol = v1.get()
    if(player != None):
        player.audio_set_volume(vol)
    
def start(event=""):
    global url,n,player,window,video,l6
    n += 1
    if(n == 1):
        url = e1.get()
        video = pafy.new(url)
        best = video.getbestaudio()
        playurl = best.url
        l5 = Label(window,text="Title : ").grid(row=2,column=0)
        l6 = Label(window,text=video.title).grid(row=2,column=1)
        b2['text'] = 'Pause or Play'
        b2['state'] = NORMAL
        v1['state'] = NORMAL
        v1.set(50)
        window.geometry("820x200")
        
        Instance = vlc.Instance("prefer-insecure")
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.audio_set_volume(50)
        player.play()
        
        
    elif(n % 2 == 0):
        b2['text'] = 'Resume'
        player.pause()
    else:
        b2['text'] = 'Pause'
        player.pause()
        

def submit(event = ""):
    global r
    r = 0
    b4['state'] = DISABLED
    b5['state'] = DISABLED
    start_reset()
        
window.bind('<space>',start)
window.bind('<Control-v>',clip)
window.bind('<Return>',submit)




l1=Label(window,text="MUSIC PLAYER",font="times 20",fg='red')
l1.grid(row=1,column=1)
l2 = Label(window,text = "Enter url : ")
l2.grid(row=3,column=0)
l3 = Label(window,text="Volume : ")
l3.grid(row=6,column=0)

v = StringVar()
e1=Entry(window,width=50,textvariable=v)
e1.grid(row=3,column=1)
b3=Button(window,text="Submit",command=submit,activeforeground='red',activebackground='blue', font='Helvetica 10 bold',width=10,cursor='hand2').grid(row=3,column=2)

b2=Button(window,text='Pause or Play',width=20,command=start,activeforeground='red',activebackground='blue',relief='ridge', font='Helvetica 10 bold',cursor='hand2',state=DISABLED)
b2.grid(row=5,column=1)

b3 = Button(window,text='Copy from Clipboard',command=clip,activeforeground='red',activebackground='blue',relief='ridge', font='Helvetica 10 bold',cursor='hand2')
b3.grid(row=5,column=2)

frame = Frame(window)
frame.grid(row=7,column=1)

b5 = Button(frame,text="Prev",command=Prev,activeforeground='red',activebackground='blue',relief='ridge', font='Helvetica 10 bold',cursor='hand2',state=DISABLED)

b4 = Button(frame,text="Next",command=Next,activeforeground='red',activebackground='blue',relief='ridge', font='Helvetica 10 bold',cursor='hand2',state=DISABLED)

b4.pack(side="right")
b5.pack(side="left")

v1 = Scale(window, from_=0, to=100, orient=HORIZONTAL,command=volume,length=200,activebackground='red',fg='green',troughcolor='blue',cursor='hand2')
v1.grid(row=6,column=1)
v1.set(50)
v1['state'] = DISABLED





l10 = Label(window,text='@Creator',fg='red',cursor='hand2')
l10.configure(font="Verdana 9 underline")
l10.grid(row=7,column=3)
l10.bind("<Button-1>", message )


window.mainloop()



