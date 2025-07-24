# bloodwork analysis
import pandas as pd
import health_reports

bloods = pd.read_csv('data/mel/bloodwork_clean.csv').drop(columns='Unnamed: 0')
weight = pd.read_csv('data/mel/weight_clean.csv').drop(columns='Unnamed: 0')

bloods['date'] = bloods['date'].apply(lambda row: date_yyyymmdd(row))
weight['date'] = weight['date'].apply(lambda row: date_yyyymmdd(row))
