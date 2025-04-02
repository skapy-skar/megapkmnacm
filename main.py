import pandas as pd
from csvfile import csv
from pkmnmastertraining import train_pkmn
from modelcheck import evalmod

fp=r"C:\Users\Aayush Dwivedi\Desktop\Python\MegaTask\Pokemon.csv"
df=pd.read_csv(fp)
dfp=csv(df)
trainer,xte,yte=train_pkmn(dfp)
print("Your Pokémons are ready :)))")
evalmod(trainer,xte,yte)
predictions=pd.DataFrame({"Name":dfp.loc[xte.index,"Name"],"Predicted_Mega_Evolution":trainer.predict(xte)})
predictions.to_csv("final_predictions.csv", index=False)
print("Predictions saved!")
