import pandas as pd

def main(file):
    return sample2(file)

def sample2(file):
    df = pd.read_csv(file)
    return df
