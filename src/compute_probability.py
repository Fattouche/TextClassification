

def compute_probability(model, total_wise, total_future, word):
    # divide the number of times the item appears in the wise plus 1, by the number of times wise appears plus total number of words in map.
    counter = model.get(word)
    if(counter is not None):
        wise_numerator = counter[0] + 1
        future_numerator = counter[1]+1
    else:
        wise_numerator = future_numerator = 1

    wise_denominator = total_wise+(len(model))
    wise_probability = wise_numerator/wise_denominator

    future_denominator = total_future+(len(model))
    future_probability = future_numerator/future_denominator

    return wise_probability, future_probability


def compute_sentence_probability(model, total_wise, total_future, sentence):
    wise_probability = 1
    future_probability = 1
    for word in sentence:
        wise, future = compute_probability(
            model, total_wise, total_future, word)
        wise_probability *= wise
        future_probability *= future
    return wise_probability, future_probability
