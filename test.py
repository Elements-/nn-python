#from neuron import Neuron
###n = Neuron(2)
#n.setWeight(0, -2)
#n.setWeight(1, -2)
#n.setBias(3)
#print(n.process([0, 0]))

from network import Network

training_examples = [
    [[0, 0], [1]],
    [[1, 1], [1]],
    [[0, 1], [0]],
    [[1, 0], [0]]
]

net = Network([2,2,3])
print(net.process([1,0]))