from fhir.client import get_patient, get_conditions, get_medications
from mcp.risk_tool import readmission_risk


def build_discharge_summary(patient_id: str):
    """
    Creates a structured discharge summary from FHIR data
    + includes readmission risk scoring
    """

    patient = get_patient(patient_id)
    conditions = get_conditions(patient_id)
    medications = get_medications(patient_id)

    name = "Unknown Patient"

    try:
        name = patient["name"][0]["text"]
    except:
        pass

    # Temporary age (we will extract from FHIR later)
    age = 70

    # 🔧 MCP TOOL CALL
    risk = readmission_risk(age, conditions, medications)

    return {
        "patient_name": name,
        "patient_id": patient_id,
        "conditions": conditions if conditions else ["No recorded conditions"],
        "medications": medications if medications else ["No medications recorded"],
        "discharge_plan": generate_plan(conditions, medications),
        "readmission_risk": risk
    }


def generate_plan(conditions, medications):
    if not conditions and not medications:
        return "Patient is stable. Routine follow-up recommended."

    if "diabetes" in str(conditions).lower():
        return "Recommend glucose monitoring and diet control follow-up."

    if "hypertension" in str(conditions).lower():
        return "Recommend blood pressure monitoring and medication adherence."

    return "Follow-up visit recommended within 2 weeks."