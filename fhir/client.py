import requests

BASE_URL = "https://hapi.fhir.org/baseR4"


def get_patient(patient_id):
    url = f"{BASE_URL}/Patient/{patient_id}"
    response = requests.get(url)
    return response.json()


def get_conditions(patient_id):
    url = f"{BASE_URL}/Condition?patient={patient_id}"
    data = requests.get(url).json()

    conditions = []

    for entry in data.get("entry", []):
        try:
            resource = entry.get("resource", {})
            code = resource.get("code", {})
            text = code.get("text")
            if text:
                conditions.append(text)
        except:
            continue

    return conditions


def get_medications(patient_id):
    url = f"{BASE_URL}/MedicationRequest?patient={patient_id}"
    data = requests.get(url).json()

    meds = []

    for entry in data.get("entry", []):
        try:
            resource = entry.get("resource", {})
            med = resource.get("medicationCodeableConcept", {})
            text = med.get("text")
            if text:
                meds.append(text)
        except:
            continue

    return meds