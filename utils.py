from itertools import zip_longest

import transformers.data.metrics.squad_metrics as squad_metrics


def doc_to_text(doc):
    # Given a passage p, the conversation history {q1, a1, . . . qi−1, ai−1}
    # and a question qi, the task is to predict the answer ai
    preprompt = ""
    doc_text = preprompt + "\n\n" + "context:{{"
    for a in doc["context"]: 
        doc_text += doc["context"] + "\n\n"
    q = doc["FAQ问题"]
    question = f"Q: {q}\n\n"
    answer = f"A:"
    doc_text += "}}" + question + answer
    return doc_text


def doc_to_target(doc):
    answers = "A:" + doc["FAQ回答"]
    return answers


def em(gold_list, pred):
    # tests for exact match and on the normalised answer (compute_exact)
    em_sum = 0.0
    em_sum += max(squad_metrics.compute_exact(gold_list, pred))

    return em_sum


def compute_scores(gold_list, pred):
    # tests for exact match and on the normalised answer (compute_exact)
    # test for overlap (compute_f1)
    f1_sum = 0.0
    em_sum = 0.0
    
    em_sum += max(squad_metrics.compute_exact(gold_list, pred))
    f1_sum += max(squad_metrics.compute_f1(gold_list, pred))

    return {
        "em": em_sum,
        "f1": f1_sum),
    }


def process_results(doc, results):
    gold_list = doc_to_target(doc)
    pred = results[0].strip().split("\n")[0]

    scores = compute_scores(gold_list, pred)
    return scores
    
