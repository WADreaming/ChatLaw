from PyPDF2 import PdfReader
from text2vec import SentenceModel, semantic_search
import numpy as np

class similarity_search():
    def __init__(self, ):

        self.model = SentenceModel('shibing624/text2vec-base-chinese')
        self.result = ""

    def text(self,path):
        reader = PdfReader(path)
        number_of_pages = len(reader.pages)
        tex = []

        for i in range(number_of_pages):
            xxx = reader.pages[i].extract_text()
            xxxx = xxx.split("\n")

            for k in xxxx:
                tex.append(k)

        return tex

    def query_embedding(self, query):

        query_embeddings = self.model.encode([query])

        return query_embeddings

    def search(self, file_path,embedding_path, query, left=10, right=10):

        #读取文本
        tex_pager=self.text(file_path)

        #导入向量
        tex_embeddings = np.load(embedding_path)
        query_embeddings=self.query_embedding(query)

        #计算相似度
        hits = semantic_search(query_embeddings, tex_embeddings)

        #循环提取
        for i in hits[0]:
            #print(i)

            #匹配文本
            stex = tex_pager[int(i['corpus_id']) - left:int(i['corpus_id']) + right]

            for st in stex:
                self.result=self.result+st
        #print(self.result)

