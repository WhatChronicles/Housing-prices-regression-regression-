import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def train_model():
    df = pd.read_csv("data/train.csv")
    target = "price"
    categorical_cols = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"]
    numeric_cols = ["area", "bedrooms", "bathrooms", "stories", "parking"]

    df = df.dropna(subset=[target] + numeric_cols)

    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le

    X = df[categorical_cols + numeric_cols]
    y = df[target]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/best_model.pkl")
    joblib.dump(encoders, "models/label_encoders.pkl")

    return model, encoders

if __name__ == "__main__":
    train_model()