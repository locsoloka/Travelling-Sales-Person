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

    def get_islands(self):
        island = []

        neighbours_cpy = list(self.neighbours)


        while neighbours_cpy:
            current_island = [neighbours_cpy.pop(0)]

            added = True
            while added:
                added = False
                i = 0
                while i < len(neighbours_cpy):
                    neighbour = neighbours_cpy[i]
                    n_keys = set(neighbour.keys())   # set segít nekünk gyorsan összehasonéítani értékeket
                    n_vals = set(neighbour.values())

                    is_connected = False
                    for item in current_island:
                        i_keys = set(item.keys())
                        i_vals = set(item.values())       

                        if (n_keys & i_keys) or (n_keys & i_vals) or (n_vals & i_keys) or (n_vals & i_vals):
                            is_connected = True
                            break

                    if is_connected:
                        current_island.append(neighbours_cpy.pop(i))
                        added = True
                    else:
                        i += 1
            island.append(current_island)
        print("island", island)

cities_instance = Cities()
cities_instance.get_k_every()
cities_instance.get_islands()
print(cities_instance.neighbours)
vizualize(Cities=cities_instance)


