# Testing chromadb + claude

NOTE: I have included some of my papers about microhylid frog biogeography for testing so feel free to ask it questions about that as that is the information that it will be using in its persistent memory.

Please use either the native terminal/command line to run the commands.

To use this tool you must set up the following environment and install the required dependencies. Navigate to where you would like to clone the repostiory and input the following commands:
```
git clone https://github.com/ehill-iolani/chromadb-claude.git
python3 -m venv env
```

To activate the environment in Windows:
```
.\env\Scripts\activate
```

To activate the environment in Mac/Linux:
```
source env/bin/activate
```

Now that the environment is activate you can now install the required dependencies:
```
pip install -r requirements.txt
```

Open the .env file and add you Anthropic and OpenAI keys.

Once you have all of the dependencies installed you can first convert the .pdfs of interest into plain text by running `pdf2txt.py`
```
python pdf2txt.py
```

Once the pdfs have been converted to text, you can now run the `main.py` script to initiate the chat with Claude, the Anthropic AI.
```
python main.py
```

For reference what happens is we split the plain text into tokens/chunks and store them in our chroma database.
During the conversation, we first query the chromadb to find the top 20 most relevant "documents" relevant to your input which are then added to Claude's "working memory".