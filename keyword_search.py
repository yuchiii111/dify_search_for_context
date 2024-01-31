from Jieba_Keyword_Table_Handler import JiebaKeywordTableHandler
from langchain.schema import BaseRetriever, Document
from collections import defaultdict
from extensions.ext_database import db ?
from models.dataset import Dataset, DatasetKeywordTable, DocumentSegment ?
from core.index.base import BaseIndex ?

1.BaseIndex
2.db
3.documentsegment

class KeywordTableIndex():
   
    def create(self, texts: list[Document], **kwargs) -> BaseIndex:
        keyword_table_handler = JiebaKeywordTableHandler()
        keyword_table = {}
        # keyword_table = {key = keyword, value = set(doc.id)}
        
        for text in texts:
            keywords = keyword_table_handler.extract_keywords(text.page_content)
            # self._update_segment_keywords(text.metadata['doc_id'], list(keywords))
            keyword_table = self._add_text_to_keyword_table(keyword_table, text.metadata['doc_id'], list(keywords))

        dataset_keyword_table = DatasetKeywordTable(
            dataset_id=self.dataset.id,
            keyword_table=json.dumps({
                '__type__': 'keyword_table',
                '__data__': {
                    "index_id": self.dataset.id,
                    "summary": None,
                    "table": {}
                }
            }, cls=SetEncoder)
        )
        db.session.add(dataset_keyword_table)
        db.session.commit()

        self._save_dataset_keyword_table(keyword_table)

        return self

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

    return sorted_chunk_indices[: k]









