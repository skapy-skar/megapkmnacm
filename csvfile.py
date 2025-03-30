import pandas as pd

def load_data(fp):
    df = pd.read_csv(fp)
    df["Mega_Evolution"] = df["Name"].apply(lambda x: "Yes" if "Mega" in x else "No")
    df.drop(columns=["#", "Name"], inplace=True)
    return df

fp = r"C:\Users\Aayush Dwivedi\Desktop\Python\MegaTask\Pokemon.csv"
df = load_data(fp)
print(df.head())
print(df["Mega_Evolution"].value_counts())