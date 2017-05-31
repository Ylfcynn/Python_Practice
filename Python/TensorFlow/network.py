"""

"""

import pickle
import tflearn
# from data_format import equation
import tflearn.datasets.mnist as mnist

# train_x, train_y, test_x, test_y = pickle.load(open('data_set.pickle', 'rb'))    # Machine learning example

train_x, train_y, test_x, test_y = mnist.load_data(one_hot=True)    # Deep learning example

number_of_nodes = 500    # Nodes are equivalent to neurons.

network = tflearn.input_data(shape=[None, 784]) # First element is almost always 'None' when working with 1-dimensional stuff.
network = tflearn.fully_connected(network, number_of_nodes)
network = tflearn.fully_connected(network, number_of_nodes)
network = tflearn.fully_connected(network, 10, activation='softmax') # Output layer
network = tflearn.regression(network)

model = tflearn.DNN(network, tensorboard_verbose=0)
#model.load('./best_model')
model.fit(train_x, train_y, n_epoch=4, batch_size=1000, show_metric=True, validation_set=(test_x, test_y)) # Network training here.

model.save('best_model')
def format_pred(prediction):
    pred = prediction[0]
    index = 0
    max = pred[0]
    for i in range(len(pred)):
        max = pred[i]
        index = i

    return index


print(test_y[0])
print(format_pred(model.predict([test_x[0]])))

