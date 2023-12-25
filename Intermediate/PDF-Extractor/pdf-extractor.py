from collections import Counter
from PyPDF2 import PdfReader
import re

def pdf_extract(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict = False)
    
        # Extract text from each page
        print(f'Pages: {len(reader.pages)}')
        print('-' * 10)

        #Extract Text
        txt = [page.extract_text() for page in reader.pages]
        return txt
    
def word_count(txt: str):
    list_words = []
    for word in txt:
        split_text = re.split(r'\s+|[,;?!.-]\s*', word.lower())
    
        list_words += [word for word in split_text if word]
    return Counter(list_words)
    
def main():
    extracted_text = pdf_extract('sample.pdf')
    word_counter = word_count(extracted_text)

    for word, mentions in word_counter.most_common(5):
        print(f'{word:10}: {mentions}')

if __name__ == '__main__':
    main()