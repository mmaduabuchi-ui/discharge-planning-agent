def generate_patient_friendly_summary(data):
    """
    Free LLM-style explanation layer (no API required)
    Converts structured clinical output into human-readable language.
    """

    summary = data.get("summary", "")
    instructions = data.get("instructions", "")
    risk = data.get("risk_level", "")
    follow_up = data.get("follow_up", "")

    # 🧠 Simple intelligent formatting (LLM-like behavior)
    explanation = f"""
    👨‍⚕️ DISCHARGE SUMMARY (SIMPLIFIED)

    What happened:
    {summary}

    What you should do:
    {instructions}

    Risk level:
    Your readmission risk is classified as: {risk}

    Follow-up plan:
    {follow_up}

    ⚠️ Note: Please follow instructions carefully and contact a healthcare provider if symptoms worsen.
    """

    return explanation.strip()