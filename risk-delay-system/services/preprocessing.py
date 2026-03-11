import pandas as pd

def preprocess_input(data_dict):
    df = pd.DataFrame([data_dict])
    return df