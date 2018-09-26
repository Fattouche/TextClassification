from extract_data import train_model, extract_data
from compute_probability import compute_sentence_probability

data_filename = "../data/testdata.txt"
label_filename = "../data/testlabels.txt"


def classify():
    model, total_wise, total_future = train_model()
    test_data, test_labels = extract_data(
        data_filename, label_filename)
    results = []
    correct_counter = 0
    for i, sentence in enumerate(test_data):
        array_sentence = sentence.split(' ')
        wise_probability, future_probability = compute_sentence_probability(
            model, total_wise, total_future, array_sentence)
        class_prediction = predict_class(wise_probability, future_probability)
        results.append({"sentence": sentence,
                        "prediction": class_prediction, "actual": test_labels[i]})
        if(class_prediction == int(test_labels[i])):
            correct_counter += 1
    for result in results:
        print(result)
    print("Accuracy: {0:.2f}%".format(
        (correct_counter/len(test_labels))*100))


def predict_class(probability1, probability2):
    if probability1 > probability2:
        return 0
    else:
        return 1


classify()
