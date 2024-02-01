from typing import List, Optional
from langchain.schema import Document
import cohere

# api=? 其他写完了

class RerankRunner:

    def run(self, query: str, documents: List[Document], score_threshold: Optional[float] = None,
            top_n: Optional[int] = None, model ) -> List[Document]:

              
        docs = []
        doc_id = []
        
        for document in documents:
            if document.metadata['doc_id'] not in doc_id:
                # 汇总所有需要排列的doc并去重
                doc_id.append(document.metadata['doc_id'])
                docs.append(document.page_content)
                

        api_key = ''
        co = cohere.Client(api_key)
        results = co.rerank(
            query=query,
            documents=docs,
            model=model,
            top_n=top_n
        )
       

        rerank_results = []
        for idx, result in enumerate(results):
            # format document
            rerank_result = RerankDocument(
                index=result.index,
                text=result.document['text'],
                score=result.relevance_score,
            )

            # score threshold check
            if score_threshold is not None:
                if result.relevance_score >= score_threshold:
                    rerank_results.append(rerank_result)
            else:
                rerank_results.append(rerank_result)

        # 规范结果输出
        rerank_documents = []

        for result in rerank_results:
            # format document
            rerank_document = Document(
                page_content=result.text,
                metadata={
                    "doc_id": documents[result.index].metadata['doc_id'],
                    "doc_hash": documents[result.index].metadata['doc_hash'],
                    "document_id": documents[result.index].metadata['document_id'],
                    'score': result.score
                }
            )
            rerank_documents.append(rerank_document)

        return rerank_documents 
        # -> list[doc, , ]
                
class RerankDocument:
    index: int
    text: str
    score: float
    
