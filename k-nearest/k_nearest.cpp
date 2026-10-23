#include <vector>
#include <cmath>

struct City
{
    double x;
    double y;
};


class k_nearest
{
private:
    std::vector<City> cities;
public:
    k_nearest();
    void add_city(double x, double y);
    size_t get_size();
    const City& get_city(size_t index);
};

void k_nearest::add_city(double x, double y)
{
    City city;
    city.x = x;
    city.y = y;
    cities.push_back(city);
}

size_t k_nearest::get_size()
{
    return cities.size();
}

const City& k_nearest::get_city(size_t index)
{
    return cities[index];
}

