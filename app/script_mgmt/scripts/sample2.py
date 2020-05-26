import pandas as pd

def main(file):
    return sample2(file)

def sample2(file):
    if file.filename.endswith('csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith('xlsx'):
        df = pd.read_excel(file)
    return df
