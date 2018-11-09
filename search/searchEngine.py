import csv
from whoosh import fields, index
from whoosh.index import create_in
from whoosh.fields import * ##import all 
import pandas as pd
import numpy as np
df = pd.read_csv("../Deliveroo.csv", sep = ",")

userQuery = input("Enter Your search request:")
userQuery = userQuery.lower()
print(userQuery)
print(df.columns.tolist())
priceFoundElements = df.loc[(df["DishName"].str.lower().str.contains(userQuery)) | (df["Restaurant"].str.lower().str.contains(userQuery))]["Price"]
