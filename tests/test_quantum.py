"""
Tests for Quantum-Inspired Cognitive Networking
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from quantum_networking import (
    NetworkNode, QuantumRoute, QuantumInspiredOptimizer,
    ClassicalRouter, SimulationRunner
)


class TestNetworkNode:
    def test_node_creation(self):
        node = NetworkNode(node_id=0, position=np.array([0,0,0]), neighbors=[1,2])
        assert node.node_id == 0
        assert node.available_capacity > 0


class TestQuantumInspiredOptimizer:
    def test_optimizer_creation(self):
        opt = QuantumInspiredOptimizer(num_nodes=10)
        assert opt.num_nodes == 10

    def test_find_route(self):
        opt = QuantumInspiredOptimizer(num_nodes=10)
        routes = opt.find_route(0, 9, num_paths=3)
        assert len(routes) >= 0

    def test_update_amplitudes(self):
        opt = QuantumInspiredOptimizer(num_nodes=10)
        opt.update_amplitudes([0, 1, 2], reward=1.0)
        assert opt.amplitude_matrix[0, 1] != 0


class TestClassicalRouter:
    def test_router_creation(self):
        router = ClassicalRouter(num_nodes=10)
        assert router.num_nodes == 10

    def test_find_route(self):
        router = ClassicalRouter(num_nodes=10)
        path = router.find_route(0, 9)
        assert path[0] == 0


class TestSimulationRunner:
    def test_runner_creation(self):
        runner = SimulationRunner(num_nodes=10)
        assert runner.num_nodes == 10

    def test_comparison_run(self):
        runner = SimulationRunner(num_nodes=10)
        results = runner.run_comparison()
        assert "quantum" in results
        assert "classical" in results


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
