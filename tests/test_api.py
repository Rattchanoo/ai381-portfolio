from fastapi.testclient import TestClient
from src.app.main import app, model

client = TestClient(app)

def test_health_check():
    """1. اختبار فحص حالة السيرفر"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_model_loaded():
    """2. اختبار التأكد من تحميل الموديل بنجاح"""
    assert model is not None

def test_predict_endpoint_success():
    """3. اختبار التنبؤ بمدخلات صحيحة وتأكد العقد (API Contract)"""
    response = client.post("/predict", json={"venue_code": 1, "opp_code": 10})
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "confidence" in data

def test_input_schema_validation():
    """4. اختبار مخطط المدخلات وإرسال بيانات ناقصة أو خاطئة النوع"""
    response = client.post("/predict", json={"venue_code": "invalid_string", "opp_code": 5})
    # يجب أن يرفضها FastAPI ويعيد خطأ 422
    assert response.status_code == 422

def test_deterministic_prediction():
    """5. اختبار التنبؤ الحتمي الثابت لنفس المدخلات المتكررة"""
    payload = {"venue_code": 0, "opp_code": 3}
    res1 = client.post("/predict", json=payload).json()
    res2 = client.post("/predict", json=payload).json()
    assert res1["prediction"] == res2["prediction"]
