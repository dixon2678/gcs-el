import requests
import pandas as pd
import os
from datetime import datetime
from google.cloud import bigquery

class extractLoad:

    def fetch_api(self):
        r = requests.get("https://api.binance.com/api/v3/ticker/24hr")
        print("stepa")
        r_json = r.json()
        print("stepb")
        df = pd.read_json("https://api.binance.com/api/v3/ticker/24hr")
        print("API data fetched")
        return df
    
    def add_datetime(self, dataframe):
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dataframe['datetime'] = dt
        print("Datetime Added")
        return dataframe

    def load_bigquery(self, dataframe):
        print("Data Loaded")
        table_id = 'final-347314.main.binance_api'
        client = bigquery.Client()
        client.load_table_from_dataframe(df, table_id)
