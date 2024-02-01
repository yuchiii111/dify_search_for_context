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


    def keyword_search(query: str, k: int = 4, texts: list[Document]) -> List[str]:
        _keyword_search = KeywordTableIndex()
        keywordtable = _keyword_search.create_keyword_table(texts)
        _keyword_search._retrieve_ids_by_query(keyword_table, query, k)
        
        results = [
            "doc_id",
            "doc_id",
            # ... 其他结果
        ]
        return results
