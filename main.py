from fastapi import FastAPI

app = FastAPI()

patients = {
    "john_smith": {
        "age": 54,
        "vitals": {"heart_rate": 82, "blood_pressure": "130/85"},
        "labs": {"HbA1c": "8.2%"},
        "medications": ["Metformin", "Lisinopril"]
    }
}

@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/patient/{id}")
def get_patient(id: str):
    return patients.get(id)

@app.get("/patient/{id}/vitals")
def get_vitals(id: str):
    return patients[id]["vitals"]

@app.get("/patient/{id}/labs")
def get_labs(id: str):
    return patients[id]["labs"]

@app.get("/patient/{id}/medications")
def get_medications(id: str):
    return patients[id]["medications"]
