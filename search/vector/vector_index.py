import weaviate
from langchain.vectorstores import VectorStore
from search.rerank import RerankRunner
from typing import List
import pandas as pd
from search.vector.embed import embed
from langchain.docstore.document import Document

# 向量检索
class Vectorindex:
    
    def __init__(
        self, 
        query: str, 
        embeddings: List[List[float]], 
        document: List[str]
    ):
        
        self._client = weaviate.Client(url='http://localhost:8080')
        self.embed = embeddings
        self._doc = document
        self._query = query
        self.class_name = 'vec_sim'  # class的名字

        class_obj = {
            'class': class_name,         # class的名字
            'vectorIndexConfig':{
                'distance': 'l2-squared',   # 这里的distance是选择向量检索方式，这里选择的是欧式距离
             },
        }
        client.schema.create_class(class_obj)
    
    def import_data(self):
        data = {'documents':self._doc,
                'embedding':self.embed}
        df = pd.DataFrame(data)
        with client.batch(
            batch_size=100
        ) as batch:
            for i in range(document.shape[0]):
                # 定义properties
                properties = {
                    'doc_id': i+1,          
                    '_doc': df.documents[i],  
                }
                custom_vector = df.embedding[i] # 这里是句子向量化后的数据
        
                self._client.batch.add_data_object(
                    properties,
                    class_name=class_name,
                    vector=custom_vector
                )
    
    def similarity_search_by_vector(
        self, k: int = 4
    ) -> List[Document]:

        self.import_data()
        
        sim_embed = embed()
        query_embed = sim_embed.embedding_query(self._query)
        nearVector = {
            'vector': query_embed
        }
        query_obj=self._client.query.get(self.class_name, ['doc_id', '_doc'])
        result = query_obj.with_near_vector(nearVector).with_limit(k).with_additional(['distance']).do()

        if "errors" in result:
            raise ValueError(f"Error during query: {result['errors']}")

        docs = []
        for res in result["data"]["Get"][self.class_name]:
            doc = res.pop('_doc')
            ad = res.pop('_additional')
            docs.append(Document(page_content=text, metadata=res))
        return docs




