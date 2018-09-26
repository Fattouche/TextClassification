
training_data_filename = '../data/traindata.txt'
training_labels_filename = '../data/trainlabels.txt'
test_data_filename = '../data/testdata.txt'
test_label_filename = '../data/testlabels.txt'


#useless_words = ['a', 'an', 'the', 'it']
useless_words = []


def extract_data(data_filename, labels_filename):
    data = []
    labels = []

    with open(data_filename) as data_file:
        data = data_file.readlines()

    with open(labels_filename) as labels_file:
        labels = labels_file.readlines()

    data = [x.strip() for x in data]
    labels = [x.strip() for x in labels]

    return data, labels


def train_model():

    model = {}
    num_wise = num_future = 0
    training_data, training_labels = extract_data(
        training_data_filename, training_labels_filename)

    training_data = [x.split() for x in training_data]

    for i, message in enumerate(training_data):
        for word in message:
            if word not in useless_words:
                if word in model:
                    model[word][int(training_labels[i])] += 1
                else:
                    model[word] = [0, 0]
                    model[word][int(training_labels[i])] = 1

        if int(training_labels[i]) == 0:
            num_wise += 1
        else:
            num_future += 1

    return model, num_wise, num_future


model, num_wise, num_future = train_model()
