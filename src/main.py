import requests
import pandas as pd
import os
from functions import extractLoad
from datetime import datetime
from google.cloud import bigquery


# Main

el = extractLoad()
df = el.fetch_api()
final_df = el.add_datetime(df)
el.load_bigquery(final_df)