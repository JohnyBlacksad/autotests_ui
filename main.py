import re
from transliterate import translit

def ru_slug(text):
    text = translit(text, 'ru', reversed=True)
    text = re.sub(r'[^a-zA-Z0-9]+', '-', text)
    text = text.strip('-')
    return text.lower()
    
if __name__ == '__main__':
    pref = 'lil-solid-dual-'
    text = 'Где я могу найти обзор на lil SOLID DUAL?'
    print(pref + ru_slug(text))
    
    
