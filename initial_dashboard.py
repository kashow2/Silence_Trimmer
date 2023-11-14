import tkinter as tk
from tkinter import *
from tkinter import filedialog




# Create the main window
root = tk.Tk()
root.title("Silence Trimming Tool")

# Create a label widget
label = tk.Label(root, text="Silence Trimming Tool", font=("Helvetica", 16, "bold"))
label.pack(side=TOP, padx=10, pady=10)  # Add padding around the label

# Create a label for the subtitle
subtitle_label = tk.Label(root, text="Select the AudioTrim_Classes text file",
                          font=("Helvetica", 12))
subtitle_label.pack(pady=1)  # Add padding below the subtitle label

classes_path = []


# Opens input folder dialog button
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        input_file_label.config(text=f"File selected")
    else:
        input_file_label.config(text="No file selected")
    classes_path.append(file_path.replace("/", "\\"))


# Input folder selection dialog button
input_button = tk.Button(root, text="Browse", command=open_file_dialog)
input_button.pack(pady=10)

# Label to display the selected input folder path
input_file_label = tk.Label(root, text="")
input_file_label.pack(pady=20)

# Button to move to next dashboard
continue_button = tk.Button(root, text="Continue", command=lambda: true_dashboard(root))
continue_button.pack(side=BOTTOM, pady=10)



def true_dashboard(previous_window):
    previous_window.destroy()  # Close the previous window

    root = tk.Tk()
    root.title("Dashboard 2")

    # Dashboard 2 content
    tk.Label(root, text="Dashboard 2").pack()


    root.mainloop()


# Run the main loop
root.mainloop()
