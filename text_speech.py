import tkinter as tk
from tkinter import filedialog
import pyttsx3

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            text_to_speech(text)

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
    engine.setProperty('volume', 1.0)  # Adjust the volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

root = tk.Tk()
root.title("Document Reader")

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

root.mainloop()
