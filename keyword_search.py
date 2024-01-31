def _retrieve_ids_by_query(self, keyword_table: dict, query: str, k: int = 4):
    keyword_table_handler = JiebaKeywordTableHandler()
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
