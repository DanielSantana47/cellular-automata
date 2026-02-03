import numpy as np
import matplotlib.pyplot as plt
from simulation import TrafficSimulation


class TrafficAnalysis:

    @staticmethod
    def plot_speed_over_time(simulation, steps: int = 200):

        for _ in range(steps):
            simulation.step()

        plt.figure()
        plt.plot(simulation.speed_history)
        plt.xlabel("Tempo")
        plt.ylabel("Velocidade Média")
        plt.title("Velocidade Média dos Veículos ao Longo do Tempo")
        plt.show()

    @staticmethod
    def plot_flow_vs_density(road_length: int, max_speed: int, slow_prob: float):

        densities = np.linspace(0.05, 0.95, 20)
        flows = []

        for density in densities:

            simulation = TrafficSimulation(
                road_length,
                density,
                max_speed,
                slow_prob
            )

            for _ in range(100):
                simulation.step()

            for _ in range(200):
                simulation.step()

            avg_speed = simulation.get_average_speed()
            flow = density * avg_speed
            flows.append(flow)

        plt.figure()
        plt.plot(densities, flows)
        plt.xlabel("Densidade de Veículos")
        plt.ylabel("Fluxo de Veículos")
        plt.title("Fluxo vs Densidade")
        plt.show()
