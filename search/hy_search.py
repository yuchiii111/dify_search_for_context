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

    
    class vector_search:
    def similarity_search(self, query: str, k: int = 5) -> List[str]:
        # 在实际应用中，这里可以使用 Milvus 进行向量相似度检索，返回检索结果
        # 此处仅为示例，返回一些虚构的结果
        results = [
            {"doc_id": "milvus_doc_1", "score": 0.9, "text": "Milvus result 1"},
            {"doc_id": "milvus_doc_2", "score": 0.85, "text": "Milvus result 2"},
            # ... 其他结果
        ]
        
        return results

        
         embedding_model = model_manager.get_model_instance(
                tenant_id=dataset.tenant_id,
                model_type=ModelType.TEXT_EMBEDDING,
                provider=dataset.embedding_model_provider,
                model=dataset.embedding_model
            )

            embeddings = CacheEmbedding(embedding_model)
            # 生成一个实例

            return WeaviateVectorIndex(
                dataset=dataset,
                config=current_app.config,
                embeddings=embeddings
            )
           # 生成一个实例

if documents:         
                    all_documents = []
                    rerank_runner = RerankRunner()
                      
                    all_documents.extend(rerank_runner.run(
                        query=query,
                        documents=documents,
                        score_threshold=0.34,
                        top_n=len(documents)
                        # model="rerank-multilingual-v2.0"
                        model="/home/yuhp/llm_models/all_models/rank_model/bge-reranker-base"
                    ))
                else:
                    all_documents.extend(documents)


