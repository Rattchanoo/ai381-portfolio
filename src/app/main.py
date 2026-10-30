import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Football Match Prediction API")

# تحميل الموديل
try:
    with open("src/app/model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception:
    model = None

class MatchInput(BaseModel):
    venue_code: int = Field(..., description="Venue code (e.g. 0 or 1)")
    opp_code: int = Field(..., description="Opponent code")

@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict")
def predict_match(data: MatchInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    features = [[data.venue_code, data.opp_code]]
    prediction = model.predict(features)
    probability = model.predict_proba(features)
    
    result = "Win" if int(prediction[0]) == 1 else "Not Win"
    confidence = float(max(probability[0]))
    
    return {"prediction": result, "confidence": confidence}
