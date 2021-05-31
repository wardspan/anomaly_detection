#!/usr/bin/env python3
"""
Author: Ward Spangenberg
Email: wardspan@mac.com
Date: May 31, 2021
Purpose: 

"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from joblib import load


# --------------------------------------------------------------
app = FastAPI()
iso_forest = load("model.joblib")


# --------------------------------------------------------------
class PredictionRequest(BaseModel):
    feature_vector: List[float]
    score: Optional[bool] = False

# --------------------------------------------------------------
@app.post("/prediction")
def predict(req: PredictionRequest):
    prediction = iso_forest.predict([req.feature_vector])
    response = {"is_inlier": int(prediction[0])}

    if req.score is True:
        score = iso_forest.score_samples([req.feature_vector])
        response["anomaly_score"] = score[0]

    return response

# --------------------------------------------------------------
@app.get("/model_information")
def model_information():
    return iso_forest.get_params()

# --------------------------------------------------------------
if __name__ == '__main__':
    print("running...")