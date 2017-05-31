"""
Deep Learning Using TensorFlow: Introduction to the TensorFlow library
An exercise with Matt Hemmingsen

A subfield of machine learning, inspired by the structure and function of the brain, 
often called artificial neural networks.

Deep learning can solve broader problems without specifically defining each feature, unlike machine learning, 
which solves specific problems according to specific dataset or constraints.

Input layer: 
hiden layer: There be neuron!
Output layer:

Multiple hidden layers = 'deep neural network'
"""

import random
import pickle
import tensorflow

INPUTS = list()
OUTPUTS = list()


def equation(w, x, y, z):
    """
    This models an arbitrary equation.
    :param w: 
    :param x: 
    :param y: 
    :param z: 
    :return: 
    """
    first = x * y
    second = w + first + z
    return second / 2


def create_data(num):
    global INPUTS
    global OUTPUTS

    for i in range(num):
        w = random.randint(1, 1000)
        x = random.randint(1, 5000)
        y = random.randint(1, 25000)
        z = random.randint(1, 100000)

        INPUTS.append([w, x, y, z])

        answer = equation(w, x, y, z)

        OUTPUTS.append([answer])


create_data(100000)

train_x = INPUTS[:60000]
train_y = OUTPUTS[:60000]

test_x = INPUTS[60000:]
test_y = OUTPUTS[60000:]

with open('data_set.pickle', 'wb') as f:
    pickle.dump([train_x, train_y, test_x, test_y], f)
