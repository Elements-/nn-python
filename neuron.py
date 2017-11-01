import math, random


class Neuron:
    num_inputs = 0
    bias = 0
    weights = []

    def __init__(self, num_inputs):
        self.num_inputs = num_inputs
        for i in range(0, num_inputs):
            self.weights += [random.random()]
        self.bias = random.random()

    def process(self, inputs):
        output = 0
        for i in range(0, self.num_inputs):
            output += inputs[i] * self.weights[i]
        output += self.bias
        return 1 / (1 + math.exp(-output))

    def setBias(self, bias):
        self.bias = bias

    def setWeight(self, index, weight):
        self.weights[index] = weight
