import os
import pickle
import pandas as pd
from fastapi import FastAPI

from starter.ml.data import process_data
from starter.ml.model import inference
from starter.ml.census_category import CATEGORY_FEATURES
from starter.api.model import RequestRecord, ReponseRecord


model_path = "model/model.pkl"
encoder_path = "model/encoder.pkl"
lb_path = "model/lb.pkl"

model = pickle.load(open(model_path, 'rb'))
encoder = pickle.load(open(encoder_path, 'rb'))
lb = pickle.load(open(lb_path, 'rb'))

app = FastAPI(title="Udacity Project 3")


@app.get('/')
async def root():
    return "Welcome"


@app.post('/predictions', response_model=ReponseRecord)
async def predict(req: RequestRecord):

    record = {key.replace('_', '-'): [value] for key, value in req.__dict__.items()}

    input_df = pd.DataFrame.from_dict(record)

    input_record, _, _, _ = process_data(
        input_df,
        categorical_features=CATEGORY_FEATURES,
        label=None,
        training=False,
        encoder=encoder,
        lb=lb
    )

    out = inference(model=model, X=input_record)
    return ReponseRecord(prediction=lb.inverse_transform(out)[0])
    

