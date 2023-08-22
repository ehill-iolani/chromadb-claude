
# importing required modules
from PyPDF2 import PdfReader
import os

# path of the PDF file
path = "./pdfs/"
dir_list = os.listdir(path)

# convert all files in the pdfs directory to text
for file in dir_list:
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
