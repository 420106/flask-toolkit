import pandas as pd

def main(file):
    return spreadsheet_mask(file)

def spreadsheet_mask(file):
    if file.filename.endswith('csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith('xlsx'):
        df = pd.read_excel(file)
    df['Customer Name'] = 'MASKED NAME'
    df['Postal Address'] = 'MASKED ADDRESS'
    df['Email'] = 'MASKED@email.com'
    return df
