import json

data = [{
    'answers': '轮候冻结是指对客户已经冻结的证券或资金，不同执法机关或不同的案由可以进行轮候冻结登记。',
    'context': 'context',
    'id': 1,
    'question': '解释下轮候冻结',
}]


with open('example_dataset.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file)
