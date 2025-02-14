# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# YOUR CODE HERE
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
    
    def __str__(self):
        return f'Waypoint named {self.name} at {self.lat}, {self.lon}'
# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        return f'Geocache named {self.name} with difficulty {self.difficulty}, size {self.size}, located at {self.lat}, {self.lon}'
# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = Waypoint('Catacombs', 41.70505, -121.51521)
print(waypoint.name)
print(waypoint.lat)
print(waypoint.lon)
# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)
# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache.__str__())
