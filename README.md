## PDF to Audiobook Converter

### Introduction

The "PDF to Audiobook Converter" is a Python script that allows you to convert the text content of a PDF file into an audio file in the MP3 format. The script utilizes the PyPDF2 library to extract text from PDF pages and the pyttsx3 library to convert the extracted text into audio. The user interacts with the program through a graphical user interface (GUI) created using the tkinter library.

### Dependencies

Before running the script, you need to have the following dependencies installed:

- PyPDF2
- tkinter
- pyttsx3

You can install these dependencies using pip:

```bash
pip install PyPDF2
pip install pyttsx3
```

### How the Converter Works

1. The script starts by importing the required libraries: PyPDF2, os, tkinter, pyttsx3, and time.

2. The `pdf_to_text` function takes a PDF file path as input and uses PyPDF2 to extract text from each page of the PDF. The extracted text is then concatenated and returned as a single string.

3. The `text_to_audio` function takes text content, an output audio file path, and a progress label as input. It initializes the pyttsx3 text-to-speech engine, converts the text to audio, and saves it as an MP3 file at the specified output path. The `runAndWait` method is used to ensure that the audio generation process is completed before proceeding.

4. The `convert` function is the core of the script. It creates a GUI using tkinter where the user can select a PDF file to convert. Upon selecting a PDF file, the function triggers the conversion process.

5. Inside the `convert` function:
   - The user is prompted to select a PDF file using a file dialog.
   - The text content of the PDF is extracted using the `pdf_to_text` function.
   - The conversion process starts, and the progress label is updated to show the conversion status.
   - The `text_to_audio` function is called to convert the text to an MP3 audio file. The progress label is updated again to show the completion status and the time taken for the conversion.
   - The generated audio file is opened using the `os.system` function, which launches the default audio player.

6. The `main` function sets up the GUI for the PDF to Audiobook Converter application:
   - A tkinter window is created with a title, dimensions, and background color.
   - A "Convert PDF to Audiobook" button is added to the GUI, along with a font and color settings.
   - A progress label is added to display conversion status, and font and color settings are applied.

7. The script runs the `main` function when executed, launching the GUI application.

### How to Use

1. Make sure you have installed the required dependencies.
2. Run the script.
3. The GUI window will open with a "Convert PDF to Audiobook" button.
4. Click the button, and a file dialog will appear. Choose the PDF file you want to convert.
5. The conversion process will start, and the progress label will be updated to show the progress.
6. Once the conversion is complete, the progress label will show the completion status and the time taken.
7. The generated MP3 audio file will open in the default audio player.

### Conclusion

The "PDF to Audiobook Converter" script provides a simple and user-friendly way to convert the text content of PDF files into MP3 audio files. It utilizes PyPDF2 and pyttsx3 libraries to achieve this conversion and presents a graphical interface using tkinter for ease of use. This converter can be helpful for individuals who prefer listening to content rather than reading it.
