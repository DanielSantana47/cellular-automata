import matplotlib.pyplot as plt
import matplotlib.animation as animation


class TrafficVisualization:

    def __init__(self, simulation):
        self.simulation = simulation

        self.fig, self.ax = plt.subplots()
        self.image = self.ax.imshow([self.simulation.get_visual_state()], aspect='auto')

        self.ax.set_title("Simulação de Fluxo de Trânsito")
        self.ax.set_yticks([])

    def update(self, frame):
        self.simulation.step()
        self.image.set_data([self.simulation.get_visual_state()])
        return self.image,

    def animate(self):
        animation.FuncAnimation(
            self.fig,
            self.update,
            interval=100,
            blit=True
        )
        plt.show()
