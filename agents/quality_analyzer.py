def calculate_quality(metrics):

    score = 100

    if metrics["comments"] == 0:
        score -= 10

    if metrics["lines"] > 50:
        score -= 10

    if metrics["complexity"] == "MEDIUM":
        score -= 10

    if metrics["complexity"] == "HIGH":
        score -= 20

    if score >= 90:
        maintainability = "Excellent"
    elif score >= 75:
        maintainability = "Good"
    else:
        maintainability = "Needs Improvement"

    recommendations = []

    if metrics["comments"] == 0:
        recommendations.append(
            "Add comments for better documentation."
        )

    if metrics["functions"] > 10:
        recommendations.append(
            "Split code into smaller modules."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Code structure looks good."
        )

    return {
        "score": score,
        "maintainability": maintainability,
        "recommendations": recommendations
    }