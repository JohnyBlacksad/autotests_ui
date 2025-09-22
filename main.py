import re
from transliterate import translit

def ru_slug(text):
    text = translit(text, 'ru', reversed=True)
    text = re.sub(r'[^a-zA-Z0-9]+', '-', text)
    text = text.strip('-')
    return text.lower()

      

if __name__ == '__main__':
    pref = ''
    text = 'Чем lil SOLID DUAL отличается от lil HYBRID 3.0?'
    print(pref + ru_slug(text))
    
