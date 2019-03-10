import FileParser as fp
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas
import time
from Node import Node

dayToIndex = {'Monday    ': 1,
              'Tuesday   ': 2,
              "Wednesday ": 3,
              "Thursday  ": 4,
              "Friday    ": 5,
              "Saturday  ": 6,
              "Sunday    ": 7}


class PopulateMap():
    def __init__(self,crime: int ):
        self.set = fp.parseCSV(fp.crime_datasets[crime])
        inp = ["occurrencedayofweek", "occurrencehour", "X", "Y"]
        inputX = self.set[inp]
        self.nodes = []
        inputX["occurrencedayofweek"] = inputX["occurrencedayofweek"].replace(dayToIndex)
        self.set = inputX
        self.filteredSet = None
        self.applyFilter(4.0, 11.0)

    def applyFilter(self, day, time):
        first = self.set[self.set.occurrencedayofweek == day]
        self.filteredSet = first[first.occurrencehour == time]
        self.nodes = []
        for index, row in self.filteredSet.iterrows():
            self.nodes.append(Node(float(row["X"]), float(row["Y"])))
        self.getNeighbors(0.03)

    def distanceTo(self, n1, n2):
        return math.sqrt((n1.lat-n2.lat)**2 + (n1.long - n2.long)**2)
    def getNeighbors(self, threshold):
        for i in range(len(self.nodes)):
            for b in range(i + 1, len(self.nodes)):
                if (self.distanceTo(self.nodes[i], self.nodes[b]) < threshold):
                    self.nodes[i].neighbors = self.nodes[i].neighbors + 1
    def getMaxNode(self):
        max = -1
        maxNode = self.nodes[0];
        for node in self.nodes:
            if (node.neighbors > max):
                maxNode = node
                max = node.neighbors
        return maxNode


if __name__ == "__main__":
    maxnodeX = []
    maxnodeY = []
    maxnodeZ = []
    x = PopulateMap(0)
    y = PopulateMap(1)
    z = PopulateMap(2)
    for i in range(0,24):
        x.applyFilter(4,i)
        y.applyFilter(4, i)
        z.applyFilter(4, i)
        xax = []
        yax = []
        for b in x.nodes:
            xax.append(b.lat)
            yax.append(b.long)
        xax1 = []
        yax1 = []
        for b in y.nodes:
            xax1.append(b.lat)
            yax1.append(b.long)
        xax2 = []
        yax2 = []
        for b in z.nodes:
            xax2.append(b.lat)
            yax2.append(b.long)
        dot_size = 3
        plt.plot(yax,xax,'ro', label="Breaking and Entering",color='b',ms=dot_size)
        plt.plot(yax1,xax1,'ro',label="Robbery", color='r',ms=dot_size)
        plt.plot(yax2, xax2, 'ro', label="Theft", color='g',ms=dot_size)
        maxX = x.getMaxNode()
        maxnodeX.append(maxX)
        plt.plot(maxX.long, maxX.lat, 'ro',color='b', ms=maxX.neighbors,alpha=.7)
        maxY = y.getMaxNode()
        maxnodeY.append(maxY)
        plt.plot(maxY.long, maxY.lat, 'ro', color='r', ms=maxY.neighbors, alpha=.7)
        maxZ = z.getMaxNode()
        maxnodeZ.append(maxnodeZ)
        plt.plot(maxZ.long, maxZ.lat, 'ro', color='g', ms=maxZ.neighbors, alpha=.7)
        plt.ylim((43.575, 43.825))
        plt.xlim((-79.625,-79.1))
        plt.legend(["Breaking and Entering","Robbery","Theft"])
        plt.title("Hour: " + str(i) + " For Day 4")
        print(x.getMaxNode())


        time.sleep(.5)
        plt.show()
