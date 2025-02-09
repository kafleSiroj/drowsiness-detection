import tkinter as tk
import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
from model import model
import numpy as np 

app = tk.Tk()
app.geometry("600x600")
app.title("Dectector")
ctk.set_appearance_mode('dark')

vidF = tk.Frame(height=480, width=600)
vidF.pack()
vid = ctk.CTkLabel(vidF)
vid.pack()


counter = 0 
counterLabel = ctk.CTkLabel(master=app, text=str(counter),  height=40, width=120, font=("Arial", 20), text_color="white", fg_color="teal")
counterLabel.pack(pady=10)

cap = cv2.VideoCapture(0)
def capture():
    global counter

    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)
    img = np.squeeze(results.render())

    if len(results.xywh[0])>0:
        dr_confidence = results.xywh[0][0][4].item()
        dr_class = results.xywh[0][0][5].item()

        if dr_confidence > 0.75 and dr_class == 1:
            counter += 1 
            print(counter)
        else:
            counter=0

    img_arr = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(img_arr)
    vid.imgtk = imgtk
    vid.configure(image=imgtk)
    vid.after(10, capture)
    counterLabel.configure(text=str(counter))



capture()

app.mainloop()
