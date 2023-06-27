import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

from starter.ml.data import process_data
from starter.ml.model import train_model, compute_model_metrics, inference, compute_model_slice_metrics
from starter.ml.census_category import CATEGORY_FEATURES

data = pd.read_csv("data/census_cleaned.csv")

train, test = train_test_split(data, test_size=0.20)

X_train, y_train, encoder, lb = process_data(
    train, 
    categorical_features=CATEGORY_FEATURES, 
    label="salary", 
    training=True
)

X_test, y_test, _, _ = process_data(
    test, 
    categorical_features=CATEGORY_FEATURES, 
    label="salary", 
    training=False, 
    encoder=encoder, 
    lb=lb
)

model = train_model(X_train, y_train)

with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/encoder.pkl', 'wb') as f:
    pickle.dump(encoder, f)

with open('model/lb.pkl', 'wb') as f:
    pickle.dump(lb, f)


y_preds = inference(model, X_test)
precision, recall, fbeta = compute_model_metrics(y_test, y_preds)
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F-beta: {fbeta}")

compute_model_slice_metrics(model, test, "education", encoder, lb, CATEGORY_FEATURES)
