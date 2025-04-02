from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_pkmn(df):
    drop=["#","Name"]
    df=df.drop(columns=drop)
    x=df.drop(columns=["Mega_Evolution"])
    y=df["Mega_Evolution"]
    print(y.value_counts())
    xtr,xte,ytr,yte=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
    trainer=LogisticRegression(max_iter=2000)
    trainer.fit(xtr,ytr)
    return trainer,xte,yte
