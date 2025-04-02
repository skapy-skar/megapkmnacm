import pandas as pd

def csv(df):
    df["Mega_Evolution"]=df["Name"].apply(lambda x: "Yes" if "Mega" in x and x != "Meganium" else "No")
    keepem=["#","Name","Mega_Evolution"]
    numstuff=["HP","Attack","Defense","Sp. Atk","Sp. Def","Speed"]
    dfp=pd.concat([df[keepem],df[numstuff]],axis=1)
    return dfp

# fp=r"C:\Users\Aayush Dwivedi\Desktop\Python\MegaTask\Pokemon.csv"
# df=pd.read_csv(fp)
# dfp=csv(df)
# print(dfp.head())
# print(dfp["Mega_Evolution"].value_counts())
# dfp.to_csv("processed_data.csv",index=False)
# print("save op!")
