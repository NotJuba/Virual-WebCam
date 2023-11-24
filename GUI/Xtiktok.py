#!/usr/bin/env python3

import threading
import subprocess
import customtkinter
import random, time, sys
import platform
import tkinter




def choice_video():
    # here I want a function to open my files and let me choice the video and store it here so I can use to do a fake webcam
    #print("hey from the coice video")
    system_platform = platform.system()
    
    if system_platform == 'Darwin':  # macOS
        subprocess.run(['open', '-R'])
    elif system_platform == 'Windows':
        subprocess.run(['explorer', '/select,'])
    elif system_platform == 'Linux':
        subprocess.run(['xdg-open', '.'])

##    file_path = tkinter.filedialog.askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
##   if file_path:
##        selected_video_path = file_path
##        print(f"Selected video: {selected_video_path}")

def run_bot():
    pass


def start_bot():
    # Create a new thread to run the bot
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()


def close_it():
    sys.exit()


# ------------------------- > the GUI

app = customtkinter.CTk()
app.title("Mack und Lo+ GbR Camera program")
app.geometry("600x500")
app.grid_columnconfigure((0), weight=1)


def combobox_callback(choice):
    pass

label = customtkinter.CTkLabel(app,
   text="TikTok camera program",
   width=400,
   height=50,
   font=("Arial", 20, "bold"),
   justify="center",
   corner_radius=10
)



video_button = customtkinter.CTkButton(
    app,
    text="Choice an input video    <>" ,
    command=choice_video,
    width=400,
    height=50,
    font=("Arial", 20, "bold"),
    fg_color="red",
    hover_color="gray",
    hover=True,
    corner_radius=10
    )


combobox_apps = customtkinter.CTkComboBox(
    app,
    values=["Undetected"],
    command=combobox_callback,
    width=400,
    height=50,
    font=("Arial", 20, "bold"),
    dropdown_font=("Arial", 20, "bold"),
    hover=True,
    justify="center",
    corner_radius=10
)


button_start = customtkinter.CTkButton(
    app,
    text="Start",
    command=start_bot,
    width=100,
    height=30,
    corner_radius=8,
    hover_color="gray",
    hover=True,
    font=("Arial", 20, "bold"),
)

button_stop = customtkinter.CTkButton(
    app,
    text="Stop",
    command=close_it,
    width=100,
    height=30,
    corner_radius=8,
    hover_color="gray",
    hover=True,
    font=("Arial", 20, "bold"),
)

# --------------------------> packing

label.grid(row=1, column=0, padx=10, pady=40, sticky="nsew", columnspan=2)

#combobox_apps.grid(row=2, column=0, padx=40, pady=40, sticky="nsew", columnspan=2)
video_button.grid(row=2, column=0, padx=40, pady=40, sticky="nsew", columnspan=2)

button_start.grid(row=8, column=0, padx=40, pady=80, sticky="nsew")
button_stop.grid(row=8, column=1, padx=40, pady=80, sticky="nsew")

app.mainloop()

