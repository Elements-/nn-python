from layer import Layer


class Network:
    num_layers = 0
    layers = []

    def __init__(self, layer_sizes):
        self.num_layers = len(layer_sizes)
        for i in range(0, self.num_layers):
            num_inputs = layer_sizes[i] if i == 0 else layer_sizes[i - 1]
            self.layers += [Layer(layer_sizes[i], num_inputs)]

    def process(self, inputs):
        current_inputs = inputs
        for i in range(0, self.num_layers):
            current_inputs = self.layers[i].process(current_inputs)
        return current_inputs

