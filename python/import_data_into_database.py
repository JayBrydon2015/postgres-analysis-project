# -*- coding: utf-8 -*-

"""

Import dataset into the database.

"""


#### IMPORTS ####

import pandas as pd
from sqlalchemy import create_engine, URL


#### Connect to postgres server and import dataset into database ####

df = pd.read_csv("datasets/CAS_Data_public.csv")
print(f"Loaded {len(df):,} crash records.")

df.columns = df.columns.str.lower()

# Read in username and password stored in txt file
with open(
        "config/postgres_server_credentials.txt",
        "r", encoding="utf-8"
    ) as f:
    username, password = [line.strip() for line in f.readlines()]


connection_url = URL.create(
    drivername="postgresql+psycopg",
    username=username,
    password=password,
    host="localhost",
    port=5432,
    database="postgres_analysis_project"
)

engine = create_engine(connection_url)

# (Took a while to finish)
df.to_sql(
    name="crashes",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=500,
    method="multi"
)

print("Dataset successfully imported!")

engine.dispose()

