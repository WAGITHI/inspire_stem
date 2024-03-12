import tkinter as tk
def button_click():
    label.config(text="button Click Me")
window= tk.Tk()
window.title("Tkinter Window")
label=tk.Label(window, text="welcome to tkinter")
label.pack()
button=tk.Button(window, text="click me",command=button_click)
button.pack()
window.mainloop()