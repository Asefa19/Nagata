import re

def clean_text(dict):
    text = dict['content']
    text = text.strip()  # Remove leading/trailing whitespace
    text = re.sub(r'\n+', '\n', text)  # Remove redundant newlines
    return text

def filter_response(text):
    beginning = text.find("<<SYS>>")
    ending = text.find("<<SYS>>", text.find('<<SYS>>') + 1)
    llm_response = text[(beginning+7):(ending-8)]
    print(beginning, ending)
    print('response from filter:\n', llm_response)
    return llm_response