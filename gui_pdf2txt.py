import os
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog
from PyPDF2 import PdfReader

def choose_files():
    # open file dialog to choose PDF files
    files = filedialog.askopenfilenames(initialdir="./pdfs", title="Select PDF files", filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
    # update label to show selected files
    file_label.config(text=", ".join(files[:3]) + (", ..." if len(files) > 3 else ""))

def convert_to_text():
    # path of the PDF file
    path = "./pdfs/"
    dir_list = os.listdir(path)

    # convert all files in the pdfs directory to text
    for i, file in enumerate(dir_list):
        if file.endswith(".pdf"):
            # creating a pdf reader object
            reader = PdfReader(path+file)
            # save to a text file for later use
            # copy the path where the script and pdf is placed
            with open('./text/'+file[:-4]+'.txt', 'w', encoding='utf-8') as f:
                for page in reader.pages:
                    text = page.extract_text()
                    f.write(text)

    # concatenate all text files into one
    ptxt = "./text/"
    dir_list = os.listdir(ptxt)

    with open('./text/database.txt', 'w', encoding='utf-8') as f:
        for file in dir_list:
            if file.endswith(".txt"):
                with open(ptxt+file, 'r', encoding='utf-8') as f2:
                    f.write(f2.read())


# create the Tkinter window
root = Tk()
root.geometry("600x400") # set window size

# create a button to choose PDF files
choose_button = Button(root, text="Choose PDF Files", command=choose_files)
choose_button.pack(pady=10)

# create a label to show selected files
file_label = Label(root, text="")
file_label.pack(pady=5)

# create a button to run the script
convert_button = Button(root, text="Convert to Text", command=convert_to_text)
convert_button.pack(pady=10)

# run the Tkinter event loop
root.mainloop()