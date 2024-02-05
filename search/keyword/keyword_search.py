from search.keyword.Jieba_Keyword_Table_Handler import JiebaKeywordTableHandler
from langchain.schema import BaseRetriever, Document
from collections import defaultdict
from typing import Dict,Set,List



class KeywordTableIndex():
    def __init__ (self, texts: List[Document]):
       self._texts = texts
   
    def create_keyword_table(self, **kwargs) ->Dict(str: Set(str)) :
        keyword_table_handler = JiebaKeywordTableHandler()
        keyword_table = {}
        # keyword_table = {key = keyword, value = set(doc.id)}
        
        for text in self._texts:
            keywords = keyword_table_handler.extract_keywords(text.page_content)
            # self._update_segment_keywords(text.metadata['doc_id'], list(keywords))
            keyword_table = self._add_text_to_keyword_table(keyword_table, text.metadata['doc_id'], list(keywords))
           
        return keyword_table

    def _add_text_to_keyword_table(self, keyword_table: dict, id: str, keywords: list[str]) -> dict:
        for keyword in keywords:
            if keyword not in keyword_table:
                keyword_table[keyword] = set()
            keyword_table[keyword].add(id)
        return keyword_table

    def _retrieve_ids_by_query(self, keyword_table: dict, query: str, k: int = 4):
        keyword_table_handler = JiebaKeywordTableHandler()
        # 提取查询中的关键词，并返回set(str)
        keywords = keyword_table_handler.extract_keywords(query)

        # go through text chunks in order of most matching keywords
        chunk_indices_count: Dict[str, int] = defaultdict(int)
        keywords = [keyword for keyword in keywords if keyword in set(keyword_table.keys())]
        for keyword in keywords:
            for node_id in keyword_table[keyword]:
                chunk_indices_count[node_id] += 1

        sorted_chunk_indices = sorted(
            list(chunk_indices_count.keys()),
            key=lambda x: chunk_indices_count[x],
            reverse=True,
        )
       
        result_id = sorted_chunk_indices[: k]
        docs = [doc for doc in self._texts if doc.metadata['doc_id'] in result_id]

        return docs
        # return[doc]




