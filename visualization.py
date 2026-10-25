import matplotlib.pyplot as plt

def vizualize(Cities):
    print(Cities.cities)
    plt.figure(figsize=(8, 6))
    for i, city in enumerate(Cities.cities):
        plt.annotate(f"Város {i}", (city[0], city[1]), textcoords="offset points", xytext=(0,10), ha='center')
        plt.scatter(city[0], city[1], color='red', zorder=5)

    for cord in Cities.neighbours:
        items = list(cord.items())

        if items:
            city_a = list(cord.keys())
            city_b = list(cord.values())

            x_cords = [Cities.cities[city_a[0]][0], Cities.cities[city_b[0]][0]]
            y_cords = [Cities.cities[city_a[0]][1], Cities.cities[city_b[0]][1]]

            plt.plot(x_cords, y_cords ,color='blue', linewidth=2, marker='o')
    
    plt.title("Utazó Ügynök Probléma - Kezdeti állapot")
    plt.xlabel("X koordináta")
    plt.ylabel("Y koordináta")

    plt.grid(True)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.show()
