from fastapi import FastAPI

app = FastAPI()

patients = {

{
  "shamira_smith": {
    "info": {
      "name": "Shamira Smith",
      "age": 34,
      "sex": "female"
    },
    "history": [],
    "medications": [
      {
        "name": "Metformin",
        "dose": "500mg",
        "frequency": "twice daily"
      },
      {
        "name": "Lisinopril",
        "dose": "10mg",
        "frequency": "once daily"
      }
    ],
    "mood": [
      "Frustrated",
      "Angry"
    ],
    "current_feeling": {
      "feelings": [
        "Exhausted",
        "Achy"
      ],
      "duration": "2 days"
    },
    "symptoms": [
      "Cough",
      "Shortness of breath"
    ],
    "cough": [
      "Coughing up green sputum"
    ],
    "sputum": [
      "Green sputum"
    ],
    "appetite": [
      "Hungry"
    ],
    "occupation": "Recruitment Manager",
    "spouse": [
      {
        "name": "John",
        "type": "Husband"
      }
    ],
    "dependants": [
      {
        "name": "Sam",
        "type": "Son"
      },
      {
        "name": "Michelle",
        "type": "Daughter"
      }
    ],
    "phases": {
      "1": {
        "status": "stable",
        "symptoms": [
          "Cough",
          "Shortness of breath",
          "Fatigue",
          "Body aches"
        ],
        "mood": [
          "Frustrated",
          "Angry"
        ],
        "vitals": {
          "heart_rate": null,
          "blood_pressure": null,
          "respiratory_rate": null,
          "oxygen_saturation": null,
          "temperature": null
        }
      },
      "2": {
        "status": "deteriorating",
        "symptoms": [
          "Cough",
          "Worsening shortness of breath",
          "Fatigue",
          "Body aches"
        ],
        "mood": [
          "Frustrated",
          "Anxious"
        ],
        "vitals": {
          "heart_rate": null,
          "blood_pressure": null,
          "respiratory_rate": null,
          "oxygen_saturation": null,
          "temperature": null
        }
      }
    }
  },
  "john_jones": {
    "info": {
      "name": "John Jones",
      "age": 54,
      "sex": "male"
    },
    "history": [
      "Type 2 diabetes",
      "Hypertension"
    ],
    "medications": [
      {
        "name": "Metformin",
        "dose": null,
        "frequency": null
      },
      {
        "name": "Lisinopril",
        "dose": null,
        "frequency": null
      }
    ],
    "mood": [
      "Concerned",
      "Anxious"
    ],
    "current_feeling": {
      "feelings": [
        "Chest discomfort"
      ],
      "duration": null
    },
    "symptoms": [
      "Chest discomfort"
    ],
    "cough": [],
    "sputum": [],
    "appetite": [],
    "occupation": null,
    "spouse": [],
    "dependants": [],
    "phases": {
      "1": {
        "status": "stable",
        "symptoms": [
          "Mild chest discomfort"
        ],
        "mood": [
          "Concerned"
        ],
        "vitals": {
          "heart_rate": 82,
          "blood_pressure": "130/85",
          "respiratory_rate": 16,
          "oxygen_saturation": 98,
          "temperature": null
        }
      },
      "2": {
        "status": "deteriorating",
        "symptoms": [
          "Severe chest pain",
          "Shortness of breath"
        ],
        "mood": [
          "Anxious"
        ],
        "vitals": {
          "heart_rate": 125,
          "blood_pressure": "90/60",
          "respiratory_rate": 28,
          "oxygen_saturation": 91,
          "temperature": null
        }
      }
    }
  }
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
