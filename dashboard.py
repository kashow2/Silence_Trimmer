import tkinter as tk
from tkinter import *
from tkinter import filedialog

import subprocess
import ffmpeg
import pathlib
import os
from ffmpeg_trim import trim_silence

file_path = r"C:\Users\omark\PycharmProjects\Nalanda_Audio_Trim\AudioTrim_Classes.txt" #txt file with class settings

# Open the text file in read mode
with open(file_path, 'r') as file:
    # Load the data into a Python dictionary and execute code
    data = file.read()
    exec(data)

# Create the main window
root = tk.Tk()
root.title("Silence Trimming Tool")

# Create a label widget
label = tk.Label(root, text="Silence Trimming Tool", font=("Helvetica", 16, "bold"))
label.pack(side=TOP, padx=10, pady=10)  # Add padding around the label

# Create a label for the subtitle
subtitle_label = tk.Label(root, text="Please select the class you want to render audio for, the input folder ",
                          font=("Helvetica", 12))
subtitle_label.pack(pady=1)  # Add padding below the subtitle label

# Create a label for the subtitle
subtitle_label = tk.Label(root, text="containing the audio files and the output folder desired!",
                          font=("Helvetica", 12))
subtitle_label.pack(pady=1)  # Add padding below the subtitle label


directory = []
# Opens input folder dialog button
def open_input_folder_dialog():
    folder_path = filedialog.askdirectory()
    quick_name = folder_path.split('/')
    if folder_path:
        input_folder_label.config(text=f"Input Folder: ...\\{quick_name[-1]}")
    else:
        input_folder_label.config(text="No folder selected")
    directory.append(folder_path.replace("/", "\\"))

# Input folder selection dialog button
input_button = tk.Button(root, text="Browse Input Audio Folder", command=open_input_folder_dialog)
input_button.pack(side=LEFT)

# Label to display the selected input folder path
input_folder_label = tk.Label(root, text="")
input_folder_label.pack(side=LEFT, pady=50)


directory_out = []
# Opens output folder selection dialog
def open_output_folder_dialog():
    folder_path = filedialog.askdirectory()
    quick_name = folder_path.split('/')
    if folder_path:
        output_folder_label.config(text=f"Output Folder:...\\{quick_name[-1]}")
    else:
        output_folder_label.config(text="No folder selected")
    directory_out.append(folder_path.replace("/", "\\"))

# Output folder selection dialog button
output_button = tk.Button(root, text="Browse Output Audio Folder", command=open_output_folder_dialog)
output_button.pack(side=RIGHT)

# Label to display the selected output folder path
output_folder_label = tk.Label(root, text="")
output_folder_label.pack(side=RIGHT, pady=50)


# Options for the dropdown menu
options = []
for course in nested_classes:
    options.append(course)

# Variable to store the selected option
selected_var = tk.StringVar()
selected_var.set(options[0])  # Default selected option

# Create the dropdown menu
dropdown_menu = tk.OptionMenu(root, selected_var, *options)
dropdown_menu.pack(pady=10)


# Last audio render button
def render_button_click():
    trim_silence(directory[-1], directory_out[-1], selected_var.get())
    label.config(text="Audio Rendered!")

# Create the Render Audio button widget
button = tk.Button(root, text="Render Audio", fg='red', font=("Arial", 10, "bold"), command=render_button_click)
button.pack(side=BOTTOM)

# Run the main loop
root.mainloop()
