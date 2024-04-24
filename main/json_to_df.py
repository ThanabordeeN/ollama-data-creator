import pandas as pd
import json
import os

def convert_to_csv():
    directory = 'output_data'
    dfs = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath) as f:
                data = json.load(f)
            df = pd.DataFrame(data)
            dfs.append(df)
    combined_df = pd.concat(dfs)
    combined_df.to_csv('csv_output\combined_data.csv', index=False)


