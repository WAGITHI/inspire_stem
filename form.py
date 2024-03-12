import tkinter as tk

def submit_form():
    # This function will handle what happens when the form is submitted
    # You can define what actions to take here

# Create a main window
 root= tk.Tk()

# Add widgets (like buttons, labels, entry fields) to the window
 label = tk.Label(root), text=("Enter your name:")
label.pack()

label = tk.Label(root), text=("Enter your ADM:")
label.pack()

label = tk.Label(root), text=("Enter your class:")
label.pack()

label = tk.Label(root), text=("Enter your phone number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root), text=("Submit"), command=submit_form
button.pack()

# Start the Tkinter event loop
root.mainloop()
