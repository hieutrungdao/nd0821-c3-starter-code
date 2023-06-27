from lightgbm import LGBMClassifier
from sklearn.metrics import fbeta_score, precision_score, recall_score

from starter.ml.data import process_data


# Optional: implement hyperparameter tuning.
def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """
    model = LGBMClassifier()
    model.fit(X_train, y_train)
    return model


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    return model.predict(X)

def compute_model_slice_metrics(model, df, feature_name, encoder, lb, cat_feats, output_path="slice_output.txt"):
    for unique_value in df[feature_name].unique():
        slice = df[df[feature_name] == unique_value]
        X_test, y_test, _, _ = process_data(
            slice, 
            cat_feats, 
            label="salary", 
            training=False, 
            encoder=encoder, 
            lb=lb
        )
        y_preds = inference(model, X_test)

        precision, recall, fbeta = compute_model_metrics(y_test, y_preds)

        with open(output_path, 'a') as f:
            f.write(f"Slice of feature {feature_name} with value {unique_value}: \n")
            f.write(f"\tPrecision: {precision}\n")
            f.write(f"\tRecall: {recall}\n") 
            f.write(f"\tF-beta: {fbeta}\n")
            f.write("\n")
