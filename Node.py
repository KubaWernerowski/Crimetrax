class Node:
    def __init__(self, x, y):
        self.long = x
        self.lat = y
        self.neighbors = 0

    def __str__(self):
        return str(self.long) + "," + str(self.lat) + "," + str(self.neighbors)