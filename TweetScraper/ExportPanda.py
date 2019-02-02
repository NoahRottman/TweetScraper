import pandas as pd
import glob
import json

files = glob.glob('tweet/*')
#files = glob.glob('user/*')
len(files)

dictlist = []

for file in files:
    json_string = open(file, 'r').read()
    json_dict = json.loads(json_string)
    dictlist.append(json_dict)

df = pd.DataFrame(dictlist)

df = df.replace({'\n': ' '}, regex=True)  # remove linebreaks in the dataframe
df = df.replace({'\t': ' '}, regex=True)  # remove tabs in the dataframe
df = df.replace({'\r': ' '}, regex=True)  # remove carriage return in the dataframe

df

# Export to csv
df.to_csv("data.csv")