from search.keyword.keyword_search import KeywordTableIndex




class search():
    def hybrid_search(query: str, milvus_top_k: int = 5, keyword_top_k: int = 5, rerank_top_k: int = 10) -> List[str]:

        milvus_results = milvus_store.similarity_search(query, k=milvus_top_k)
        milvus_ids = [result.metadata['doc_id'] for result in milvus_results]

        keyword_results = keyword_search(query, k=keyword_top_k)
        keyword_ids = [result.metadata['doc_id'] for result in keyword_results]

        all_ids = set(milvus_ids + keyword_ids)

        rerank_documents = rerank_runner.run(query, documents=milvus_results + keyword_results, top_n=rerank_top_k)
        rerank_ids = [result.metadata['doc_id'] for result in rerank_documents]

        final_results = [result for result in rerank_documents if result.metadata['doc_id'] in all_ids][:rerank_top_k]

        return final_results


    def keyword_search(query: str, k: int = 5) -> List[str]:
        # 在实际应用中，这里可以使用您的关键词检索实现，返回检索结果

        # 此处仅为示例，返回一些虚构的结果
        results = [
            {"doc_id": "keyword_doc_1", "score": 0.8, "text": "Keyword result 1"},
            {"doc_id": "keyword_doc_2", "score": 0.7, "text": "Keyword result 2"},
            # ... 其他结果
        ]
        return results
