import FileParser as fp
import numpy as np
import math
from Node import Node
from NeuralNetwork import Neural_Network

dayToIndex = {'Monday    ': 1,
              'Tuesday   ': 2,
              "Wednesday ": 3,
              "Thursday  ": 4,
              "Friday    ": 5,
              "Saturday  ": 6,
              "Sunday    ": 7}


class PopulateMap():
    def __init__(self):
        self.set = fp.parseCSV(fp.crime_datasets[1])
        inp = ["occurrencedayofweek", "occurrencehour", "X", "Y"]
        output = ["Lat", "Long"]
        inputX = self.set[inp]
        inputX["occurrencedayofweek"] = inputX["occurrencedayofweek"].replace(
            dayToIndex)

        self.applyFilter(4.0, 11.0)
        self.nodes = []
        for index, row in self.set.iterrows():
            self.nodes.append(Node(float(row["X"]), float(row["Y"])))
        self.getNeighbors(0.03)

    def applyFilter(self, day, time):
        first = self.set[self.set.occurrencedayofweek == day]
        self.set = first[first.occurrencehour == time]

    def distanceTo(self, n1, n2):
        return math.sqrt((n1.lat-n2.lat)**2 + (n1.long - n2.long)**2)

    def getNeighbors(self, threshold):
        for i in range(len(self.nodes)):
            for b in range(i + 1, len(self.nodes)):
                if (self.distanceTo(self.nodes[i], self.nodes[b]) < threshold):
                    self.nodes[i].neighbors = self.nodes[i].neighbors + 1
