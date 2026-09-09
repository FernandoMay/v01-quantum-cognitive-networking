"""
Quantum-Inspired Cognitive Networking: A Framework for Adaptive
AI-Native 6G Infrastructure

Paper: Quantum-Inspired Cognitive Networking for AI-Native 6G
Venue: ICMV 2026
Authors: Fernando May et al.
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple
import time


@dataclass
class NetworkNode:
    node_id: int
    position: np.ndarray
    neighbors: List[int]
    load: float = 0.0
    energy: float = 1.0
    qubits: int = 8

    @property
    def available_capacity(self) -> float:
        return (1.0 - self.load) * self.energy


@dataclass
class QuantumRoute:
    path: List[int]
    cost: float
    probability: float
    superposition_score: float


class QuantumInspiredOptimizer:
    """Quantum-inspired optimization for cognitive routing."""

    def __init__(self, num_nodes: int = 20, num_qubits: int = 8):
        self.num_nodes = num_nodes
        self.num_qubits = num_qubits
        self.amplitude_matrix = np.random.randn(num_nodes, num_nodes) * 0.1
        self.phase_matrix = np.random.uniform(0, 2*np.pi, (num_nodes, num_nodes))

    def _superposition_exploration(self, current: int,
                                    visited: set) -> List[Tuple[int, float]]:
        candidates = []
        for next_node in range(self.num_nodes):
            if next_node not in visited and next_node != current:
                amp = np.abs(self.amplitude_matrix[current, next_node])
                phase = self.phase_matrix[current, next_node]
                probability = amp ** 2
                score = probability * (1 + np.cos(phase))
                candidates.append((next_node, score))
        candidates.sort(key=lambda x: -x[1])
        return candidates[:self.num_qubits]

    def _entanglement_correlation(self, path1: List[int],
                                   path2: List[int]) -> float:
        overlap = len(set(path1) & set(path2))
        max_len = max(len(path1), len(path2))
        return overlap / max(max_len, 1)

    def find_route(self, source: int, destination: int,
                   num_paths: int = 3) -> List[QuantumRoute]:
        routes = []
        for _ in range(num_paths):
            path = [source]
            visited = {source}
            current = source

            for step in range(self.num_nodes):
                if current == destination:
                    break
                candidates = self._superposition_exploration(current, visited)
                if not candidates:
                    break
                next_node = candidates[0][0]
                path.append(next_node)
                visited.add(next_node)
                current = next_node

            if path[-1] == destination:
                cost = len(path) * 1.0
                prob = np.prod([
                    np.abs(self.amplitude_matrix[path[i], path[i+1]])
                    for i in range(len(path)-1)
                ])
                routes.append(QuantumRoute(
                    path=path, cost=cost,
                    probability=min(prob, 1.0),
                    superposition_score=prob * len(path)
                ))

        routes.sort(key=lambda r: r.cost)
        return routes

    def update_amplitudes(self, path: List[int], reward: float):
        for i in range(len(path)-1):
            src, dst = path[i], path[i+1]
            self.amplitude_matrix[src, dst] += reward * 0.01
            self.phase_matrix[src, dst] += reward * 0.05


class ClassicalRouter:
    """Baseline Dijkstra router."""

    def __init__(self, num_nodes: int = 20):
        self.num_nodes = num_nodes
        self.distance_matrix = np.random.rand(num_nodes, num_nodes) * 10
        np.fill_diagonal(self.distance_matrix, 0)
        self.distance_matrix = np.maximum(
            self.distance_matrix, self.distance_matrix.T
        )

    def find_route(self, source: int, destination: int) -> List[int]:
        dist = np.full(self.num_nodes, np.inf)
        prev = np.full(self.num_nodes, -1, dtype=int)
        dist[source] = 0
        visited = set()

        for _ in range(self.num_nodes):
            u = -1
            min_dist = np.inf
            for v in range(self.num_nodes):
                if v not in visited and dist[v] < min_dist:
                    min_dist = dist[v]
                    u = v
            if u == -1:
                break
            visited.add(u)
            for v in range(self.num_nodes):
                if v not in visited:
                    new_dist = dist[u] + self.distance_matrix[u, v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        prev[v] = u

        path = []
        current = destination
        while current != -1:
            path.append(current)
            current = prev[current]
        return list(reversed(path))


class SimulationRunner:
    """Main simulation for quantum-inspired cognitive networking."""

    def __init__(self, num_nodes: int = 20):
        self.num_nodes = num_nodes
        self.quantum_optimizer = QuantumInspiredOptimizer(num_nodes)
        self.classical_router = ClassicalRouter(num_nodes)

    def run_comparison(self) -> Dict:
        source = 0
        destination = self.num_nodes - 1

        print("Finding quantum-inspired routes...")
        quantum_routes = self.quantum_optimizer.find_route(
            source, destination, num_paths=5
        )

        print("Finding classical route...")
        classical_path = self.classical_router.find_route(source, destination)

        quantum_cost = quantum_routes[0].cost if quantum_routes else float('inf')
        classical_cost = len(classical_path)

        return {
            "quantum": {
                "cost": quantum_cost,
                "num_routes": len(quantum_routes),
                "best_path": quantum_routes[0].path if quantum_routes else [],
                "probability": quantum_routes[0].probability if quantum_routes else 0
            },
            "classical": {
                "cost": classical_cost,
                "path": classical_path
            },
            "improvement": (classical_cost - quantum_cost) / max(classical_cost, 1) * 100
        }

    def run_scalability(self) -> Dict:
        scales = [10, 20, 50, 100]
        results = {}

        for n in scales:
            self.quantum_optimizer = QuantumInspiredOptimizer(n)
            self.classical_router = ClassicalRouter(n)
            self.num_nodes = n
            results[n] = self.run_comparison()

        return results


if __name__ == "__main__":
    np.random.seed(20260909)
    print("=" * 60)
    print("Quantum-Inspired Cognitive Networking for 6G")
    print("ICMV 2026 — Simulation Runner")
    print("=" * 60)

    runner = SimulationRunner(num_nodes=20)

    print("\n--- Route Comparison ---")
    comparison = runner.run_comparison()
    print(f"Quantum Route Cost:  {comparison['quantum']['cost']:.2f}")
    print(f"Classical Route Cost: {comparison['classical']['cost']:.2f}")
    print(f"Improvement: {comparison['improvement']:.1f}%")
    print(f"Quantum Routes Found: {comparison['quantum']['num_routes']}")
