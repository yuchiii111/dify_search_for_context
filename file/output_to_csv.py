from search.hy_search import search
from search.vector.embed import embed
from search.keyword.keyword_search import KeywordTableIndex
import pandas as pd

loader1 = CSVLoader(file_path='')
loader2 = (file_path='')
loader3 = (file_path='')
loader4 = (file_path='')
doc1 = loader1.load()
doc2 = loader2.load()
doc3 = loader3.load()
doc4 = loader4.load()

vec_embed = embed()
doc_embed = [doc.page_content for doc in base_doc]
embeddings = vec_embed.embedding_documents(doc_embed)

keyword_search = KeywordTableIndex(base_doc)
keywtab = keyword_search.create_keyword_table()

csc_file_path = " "
df = pd.read_csv(csv_file_path, encoding='utf-8')
query_list = df.['FAQ问题'].tolist()

run_search = search()
final_context = []
for query in query_list：
    final_doc = run_search.hybrid_search(query, base_doc, embeddings, keywtab)
    final_context.append([doc.page_content for doc in final_doc])

df['context'] = final_context
df.to_csv(csv_file_pahth, index=False, encoding='utf-8')
    

