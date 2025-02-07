import re

def clean_text(dict):
    text = dict['content']
    text = text.strip()  # Remove leading/trailing whitespace
    text = re.sub(r'\n+', '\n', text)  # Remove redundant newlines
    return text
