import FileParser as fp
import numpy as np
import math
import matplotlib.pyplot as plt
from Node import Node
from NeuralNetwork import Neural_Network
dayToIndex = {'Monday    ': 1,
            'Tuesday   ': 2,
            "Wednesday ": 3,
            "Thursday  ": 4,
            "Friday    ": 5,
            "Saturday  ": 6,
            "Sunday    ": 7}
'''

'''
def applyFilter(set, day, time):
    first =  set[set.occurrencedayofweek == day]
    first = first[first.occurrencehour == time]
    return first
'''
'''
def distanceTo(n1, n2):
    return math.sqrt((n1.lat-n2.lat)**2 + (n1.long - n2.long)**2)
'''
'''
def getNeighbors(Nodes, threshold):
    for i in range(len(Nodes)):
        for b in range(i + 1, len(x)):
            if (distanceTo(x[i], x[b]) < threshold):
                x[i].neighbors = x[i].neighbors + 1

if __name__ == "__main__":

    set = fp.parseCSV(fp.crime_datasets[2])
    features = ["LAT", "LONG", "occurencehour", "occurrencedayofyear","reporteddayofweek"]
    input = ["occurrencedayofweek","occurrencehour", "X", "Y"]
    output = ["Lat","Long"]
    inputX = set[input]
    inputX["occurrencedayofweek"] = inputX["occurrencedayofweek"].replace(dayToIndex)

    modified = applyFilter(inputX, 4.0, 11.0)
    x = []
    for index,row in modified.iterrows():
        x.append(Node(float(row["X"]),float(row["Y"])))
    counter = 0
    dict = {}
    getNeighbors(x, .03)
    xax = []
    yax = []
    for i in x:
        xax.append(i.lat)
        yax.append(i.long)
    plt.plot(xax,yax,'ro')
    plt.show()
