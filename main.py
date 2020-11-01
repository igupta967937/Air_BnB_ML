import os
import pandas as pd


DATA_PATH = '../data/'


def load_airbnb_data(path=DATA_PATH):
    print('hey ya')
    csv_path = os.path.join(path, 'BristolAirbnbListings.csv')
    return pd.read_csv(csv_path)


data = load_airbnb_data()
data.head()

