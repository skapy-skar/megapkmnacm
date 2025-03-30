import numpy as np
from csvfile import load_data
from filemanage import prep_data
from pkmnmastertraining import train_pkmn
from modelcheck import evalmod

fp = r"C:\Users\Aayush Dwivedi\Desktop\Python\MegaTask\Pokemon.csv"
df = load_data(fp)
dfp = prep_data(df)
print("Yo labels before training:", np.unique(dfp["Mega_Evolution"]))
trainer, xte, yte = train_pkmn(dfp)
print("Your Pokémons are ready :)))")
evalmod(trainer, xte, yte)
