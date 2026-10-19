import re, unicodedata
def normalize_question(text):
    text=unicodedata.normalize("NFKC",text).casefold().strip()
    text=re.sub(r"\s+"," ",text)
    return re.sub(r"[^\w\s]","",text)
