import FileParser as fp
import numpy as np
dayToIndex = {'Monday': 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7}

if __name__ == "__main__":
    robDset = fp.parseCSV(fp.crime_datasets[1])
    features = ["LAT", "LONG", "occurencehour", "occurrencedayofyear","reporteddayofweek"]
    msk = np.random.rand(len(robDset)) < .8
    trainSet = robDset[msk]
    testSet = robDset[~msk]
    input = ["occurrencedayofweek","occurrencehour"]
    output = ["X","Y"]
    inputX = trainSet[input]
    outputY = trainSet[output]
    inputX["occurrencedayofweek"].replace({'Monday': 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7})
    print(inputX)
