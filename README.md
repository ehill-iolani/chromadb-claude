# Testing chromadb + claude

To use this tool you must set up the following environment and install the required dependencies. Navigate to where you would like to clone the repostiory and input the following commands:
```
git clone https://github.com/ehill-iolani/chromadb-claude.git
python3 -m venv env
# For Windows:
.\env\Scripts\activate
# For Mac/Linux:
source env/bin/activate
pip install -r requirements.txt
```

Once you have all of the dependencies installed you can first convert the .pdfs of interest into plain text by running `pdf2txt.py`
```
python pdf2txt.py
```

Once the pdfs have been converted to text, you can now run the `main.py` script to initiate the chat with the Claude, the Anthropic AI.
```
python main.py
```

For reference what happens is we split the plain text into tokens/chunks and store them in our chroma database.
During the conversation, we first query the chromadb to find the top 20 most relevant "documents" relevant to your input which are then added to Claude's "working memory".