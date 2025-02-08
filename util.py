import cv2
from PIL import Image, ImageTk
from model import model
import numpy as np 

cap = cv2.VideoCapture(0)
def capwindow(vid):
    def capture():
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model(frame)
        img = np.squeeze(results.render())

        img_arr = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(img_arr)
        vid.imgtk = imgtk
        vid.configure(image=imgtk)
        vid.after(10, capture)

    return capture