from search.hy_search import search
from search.vector.embed import embed
from search.keyword.keyword_search import KeywordTableIndex

loader1 = CSVLoader(file_path='')
loader2 = ()
loader3 = ()
loader4 = ()
doc1 = loader1.load()
doc2 = loader2.load()
doc3 = loader3.load()
doc4 = loader4.load()
run_search = search()
vec_embed = embed()
doc_embed = [doc.page_content for doc in base_doc]
embeddings = vec_embed.embedding_documents(doc_embed)
keyword_search = KeywordTableIndex(base_doc)
keywtab = keyword_search.create_keyword_table()

for query in query_doc：
    run_search.hybrid_search(query, base_doc, embeddings, keywtab)
    
def ouput_file():
