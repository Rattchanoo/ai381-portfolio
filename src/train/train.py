import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    # قراءة البيانات
    matches = pd.read_csv('matches.csv', index_col=0)
    matches["date"] = pd.to_datetime(matches["date"])
    matches["venue_code"] = matches["venue"].astype("category").cat.codes
    matches["opp_code"] = matches["opponent"].astype("category").cat.codes
    matches["target"] = (matches["result"] == "W").astype("int")

    # تحديد المتغيرات (Features) وتدريب النموذج
    predictors = ["venue_code", "opp_code"]
    train = matches[matches["date"] < '2022-01-01']
    
    rf = RandomForestClassifier(n_estimators=50, min_samples_split=10, random_state=1)
    rf.fit(train[predictors], train["target"])

    # حفظ الموديل الناتج
    os.makedirs("src/app", exist_ok=True)
    with open("src/app/model.pkl", "wb") as f:
        pickle.dump(rf, f)
    
    print("Model trained and saved successfully!")
import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    # قراءة البيانات
    matches = pd.read_csv('matches.csv', index_col=0)
    matches["date"] = pd.to_datetime(matches["date"])
    matches["venue_code"] = matches["venue"].astype("category").cat.codes
    matches["opp_code"] = matches["opponent"].astype("category").cat.codes
    matches["target"] = (matches["result"] == "W").astype("int")

    # تحديد المتغيرات (Features) وتدريب النموذج
    predictors = ["venue_code", "opp_code"]
    train = matches[matches["date"] < '2022-01-01']
    
    rf = RandomForestClassifier(n_estimators=50, min_samples_split=10, random_state=1)
    rf.fit(train[predictors], train["target"])

    # حفظ الموديل الناتج
    os.makedirs("src/app", exist_ok=True)
    with open("src/app/model.pkl", "wb") as f:
        pickle.dump(rf, f)
    
    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_model()

if __name__ == "__main__":
    train_model()
