from neuron import Neuron


class Layer:
    num_neurons = 0
    num_inputs = 0
    neurons = []

    def __init__(self, num_inputs, num_neurons):
        self.num_inputs = num_inputs
        self.num_neurons = num_neurons

        for i in range(0, num_neurons):
            self.neurons += [Neuron(num_inputs)]

    def process(self, inputs):
        outputs = []
        for i in range(0, self.num_neurons):
            outputs += [self.neurons[i].process(inputs)]
        return outputs
