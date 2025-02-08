import tkinter as tk
import customtkinter as ctk
from util import capwindow


app = tk.Tk()
app.geometry("600x600")
app.title("Dectector")
ctk.set_appearance_mode('dark')

vidF = tk.Frame(height=600, width=600)
vidF.pack()
vid = ctk.CTkLabel(vidF)
vid.pack()



window = capwindow(vid)
window()
app.mainloop()