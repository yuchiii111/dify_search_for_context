from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
# from langchain.vectorstores import Chroma
# import numpy as np
from typing import List

class embed:
    def embedding_query(self, text) -> List[float]:
        model_name = "BAAI/bge-Large-zh"
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        hf = HuggingFaceBgeEmbeddings(
                        model_name=model_name,
                        model_kwargs=model_kwargs,
                        encode_kwargs=encode_kwargs,
                        query_instruction="为文本生成向量表示用于文本检索"
                    )
        text_embeddings = hf.embed_query(text)
        return text_embeddings

    def embedding_documents(self, documents: List[str]) -> List[List[float]]:
        model_name = "BAAI/bge-Large-zh"
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        hf = HuggingFaceBgeEmbeddings(
                        model_name=model_name,
                        model_kwargs=model_kwargs,
                        encode_kwargs=encode_kwargs,
                        query_instruction="为文本生成向量表示用于文本检索"
                    )
        embedding_result_ = hf.embed_documents(document)
        return embedding_result_
            

# class embed:
#     def embedding_query(self, text) -> List[float]:
#         model_name = "BAAI/bge-Large-zh"
#         model_kwargs = {'device': 'cpu'}
#         encode_kwargs = {'normalize_embeddings': True}
#         model = HuggingFaceBgeEmbeddings(
#                         model_name=model_name,
#                         model_kwargs=model_kwargs,
#                         encode_kwargs=encode_kwargs,
#                         query_instruction="为文本生成向量表示用于文本检索"
#                     )
#         embedding_result = model.ivoke_text_embedding(texts=text)
        

        
#         text_embeddings = self.norm_embedding(embedding_result.embeddings)
#         return text_embeddings

#     def norm_embedding(self, embeddings) -> List[float]:
#         text_embeddings = []
#          for vector in embeddings:
#             normalized_embedding = (vector / np.linalg.norm(vector)).tolist()
#             text_embeddings.append(normalized_embedding)
#          return text_embeddings

#     def embedding_documents(self, documents) -> List[List[float]]:
#         embedding_result_ = []
#         for i in range(0, len(texts)):
#             batch_texts = documents[i:i + 1]      
#             embedding_result_.append(self.embedding_query(batch_texts)) 
#         return embedding_result_
            
