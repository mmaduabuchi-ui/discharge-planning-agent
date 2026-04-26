def readmission_risk(age, conditions, meds):
    """
    Simple heuristic risk scoring for hospital readmission
    """

    score = 0

    if age and age > 65:
        score += 2

    if conditions and len(conditions) > 1:
        score += 1

    if meds and len(meds) >= 3:
        score += 1

    if score >= 3:
        return "High"
    elif score == 2:
        return "Medium"
    else:
        return "Low"