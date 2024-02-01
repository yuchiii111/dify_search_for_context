import weaviate
from langchain.vectorstores import VectorStore

# 向量检索

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

# rerank

documents->


if documents:
                if reranking_model and search_method == 'semantic_search':
                    try:
                        model_manager = ModelManager()
                        rerank_model_instance = model_manager.get_model_instance(
                            tenant_id=dataset.tenant_id,
                            provider=reranking_model['reranking_provider_name'],
                            model_type=ModelType.RERANK,
                            model=reranking_model['reranking_model_name']
                        )
                    except InvokeAuthorizationError:
                        return

                      
                    all_documents = []
                    rerank_runner = RerankRunner(rerank_model_instance)
                      
                    all_documents.extend(rerank_runner.run(
                        query=query,
                        documents=documents,
                        score_threshold=score_threshold,
                        top_n=len(documents)
                    ))
                else:
                    all_documents.extend(documents)



