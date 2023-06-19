import unittest

import synaptic


class TestSynaptic(unittest.TestCase):

    def test_add_neuron(self):
        # Arrange
        network = synaptic.SynapticNetwork()

        # Act
        network.add_neuron(1)

        # Assert
        assert len(network.neurons) == 1

    def test_add_synapse(self):
        # Arrange
        network = synaptic.SynapticNetwork()
        neuron1 = network.add_neuron(1)
        neuron2 = network.add_neuron(2)

        # Act
        network.add_synapse(neuron1, neuron2, 1)

        # Assert
        assert neuron1.synapses[0].target == neuron2
        assert neuron1.synapses[0].weight == 1

    def test_update_weights(self):
        # Arrange
        network = synaptic.SynapticNetwork()
        network.add_neuron(1)
        network.add_neuron(2)
        network.add_synapse(1, 2, 1)

        # Act
        network.update_weights(0.1)

        # Assert
        assert network.neurons[0].activation == 0.1
        assert network.neurons[1].activation == 0.2

    def test_forward_pass(self):
        # Arrange
        network = synaptic.SynapticNetwork()
        network.add_neuron(1)
        network.add_neuron(2)
        network.add_synapse(1, 2, 1)

        # Act
        network.forward_pass([1])

        # Assert
        assert network.neurons[0].activation == 1
        assert network.neurons[1].activation == 1.1

    def test_backpropagate(self):
        # Arrange
        network = synaptic.SynapticNetwork()
        network.add_neuron(1)
        network.add_neuron(2)
        network.add_synapse(1, 2, 1)

        # Act
        network.forward_pass([1])
        network.backpropagate([0.5])

        # Assert
        assert network.neurons[0].activation == 0.5
        assert network.neurons[1].activation == 0.6


if __name__ == "__main__":
    unittest.main()
