import weaviate
from langchain.vectorstores import VectorStore
from search.rerank import RerankRunner

# model path ?

# 向量检索
class Vectorindex:
    def vec_sim():
        docs_with_similarity = vector_store.similarity_search_with_relevance_scores(
                                   query,
                                   search_kwargs={
                                       'k': top_k,
                                       'score_threshold': score_threshold,
                                       'filter': {
                                            'group_id': [dataset.id]
                                       }
                                   }
                               )
        docs = []
        for doc, similarity in docs_with_similarity:
            doc.metadata['score'] = similarity
            docs.append(doc)

        return docs
        # -> list[doc, ,]


