import requests
import pandas as pd
import os
from datetime import datetime
from google.cloud import bigquery

# Creds are supplied through Airflow's environment variables

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/secret/creds.json'

class extractLoad:

    # Fetch prices from Binance API

    """
    Fetches all information on every available pairs on Binance 
    (cryptocurrency trading platform) as json
    Converts to DataFrame with pandas built-in read_json

    Input : None
    Output : DataFrame
    """

    def fetch_api(self):
        r = requests.get("https://api.binance.com/api/v3/ticker/24hr")
        r_json = r.json()
        df = pd.read_json("https://api.binance.com/api/v3/ticker/24hr")
        return df
    
    # Add datetime column - Minor Transformation

    """
    Adds an additional datetime column for the entire batch of data
    Format YYYY-MM-DD HH:MM:SS

    Input : DataFrame
    Output : DataFrame
    """

    def add_datetime(self, dataframe):
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dataframe['datetime'] = dt
        return dataframe

    # Load to Database

    """
    Loads DataFrame to BigQuery as a table

    Input : DataFrame
    Output : None
    """

    def load_bigquery(self, dataframe):
        print("Data Loaded")
        table_id = 'final-347314.main.binance_api'
        client = bigquery.Client()
        client.load_table_from_dataframe(df, table_id)
