from simulation import TrafficSimulation
from visualization import TrafficVisualization
from analysis import TrafficAnalysis


class Application:

    def run(self):

        road_length = 100
        car_density = 0.3
        max_speed = 5
        slow_probability = 0.2

        simulation = TrafficSimulation(
            road_length,
            car_density,
            max_speed,
            slow_probability
        )

        visualization = TrafficVisualization(simulation)
        visualization.animate()

        TrafficAnalysis.plot_speed_over_time(simulation)

        TrafficAnalysis.plot_flow_vs_density(
            road_length,
            max_speed,
            slow_probability
        )


if __name__ == "__main__":
    app = Application()
    app.run()
