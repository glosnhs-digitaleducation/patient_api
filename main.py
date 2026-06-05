from fastapi import FastAPI

app = FastAPI()

patients = {
    "shamira_smith": {
        "name": "Shamira Smith",
        "age": 34,
        "medications": [
        {"name": "Metformin", "dose": "500mg", "frequency": "2 daily"},
        {"name": "Lisinopril", "dose": "500mg", "frequency": "once a day"}
        ],
        "mood": ["Frustrated", "Angry"],
        "current_feeling" : [
            {"feeling": "Exhausted", "Achy"},
            {"duration": "2 days"},
        ],
        "symptoms" : ["Cough", "Out of breath"],
        "cough" : ["Coughing up green sputum"],
        "sputum" : ["Coughing up green sputum"],
        "appetite": ["Hungry"],
        "occupation": "Recruitment Manager",
        "spouse": [
            {"name": "John", "type":"Husband"}
        ],
        "dependants": [
          {"name": "Sam", "type": "Son"},
          {"name": "Michelle", "type": "Daughter"}
        ]
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
