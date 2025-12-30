import pandas as pd

def load_processed_data():
    data = pd.read_csv('../data/processed/processed_fraud_data.csv')
    X = data.drop('class', axis=1)
    y = data['class']
    return X, y