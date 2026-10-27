
import json
from pathlib import Path

from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Medical Patient Simulation API"
)

# Load patients from patients.json
PATIENTS_FILE = Path(__file__).with_name("patients.json")

with open(PATIENTS_FILE, "r", encoding="utf-8") as file:
    patients = json.load(file)


# ---------------------------------
# HELPER FUNCTIONS
# ---------------------------------

def get_patient_data(patient_id: str):
    patient = patients.get(patient_id)

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


def get_current_phase(patient):
    # For now, use phase 1 by default.
    # Later, each consultation will have
    # its own independently tracked phase.
    return patient["phases"]["1"]


# ---------------------------------
# API STATUS
# ---------------------------------

@app.get("/")
def root():
    return {"status": "API running"}


# ---------------------------------
# LIST PATIENTS
# ---------------------------------

@app.get("/patients")
def list_patients():
    return [
        {
            "id": patient_id,
            "name": patient["info"]["name"],
            "age": patient["info"]["age"]
        }
        for patient_id, patient in patients.items()
    ]


# ---------------------------------
# FULL PATIENT INFORMATION
# ---------------------------------

@app.get("/patient/{id}")
def get_patient(id: str):
    patient = get_patient_data(id)
    phase = get_current_phase(patient)

    return {
        **{
            key: value
            for key, value in patient.items()
            if key not in ("phases", "symptoms", "mood")
        },
        "symptoms": phase.get("symptoms", []),
        "mood": phase.get("mood", []),
        "vitals": phase.get("vitals", {}),
        "status": phase.get("status", "unknown")
    }


# ---------------------------------
# VITAL SIGNS
# ---------------------------------

@app.get("/patient/{id}/vitals")
def get_vitals(id: str):
    patient = get_patient_data(id)
    phase = get_current_phase(patient)

    return phase.get("vitals", {})


# ---------------------------------
# LAB RESULTS
# ---------------------------------

@app.get("/patient/{id}/labs")
def get_labs(id: str):
    patient = get_patient_data(id)

    return patient.get("labs", {})


# ---------------------------------
# MEDICATIONS
# ---------------------------------

@app.get("/patient/{id}/medications")
def get_medications(id: str):
    patient = get_patient_data(id)

    return patient.get("medications", [])


# ---------------------------------
# MEDICAL HISTORY
# ---------------------------------

@app.get("/patient/{id}/history")
def get_history(id: str):
    patient = get_patient_data(id)

    return patient.get("history", [])


# ---------------------------------
# CURRENT SYMPTOMS
# ---------------------------------

@app.get("/patient/{id}/symptoms")
def get_symptoms(id: str):
    patient = get_patient_data(id)
    phase = get_current_phase(patient)

    return {
        "symptoms": phase.get("symptoms", []),
        "mood": phase.get("mood", []),
        "status": phase.get("status", "unknown")
    }
