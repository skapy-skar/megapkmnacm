import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_pkmn(df):
    dropclmn = ["#", "Name"]
    dropclmn = [c for c in dropclmn if c in df.columns]
    df = df.drop(columns=dropclmn)
    x = df.drop(columns=["Mega_Evolution"])
    y = df["Mega_Evolution"]
    xtr, xte, ytr, yte = train_test_split(x, y, test_size=0.2, random_state=42)
    trainer = LogisticRegression(max_iter=2000)
    trainer.fit(xtr, ytr)
    return trainer, xte, yte