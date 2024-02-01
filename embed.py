from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Chroma
import numpy as np

def embedding(documents):
    text_embeddings = []
    model_name = "BAAI/bge-Large-zh"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}
    embeddings = HuggingFaceBgeEmbeddings(
                    model_name=model_name,
                    model_kwargs=model_kwargs,
                    encode_kwargs=encode_kwargs,
                    query_instruction="为文本生成向量表示用于文本检索"
                )

    for vector in embeddings:
        normalized_embedding = (vector / np.linalg.norm(vector)).tolist()
        text_embeddings.append(normalized_embedding)

    return text_embeddings

            for i in range(0, len(texts), max_chunks):
                batch_texts = texts[i:i + max_chunks]

                embedding_result = self._model_instance.invoke_text_embedding(
                    texts=batch_texts,
                    user=self._user
                )

                for vector in embedding_result.embeddings:
                    try:
                        normalized_embedding = (vector / np.linalg.norm(vector)).tolist()
                        text_embeddings.append(normalized_embedding)
            
