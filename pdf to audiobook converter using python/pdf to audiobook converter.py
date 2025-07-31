import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog
import pyttsx3
import time

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_audio(text, output_path, progress_label):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    progress_label.config(text="Conversion Complete!")

def convert(root, progress_label):
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_path:
        audio_path = 'output.mp3'

        text = pdf_to_text(pdf_path)

        start_time = time.time()

        progress_label.config(text="Converting...", fg="red")  # Set text color to red
        root.update()

        text_to_audio(text, audio_path, progress_label)

        end_time = time.time()
        elapsed_time = end_time - start_time

        progress_label.config(text=f"Conversion Complete! Time taken: {elapsed_time:.2f} seconds", fg="red")  # Set text color to red
        os.system(f'open {audio_path}')  # Opens the generated audio file

def main():
    root = tk.Tk()
    root.title("PDF to Audiobook Converter")
    root.geometry("800x600")
    root.configure(bg="black")

    button_font = ("Times New Roman", 30)
    convert_button = tk.Button(root, text="Convert PDF to Audiobook", command=lambda: convert(root, progress_label), font=button_font, bg="black", fg="red")
    convert_button.pack(padx=20, pady=20)

    progress_label = tk.Label(root, text="", font=("Times New Roman", 20), bg="black", fg="white")
    progress_label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()


