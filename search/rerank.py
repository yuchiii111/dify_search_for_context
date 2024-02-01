from typing import List, Optional
from langchain.schema import Document
import cohere

api=?

class RerankRunner:

    def run(self, query: str, documents: List[Document], score_threshold: Optional[float] = None,
            top_n: Optional[int] = None, model ) -> List[Document]:

              
        docs = []
        doc_id = []
        unique_documents = []
        for document in documents:
            if document.metadata['doc_id'] not in doc_id:
                # 汇总所有需要排列的doc并去重
                doc_id.append(document.metadata['doc_id'])
                docs.append(document.page_content)
                unique_documents.append(document)

        api_key = ''
        co = cohere.Client(api_key)
        results = co.rerank(
            query=query,
            documents=docs,
            model=model,
            top_n=top_n
        )
        rerank_result
              
        "/home/yuhp/llm_models/all_models/rank_model/bge-reranker-base"

        rerank_documents = []
        for idx, result in enumerate(results):
            # format document
            rerank_document = RerankDocument(
                index=result.index,
                text=result.document['text'],
                score=result.relevance_score,
            )

            # score threshold check
            if score_threshold is not None:
                if result.relevance_score >= score_threshold:
                    rerank_documents.append(rerank_document)
            else:
                rerank_documents.append(rerank_document)

        return RerankResult(
            model=model,
            docs=rerank_documents
        )





        # 规范结果输出而已，后面先不看
        rerank_documents = []

        for result in rerank_result.docs:
            # format document
            rerank_document = Document(
                page_content=result.text,
                metadata={
                    "doc_id": documents[result.index].metadata['doc_id'],
                    "doc_hash": documents[result.index].metadata['doc_hash'],
                    "document_id": documents[result.index].metadata['document_id'],
                    "dataset_id": documents[result.index].metadata['dataset_id'],
                    'score': result.score
                }
            )
            rerank_documents.append(rerank_document)

        return rerank_documents -> list[doc, , ]
