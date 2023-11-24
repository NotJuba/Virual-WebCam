#!/usr/bin/env python3

import threading
import subprocess
import customtkinter
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options as opt
import random, time, sys
from datetime import datetime


def get_bot():
    pass


def dismiss_alert(driver):
    pass


def intercart(active_element):
    pass


def go_through_picutre(active_element):
    pass


def swipe(active_element):
    pass


def close_match(driver):
    pass


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

combobox_apps.grid(row=2, column=0, padx=40, pady=40, sticky="nsew", columnspan=2)

button_start.grid(row=8, column=0, padx=40, pady=80, sticky="nsew")
button_stop.grid(row=8, column=1, padx=40, pady=80, sticky="nsew")

app.mainloop()

