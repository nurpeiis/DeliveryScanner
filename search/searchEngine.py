import csv
from whoosh import fields, index
from whoosh.index import create_in
from whoosh.fields import * ##import all 
import pandas as pd
import numpy as np
def main():
    df = pd.read_csv("../Deliveroo.csv", sep = ",")
    #sort by price
    df.sort_values(by=["Price"], ascending=False)
    userQuery = input("Enter Your search request:")
    userQuery = userQuery.lower()
    print(userQuery)
    print(df.loc[(df["DishName"].str.lower().str.contains(userQuery)) | (df["Restaurant"].str.lower().str.contains(userQuery))]["Price"])

if __name__ == "__main__":
    # execute only if run as a script
    main()