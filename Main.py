import FileParser as fp
import tensorflow as tf
import numpy as np
dayToIndex = {"Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7}
monthToIndex = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
if __name__ == "__main__":
    robDset = fp.parseCSV(fp.crime_datasets[1])
    features = ["LAT", "LONG", "reportedhour", "occurencemonth", "reportedday","reporteddayofweek"]

