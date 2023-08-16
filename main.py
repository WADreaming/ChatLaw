import similarity_search as ss


file_path="law/civil_law.pdf"
embedding="embedding/civil_law_embedding.npy"
law_search=ss.similarity_search()

law_search.search(file_path,embedding,"法律制度与法律部门的关系是(  )。",10,10)

print(law_search.result)











