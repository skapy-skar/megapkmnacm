hvnt completed the readme file yet



other than that.....am not sure if i did what was asked....cuz i ended up using the names only.....but cudnt see any other way around so anyways
   
   okay so ig i'll explain whatever i did



   1)csvfile.py
pandas:this is a data analyzing library
fp:this is the file path of the CSV dataset.
pd.read_csv(fp):reads the CSV file and stores it in a pandas(df).
df["Name"].apply(lambda x: "Yes" if "Mega" in x else "No"):this checks if "Mega" is in the Pokemon's name
if "Mega" is found, it labels it "Yes", otherwise "No".the result goes to Mega_Evolution

df.drop(columns=["#", "Name"], inplace=True)
this removes index number and column names because they're unnecessary for training
inplace=True: ensures changes apply directly to df without needing to reassign it

return df:returns the edited dataset

fp:stores the path to the Pokemon dataset

df = load_data(fp):loads the dataset and processes it

df.head():displays the first few rows

df["Mega_Evolution"].value_counts():counts how many "Yes" and "No" labels exist



    2)filemanage.py
