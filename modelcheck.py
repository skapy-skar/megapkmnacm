import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_recall_curve

def evalmod(trainer, xte, yte):
    ytb = (yte == "Yes").astype(int)
    yhat = trainer.predict(xte)
    ypb = (yhat == "Yes").astype(int)
    print("Yo, predictions be like:", np.unique(ypb))

    cm = confusion_matrix(ytb, ypb)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Regular", "Mega"], yticklabels=["Regular", "Mega"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()

    if hasattr(trainer, "predict_proba"):
        y_probs = trainer.predict_proba(xte)[:, 1]
        fpr, tpr, _ = roc_curve(ytb, y_probs)
        roc_auc = auc(fpr, tpr)
        plt.figure(figsize=(6, 4))
        plt.plot(fpr, tpr, color="b", label=f"ROC (AUC = {roc_auc:.2f})")
        plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC Curve")
        plt.legend()
        plt.show()

        prec, rec, _ = precision_recall_curve(ytb, y_probs)
        plt.figure(figsize=(6, 4))
        plt.plot(rec, prec, color="g", label="Precision-Recall Curve")
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        plt.title("Precision-Recall Curve")
        plt.legend()
        plt.show()
    else:
        print("Np predictions,ROC,PRC skip")