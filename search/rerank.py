from typing import List, Optional
from langchain.schema import Document
import cohere
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# 直接用了本地模型，没用cohere

class RerankRunner:

    def run(self, query: str, documents: List[Document], model, score_threshold: Optional[float] = None,
            top_n: Optional[int] = None) -> List[Document]:

              
        docs = []
        doc_id = []
        
        for document in documents:
            if document.metadata['doc_id'] not in doc_id:
                # 汇总所有需要排列的doc并去重
                doc_id.append(document.metadata['doc_id'])
                docs.append(document.page_content)
                
        
        # api_key = ''
        # co = cohere.Client(api_key)
        # results = co.rerank(
        #     query=query,
        #     documents=docs,
        #     model=model,
        #     top_n=top_n
        # )
        
        tokenizer = AutoTokenizer.from_pretrained(model)
        model_r = AutoModelForSequenceClassification.from_pretrained(model)
        model_r.eval()
                
        with torch.no_grad():
            inputs = tokenizer(docs, padding=True, truncation=True, return_tensors='pt', max_length=512)
            results = model_r(**inputs, return_dict=True).logits.view(-1, ).float()

       
        rerank_results = []
        for idx, result in enumerate(results.items):
            # format document
            rerank_result = RerankDocument(
                index=idx,
                text=result[0],
                score=result[1],
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
    
