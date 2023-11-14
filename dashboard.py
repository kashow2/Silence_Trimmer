import tkinter as tk
from tkinter import *
from tkinter import filedialog

import subprocess
import ffmpeg
import pathlib
import os
from ffmpeg_trim import trim_silence

import datetime
import time
import json

file_path = r"C:\Users\omark\PycharmProjects\Silence_Trimmer\AudioTrim_Classes.txt"  # txt file with class settings

# Open the AudioTrim_Classes text file in read mode
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
subtitle_label = tk.Label(root, text="1. Select the class you want to render audio for.",
                          font=("Helvetica", 12))
subtitle_label.pack(pady=1)  # Add padding below the subtitle label

# Create a label for the subtitle
subtitle_label = tk.Label(root,
                          text='2. Browse for Input/Output folders & save settings OR Select saved folder settings.',
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
dropdown_menu_label = tk.Label(root, text="Class:")
dropdown_menu_label.pack(padx=5, pady=(15, 1))
dropdown_menu = tk.OptionMenu(root, selected_var, *options)
dropdown_menu.configure(fg="red")
dropdown_menu.pack(pady=(1, 10))

num = []


# Last audio render button
def render_button_click():
    if directory:  # if Browse Folders was utilized
        trim_silence(directory[-1], directory_out[-1], selected_var.get(), num)
    else:  # if Selected Settings were utilized
        selected_setting = app.get_selected_preferred_name()
        keys = list(selected_setting.keys())
        values = list(selected_setting.values())
        trim_silence(keys[0], values[0], selected_var.get(), num)
    label.config(text="Audio Rendered!")

    # Creating a pop-up window
    popup_window = tk.Toplevel(root)
    popup_window.title("Render Done")
    popup_label = tk.Label(popup_window, text=f"{num} files rendered!", font=("Courier New", 16, "bold"))
    popup_label.pack()


# Create the Render Audio button widget
button = tk.Button(root, text="Render Audio", fg='red', font=("Arial", 10, "bold"), command=render_button_click)
button.pack(side=BOTTOM)


# Function to save settings to a JSON file
def save_settings_to_file(settings_dict):
    with open("settings.json", "w") as json_file:
        json.dump(settings_dict, json_file)


# Function to load settings from a JSON file
def load_settings_from_file():
    try:
        with open("settings.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {"Default": {"path": "none"}}


class SaveSettings(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Dictionary to store settings for each preferred name, default on first use
        self.settings = {"None": {"path": "None"}}

        # Load settings from file (if available)
        self.settings = load_settings_from_file()

        # Label for the Entry widget
        self.name_label = tk.Label(self, text="Enter Folder Settings Name:")
        self.name_label.pack(padx=10, pady=(5, 1))

        # Entry widget for user to enter the preferred name
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(padx=3, pady=(1, 5))

        # Create a button to save settings
        self.save_button = tk.Button(self, text="Save Settings", command=self.save_settings)
        self.save_button.pack(padx=10, pady=(1, 15))

        # Label for settings options dropdown menu
        self.preferred_name_label = tk.Label(self, text="Saved Settings:")
        self.preferred_name_label.pack(padx=10, pady=(10, 1))

        # Dropdown menu to select preferred name
        self.preferred_name_var = tk.StringVar()
        self.preferred_name_var.set(list(self.settings.keys())[0] if self.settings else "")
        self.preferred_name_menu = tk.OptionMenu(self, self.preferred_name_var, *self.settings.keys())
        self.preferred_name_menu.configure(fg="red")
        self.preferred_name_menu.pack(padx=3, pady=(1, 10))

    # Method to get the selected preferred name from outside the class
    def get_selected_preferred_name(self):
        name = self.preferred_name_var.get()
        return self.settings[name]

    def save_settings(self):
        # Get the user-entered preferred name
        preferred_name = self.name_entry.get()

        # Save the selected folder path to settings for the preferred name
        self.settings[preferred_name] = {directory[0]: directory_out[0]}

        # Update the dropdown menu with the new preferred name
        menu = self.preferred_name_menu["menu"]
        menu.delete(0, "end")
        for name in self.settings.keys():
            menu.add_command(label=name, command=lambda n=name: self.preferred_name_var.set(n))

        # Save settings to a JSON file
        save_settings_to_file(self.settings)
        print(f"Settings saved for {preferred_name}!")


if __name__ == "__main__":
    app = SaveSettings(master=root)  # Or pass your existing instance as master
    app.mainloop()

# Run the main loop
root.mainloop()
