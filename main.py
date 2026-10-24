import random
import math
from visualization import vizualize



class Cities:
    def __init__(self):
        self.NUM_CITIES = 10
        self.cities = [(random.randint(0,100), random.randint(0, 100)) for _ in range(self.NUM_CITIES)] 
        #self.cities = [(64, 10), (65, 68)]
        self.total_dist = 0
        self.neighbours = []

    def return_cities(self):
        return self.cities
    
    def distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

    def get_k_every(self):
        
        for i, city_i in enumerate(self.cities):
            smallest_d = 999999
            smallest_d_city = None
            for j, city_j in enumerate(self.cities):
                d = self.distance(city_i, city_j)
                
                if d < smallest_d and i != j:
                    smallest_d = d
                    smallest_d_city = j

            self.neighbours.append({i : smallest_d_city})


cities_instance = Cities()
cities_instance.get_k_every()
print(cities_instance.neighbours)
vizualize(Cities=cities_instance)


