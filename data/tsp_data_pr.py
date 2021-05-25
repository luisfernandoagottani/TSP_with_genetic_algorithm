# TSP data from https://developers.google.com/optimization/routing/tsp
import math
import random
import copy
from random import choice
from copy import deepcopy
from data.read_tsp_data import from_file
import pandas as pd

# data = from_file('data/berlin52.txt')
# data_uy = from_file('data/uy734.txt')
data_pr = from_file('data/pr2392.txt')

def euclidian_distance(city_departure, city_arrive):
    return abs(math.sqrt((city_departure.x - city_arrive.x) ** 2 + (city_departure.y - city_arrive.y) ** 2))

def dist_matrix(data):
    city_distance = []
    for i, city_departure in enumerate(data):
        city_distance.append([])
        for city_arrive in data:
            city_distance[i].append(euclidian_distance(city_departure, city_arrive))
    return city_distance


distance_matrix = dist_matrix(data_pr)
