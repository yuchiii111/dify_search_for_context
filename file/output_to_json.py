from search.hy_search import search
from search.vector.embed import embed
from search.keyword.keyword_search import KeywordTableIndex
import pandas as pd
import json
from langchain.document_loaders import TextLoader,CSVLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter


loader1 = CSVLoader(file_path='')
loader2 = CSVLoader(file_path='')
loader3 = PyPDFLoader(file_path='')
loader4 = TextLoader(file_path='')
query_csv_file_path = " "
dataset_json_file_path = ""

doc1 = loader1.load()
doc2 = loader2.load()
doc3 = loader3.load()
doc4 = loader4.load()

# 处理pdf
for pdf_id in range(1,len(doc3))
    doc3[0].page_content = doc3[0].page_content+doc3[pdf_id].page_content
    doc3.pop(pdf_id)

def load_split(documents):
    text_splitter = CharacterTextSplitter(separator="/n/n",chunk_overlap=0)
    documents = text_splitter.split_documents(documents)
    return documents

base_doc = []
for doc_sp in [doc1,doc2,doc3,doc4]:
    sp_doc = load_split(doc_sp).
    base_doc.extend(sp_doc)

for doc_id, doc_seg in enumerate(base_doc):
        doc_seg["metadata"].clear()
        doc_seg["metadata"]["doc_id"] = doc_id + 1    


vec_embed = embed()
doc_embed = [doc.page_content for doc in base_doc]
embeddings = vec_embed.embedding_documents(doc_embed)

keyword_search = KeywordTableIndex(base_doc)
keywtab = keyword_search.create_keyword_table()

df = pd.read_csv(query_csv_file_path, encoding='utf-8')
query_list = df.['FAQ问题'].tolist()
answer_list = df.['FAQ回答'].tolist()

run_search = search()
data = []
final_context = []
for i, query in enumerate(query_list):
    final_doc = run_search.hybrid_search(query, base_doc, embeddings, keywtab)
    context_list = [doc.page_content for doc in final_doc]
    dataset_ = {
        'answers': answer_list[i],
        'context': context_list,
        'id': i+1,
        'question': query,
    }
    data.append(dataset_)

with open(dataset_json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
    

