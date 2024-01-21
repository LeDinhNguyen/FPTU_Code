import pymongo
import os
import pandas as pd
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["DAP301m_movies"]

"""
data/
    cleaned_keywords.csv
    collection_df.csv
    company_df.csv
    country.csv
    craw.csv
    crew.csv
    genre.csv
    language_df.csv
"""

data_file = os.listdir("./data")
collections_name = {d: d[:-4] for d in data_file}
for i in data_file:
    print(i)
data = pd.read_csv("./data/cleaned_keywords.csv", index_col=0)

def mongoimport(csv_path, collection):
    data = pd.read_csv(csv_path, index_col=0)
    temp = []
    for i in range(data.shape[0]):
        temp.append(data.iloc[i].to_dict())
    collection.insert_many(temp)

for d in data_file:
    if collections_name[d] not in mydb.list_collection_names():
        mydb.create_collection(collections_name[d])
    curr_coll = mydb[collections_name[d]]
    print(f"******Start {collections_name[d]}******")
    mongoimport(f"./data/{d}", curr_coll)
    print(f"******Done {collections_name[d]}******\n")
