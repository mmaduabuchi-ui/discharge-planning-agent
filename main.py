from fastapi import FastAPI
from fhir.client import get_patient, get_conditions, get_medications
from agent.discharge_agent import generate_discharge_summary

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Healthcare AI Agent Running 🚀"}


@app.get("/discharge-summary/{patient_id}")
def discharge_summary(patient_id: str):
    patient = get_patient(patient_id)
    conditions = get_conditions(patient_id)
    meds = get_medications(patient_id)

    result = generate_discharge_summary(patient, conditions, meds)

    return result