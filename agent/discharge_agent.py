from mcp.risk_tool import readmission_risk
from agent.patient_explainer import generate_patient_friendly_summary


def generate_discharge_summary(patient, conditions, meds):
    """
    Core discharge agent logic
    """

    # 🧠 Extract age safely (FHIR can vary)
    age = 50  # default fallback

    try:
        if "birthDate" in patient:
            birth_year = int(patient["birthDate"][:4])
            age = 2026 - birth_year
    except:
        pass

    # 🔌 MCP TOOL CALL
    risk = readmission_risk(age, conditions, meds)

    # 🏥 Clinical summary
    condition_text = ", ".join(conditions) if conditions else "general condition"

    summary = f"Patient was treated for: {condition_text}."

    instructions = (
        "Take medications as prescribed. "
        "Rest, stay hydrated, and monitor symptoms."
    )

    follow_up = "Visit clinic within 5–7 days."

    # 🔹 Structured output (for systems / clinicians)
    raw_output = {
        "summary": summary,
        "instructions": instructions,
        "risk_level": risk,
        "follow_up": follow_up
    }

    # 🔹 Patient-friendly explanation (FREE LLM-style layer)
    patient_friendly = generate_patient_friendly_summary(raw_output)

    return {
        "structured": raw_output,
        "patient_friendly": patient_friendly
    }