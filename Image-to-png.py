import tkinter as tk
import os,random
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
root =tk.Tk()
canvas=tk.Canvas(root,width=500,height=500)
canvas.grid(columnspan=3,rowspan=10)
#functions
def open_file():
    browse_text.set("loading....")
    global path
    path= filedialog.askopenfilename(parent=root,title='Choose a mp4 file',filetype=[("mp4 files","*.mp4")])
    if path:
        print(path)
        browse_text.set("Uploaded")
def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")  
def save_file():
    browse_text2.set("loading....")
    global path2
    path2=filedialog.askdirectory()
    if path2:
        path2=path2+"/"
        print(path2)
        browse_text2.set("Selected")
def convert_file():
    name = path.split("/")[-1].split(".")[0]
    save_path= os.path.join(path2, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(path)
    idx = 0

    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break
        cv2.imwrite(f"{save_path}/{idx}.png", frame)
        idx += 1
    convert_text.set("Converted")

#funnction to show random images on tkinter
def show_frame():
    name = path.split("/")[-1].split(".")[0]
    path3=path2+name
    random_filename = random.choice([x for x in os.listdir(path3) if os.path.isfile(os.path.join(path3, x))])
    path4=path3+"/"+random_filename
    img = tk.PhotoImage(file=path4)   
    img_label=tk.Label(image=img,bg="white")
    img_label.image=img
    img_label.grid(row=8,column=0,columnspan=2)
    return img_label
#logo
logo=Image.open("logo.png")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo,bg="#6cb0e0")
logo_label.image = logo
logo_label.grid(row=0,column=1)

#instructions
instructions=tk.Label(root,text="select the mp4 file to convert",font="Raleway")
instructions.grid(columnspan=3,column=0,row=1)

#browse button
browse_text=tk.StringVar()
browse_btn=tk.Button(root,textvariable=browse_text,font="Raleway",height=2,width=10,command=lambda:open_file())
browse_text.set("Browse")
browse_btn.grid(column=1,row=2)

#save button
instructions2=tk.Label(root,text="select where the png files should be saved",font="Raleway")
instructions2.grid(columnspan=3,column=0,row=3)

#browse button
browse_text2=tk.StringVar()
browse_btn2=tk.Button(root,textvariable=browse_text2,font="Raleway",height=2,width=10,command=lambda:save_file())
browse_text2.set("Browse")
browse_btn2.grid(column=1,row=4)

#convert button
convert_text=tk.StringVar()
convert_btn=tk.Button(root,textvariable=convert_text,font="Raleway",height=2,width=15,command=lambda:convert_file(),bg="#6cb0e0",fg="white")
convert_text.set("Convert")
convert_btn.grid(column=1,row=6)

#show button
show_text=tk.StringVar()
show_btn=tk.Button(root,textvariable=show_text,font="Raleway",height=2,width=25,command=lambda:show_frame(),bg="#6cb0e0",fg="white")
show_text.set("Show random images")
show_btn.grid(column=1,row=7)
root.mainloop()
