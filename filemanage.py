import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def prep_data(df):
    keepem = ["#", "Name", "Mega_Evolution"]
    keepem = [c for c in keepem if c in df.columns]
    numstuff = df.select_dtypes(include=["number"])
    catstuff = ["Type 1", "Type 2", "Generation"]
    catstuff = [c for c in catstuff if c in df.columns]
    enc = pd.get_dummies(df[catstuff], drop_first=True)
    dfp = pd.concat([df[keepem], numstuff, enc], axis=1)
    return dfp

fp = r"C:\Users\Aayush Dwivedi\Desktop\Python\MegaTask\Pokemon.csv"
df = pd.read_csv(fp)
dfp = prep_data(df.copy())
dfp.to_csv("processed_data.csv", index=False)
print("save op!")