from PyPDF2 import PdfReader
from text2vec import SentenceModel

model = SentenceModel('shibing624/text2vec-base-chinese')


def text(path):
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
    tex = []

    for i in range(number_of_pages):
        xxx = reader.pages[i].extract_text()
        xxxx = xxx.split("\n")

        for k in xxxx:
                tex.append(k)

    return tex

def text_embedding(query):

    text_embeddings = model.encode(query)

    return text_embeddings

