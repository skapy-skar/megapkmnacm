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
pandas:used for manipulating data
OneHotEncoder:converts category data like "type" into a format ML models can use
StandardScaler:to make numerical data normal to improve training 

prep_data(df) function -
 a)keepem = ["#", "Name", "Mega_Evolution"]
   keepem = [c for c in keepem if c in df.columns]
--->keeps only the columns that exist in df.

 b)numstuff = df.select_dtypes(include=["number"])
 --->selects all numeric columns for standardization

  c)catstuff = ["Type 1", "Type 2", "Generation"]
    catstuff = [c for c in catstuff if c in df.columns]
  --->categorical columns are stored in catstuff

d)enc = pd.get_dummies(df[catstuff], drop_first=True)
pd.get_dummies():categorical variables into binary(onehotencoder).
drop_first=True:prevents repetition by dropping the first category.

e)dfp = pd.concat([df[keepem], numstuff, enc], axis=1)
  return dfp
combines necessary columns into dfp
returns the managed dataset

f)fp = r"C:\Users\Aayush Dwivedi\Desktop\Python\MegaTask\Pokemon.csv"
  df = pd.read_csv(fp):reads the dataset
  dfp = prep_data(df.copy()):processes it using prep_data()
  dfp.to_csv("processed_data.csv", index=False):saves it as processed_data.csv
  print("save op!")








      3)pkmnmastertraining,py
from sklearn.model_selection import train_test_split ====to split data into training and testing parts
from sklearn.linear_model import LogisticRegression ====for making the lr model

train_pkmn(df) function:
   df = df.drop(columns=dropclmn)
   --drops the columns which are not needed which is name clmn and serial num clmn

   x = df.drop(columns=["Mega_Evolution"])-has everything except mega evos
   y = df["Mega_Evolution"]-mega evo only

   xtr, xte, ytr, yte = train_test_split(x, y, test_size=0.2, random_state=42)
   spliting x and y to 80percent train and 20% test data.
   random_state=42: Ensures the same split every time.

   trainer = LogisticRegression(max_iter=2000)
   trainer.fit(xtr, ytr)
   creates a lr model
   trains it using xtr and ytr

   return trainer, xte, yte
   returns the trained model and test data







   4)
