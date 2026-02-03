import numpy as np
import random


class TrafficSimulation:

    def __init__(self, road_length: int, car_density: float, max_speed: int, slow_prob: float):
        self.road_length = road_length
        self.car_density = car_density
        self.max_speed = max_speed
        self.slow_prob = slow_prob

        self.road = [-1] * self.road_length
        self.speed_history = []

        self.initialize_road()

    def initialize_road(self):
        num_cars = int(self.road_length * self.car_density)
        positions = random.sample(range(self.road_length), num_cars)

        for pos in positions:
            self.road[pos] = random.randint(0, self.max_speed)

    def distance_to_next_car(self, position: int) -> int:
        for d in range(1, self.road_length):
            if self.road[(position + d) % self.road_length] != -1:
                return d
        return self.road_length

    def step(self):
        new_road = [-1] * self.road_length
        speeds = []

        for position in range(self.road_length):

            speed = self.road[position]

            if speed != -1:

                if speed < self.max_speed:
                    speed += 1

                distance = self.distance_to_next_car(position)
                speed = min(speed, distance - 1)

                if speed > 0 and random.random() < self.slow_prob:
                    speed -= 1

                new_position = (position + speed) % self.road_length
                new_road[new_position] = speed
                speeds.append(speed)

        self.road = new_road

        if speeds:
            self.speed_history.append(np.mean(speeds))
        else:
            self.speed_history.append(0)

    def get_visual_state(self):
        return [1 if cell != -1 else 0 for cell in self.road]

    def get_average_speed(self):
        return np.mean(self.speed_history) if self.speed_history else 0
