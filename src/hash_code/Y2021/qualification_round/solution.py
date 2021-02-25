import logging
import os
from collections import defaultdict
from math import ceil


class City:
    def __init__(self, ):
        self.in_intersections = defaultdict(list)
        self.out_intersections = defaultdict(list)
        self.streets = dict()
        self.traffic = defaultdict(int)
        self.weights = dict()

    def add_street(self, street):
        self.in_intersections[street["end"]].append(street["name"])
        self.out_intersections[street["start"]].append(street["name"])
        self.streets[street["name"]] = street

    def add_car(self, car):
        for street in car:
            self.traffic[street] += 1

    def build_weights(self):
        for intersection, streets in self.in_intersections.items():
            total_traffic = sum([self.traffic[street] for street in streets])
            self.weights[intersection] = {
                street: self.traffic[street] / total_traffic for street in streets
            }

    def build_scheduler_v0(self, lift=2):
        scheduler = {
            intersection: {
                street: ceil(lift * weight / sum(traffic.values()))
                for street, weight in traffic.items()
            }
            for intersection, traffic in self.weights.items()
        }
        return scheduler


def make_solution(total_time, nb_intersection, reward, streets, cars):
    logger = logging.getLogger()
    city = City()
    logger.info(f'Adding {len(streets)} streets')
    for street in streets:
        city.add_street(street=street)
    logger.info(f'Adding {len(cars)} cars')
    for car in cars:
        city.add_car(car=car)
    logger.info(f'Building weights')
    city.build_weights()
    logger.info(f'Building scheduler')
    scheduler = city.build_scheduler_v0(lift=2)
    return scheduler

