# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:54:51 2020

@author: zaynab
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 
#reading the .xlsx file using pandas

#X = pd.read_excel("Results.xlsx")

X = pd.read_excel("Results.xlsx", sheet_name = None)


#exporting each sheet as a .csv file


X = pd.read_excel("Results.xlsx", sheet_name= None)
for y in X:          #y is sheetname
    X[y].to_csv("%s.csv" %y)
  
