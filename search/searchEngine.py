import csv
from whoosh import fields, index
from whoosh.index import create_in
from whoosh.fields import * ##import all 
import pandas as pd
import numpy as np
def main():
    df = pd.read_csv("../Deliveroo.csv", sep = ",")

    userQuery = input("Enter Your search request:")
    userQuery = userQuery.lower()
    print(userQuery)
    print(df.columns.tolist())
    mergeSort(df.loc[(df["DishName"].str.lower().str.contains(userQuery)) | (df["Restaurant"].str.lower().str.contains(userQuery))]["Price"])
    print(priceFoundElements)
    print(df.loc[(df["DishName"].str.lower().str.contains(userQuery)) | (df["Restaurant"].str.lower().str.contains(userQuery))]["Price"])
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)


if __name__ == "__main__":
    # execute only if run as a script
    main()