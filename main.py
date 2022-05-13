import requests
import pandas as pd
import os
from functions import extractLoad
from datetime import datetime
from google.cloud import bigquery


# Fetch prices from Binance API
"""
Fetches all information on every available pairs on Binance (cryptocurrency trading platform) as json
Converts to Pandas DataFrame
Minor transformation - Add new datetime column
"""

el = extractLoad()
df = el.fetch_api()
final_df = el.add_datetime(df)
#el.load_bigquery(final_df)