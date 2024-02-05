from search.keyword.keyword_search import KeywordTableIndex
from search.vector.vector_index import Vectorindex
from typing import List
from search.vector.embed import embed
from search.rerank import RerankRunner
from langchain.schema import Document



class search():
    def hybrid_search(self, query: str, document) -> List[str]:

        vector_results = self.vector_search(query, document)
        keyword_results = self.keyword_search(query, document)

        all_docs = self.uni_doc(vector_results, keyword_results)

        rerank_documents = self.rerank_doc(query, all_docs)

        return rerank_documents


    def keyword_search(self, query: str, texts: List[Document]) -> List[str]:

        _keyword_search = KeywordTableIndex(texts)
        keywordtable = _keyword_search.create_keyword_table()
        results = _keyword_search._retrieve_ids_by_query(keyword_table, query)    

        return results

    
    def vector_search(self, query, document)：
        vec_embed = embed()
        doc_embed = [doc.page_content for doc in document]
        embeddings = vec_embed.embedding_documents(doc_embed)

        Vectorsearch = Vectorindex(query,embeddings,document)
        document_vec = Vectorsearch.similarity_search_by_vector()
        
        return document_vec

    def uni_doc (self, doc1, doc2):
        new_doc = []
        new_doc.extend(doc1)
        ex_docid = [dc.metadata['doc_id'] for dc in doc1]
        for doc in doc2:
            if doc.metadata['doc_id'] not in ex_docid:
                new_doc.append(doc)
        
        return new_doc

    def rerank_doc(self, query, al_doc) ->List(Document) :
        
        rerank_runner = RerankRunner()
                      
        all_documents = rerank_runner.run(
            query=query,
            documents=al_doc,
            score_threshold=0.34,
            top_n=len(al_doc)
          # model="rerank-multilingual-v2.0"
            model="/home/yuhp/llm_models/all_models/rank_model/bge-reranker-base"
         )

        return all_documents


