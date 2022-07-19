import requests
import pandas as pd
import os
import json
from datetime import datetime
from google.cloud import bigquery
from google.oauth2 import service_account

gcp_json_credentials_dict = json.loads(os.environ['creds'])
credentials = service_account.Credentials.from_service_account_info(gcp_json_credentials_dict)

# Creds are supplied through Airflow's environment variables

class extractLoad:

    # Fetch prices from Binance API

    """
    Fetches csv from GCS
    Converts to DataFrame with pandas built-in read_json

    Input : None
    Output : DataFrame
    """

    def fetch_csv(self):
        url = 'gs://csv-etl-fyp/historical.csv'
        csv_df = pd.read_csv(url)
        return csv_df
    
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

        table_id = 'final-347314.main.gcs_mcapcsv'
        client = bigquery.Client(credentials=credentials)
        client.load_table_from_dataframe(dataframe, table_id)
