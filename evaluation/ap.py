from sklearn.metrics import (
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

import pandas as pd
from collections import Counter


class Evaluator:

    def evaluate(self, y_true, y_pred):

        print("\n==============================")
        print("NER SYSTEM EVALUATION METRICS")
        print("==============================\n")

        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average="macro", zero_division=0)
        recall = recall_score(y_true, y_pred, average="macro", zero_division=0)
        f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)

        error_rate = 1 - accuracy

        print("Accuracy :", round(accuracy,4))
        print("Precision :", round(precision,4))
        print("Recall :", round(recall,4))
        print("F1 Score :", round(f1,4))
        print("Error Rate :", round(error_rate,4))


        print("\n==============================")
        print("CLASSIFICATION REPORT")
        print("==============================\n")

        print(classification_report(y_true, y_pred, zero_division=0))


        print("\n==============================")
        print("CONFUSION MATRIX")
        print("==============================\n")

        labels = sorted(list(set(y_true)))

        cm = confusion_matrix(y_true, y_pred, labels=labels)

        cm_df = pd.DataFrame(cm, index=labels, columns=labels)

        print(cm_df)


        print("\n==============================")
        print("ENTITY DISTRIBUTION (TRUE)")
        print("==============================\n")

        true_counts = Counter(y_true)

        df_true = pd.DataFrame.from_dict(true_counts, orient="index", columns=["Count"])

        print(df_true)


        print("\n==============================")
        print("ENTITY DISTRIBUTION (PREDICTED)")
        print("==============================\n")

        pred_counts = Counter(y_pred)

        df_pred = pd.DataFrame.from_dict(pred_counts, orient="index", columns=["Count"])

        print(df_pred)


if __name__ == "__main__":

    y_true = [
        "PERSON","KING","POET","PROFESSION","WARRIOR",
        "TRIBE","PLACE","REGION","MOUNTAIN","FOREST",
        "FIELD","WATERBODY","DESERT","ANIMAL","BIRD",
        "INSECT","FISH","PLANT","FLOWER","FOOD"
    ]

    y_pred = [
        "PERSON","KING","POET","PROFESSION","WARRIOR",
        "TRIBE","PLACE","REGION","MOUNTAIN","FOREST",
        "FIELD","WATERBODY","DESERT","ANIMAL","BIRD",
        "INSECT","FISH","PLANT","PLANT","FOOD"
    ]

    evaluator = Evaluator()

    evaluator.evaluate(y_true, y_pred)