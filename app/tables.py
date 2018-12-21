import pandas as pd
import os

path = os.path.abspath(os.path.dirname(__file__))


def hittingData(d=','):
    url = path + '/static/data/redsox_2018_hitting.txt'
    df = pd.read_csv(url, sep=d)

    # return dataframe as html using pandas .to_html() method
    return df.to_html()
