import tkinter as tk
import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import numpy as np
from model import model
from util import motor_off, motor_on

app = tk.Tk()
app.geometry("600x600")
app.title("Dectector")
ctk.set_appearance_mode('dark')

vidF = tk.Frame(height=480, width=600)
vidF.pack() 
vid = ctk.CTkLabel(vidF)
vid.pack()


counter = 0 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
def capture():
    global counter

    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)
    img = np.squeeze(results.render())
    motor_on()

    if len(results.xywh[0])>0:
        dr_class = results.xywh[0][0][5].item()
        if dr_class in [1,2]:
            counter += 1 
            print(counter)

            if counter >= 5:
                motor_off()
        else:
            counter = 0
            motor_on()
            
    img_arr = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(img_arr)
    vid.imgtk = imgtk
    vid.configure(image=imgtk)
    vid.after(10, capture)
    

capture()
app.mainloop()
