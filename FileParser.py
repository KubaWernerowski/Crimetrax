import csv
import numpy as np
import json
import pandas as pd
'''
Returns array given .csv
'''
path = 'datasets/'
path_crime = 'crime_data/'
datasets = [path + "Neighbourhood_Crime_Rates_Boundary_File.csv",path+ "community-programs.csv",path + "community-programs.json"]
crime_datasets = [path_crime + "Break_and_Enter_2014_to_2017.csv",
                  path_crime + "Robbery_2014_to_2017.csv",
                  path_crime + "Theft_Over_2014_to_2017.csv"]
'''
Usages syntax:
'''
def parseCSV(file: str):
    data = pd.read_csv(file)
    return data
def parseJSON(file: str):
    data = pd.read_json(file)
    return data
