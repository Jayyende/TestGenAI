def calculate_metrics(filepath, functions):

    with open(filepath, "r", encoding="utf-8") as file:
        code = file.readlines()

    total_lines = len(code)

    comments = 0

    for line in code:
        if line.strip().startswith("#"):
            comments += 1

    if total_lines < 30:
        complexity = "LOW"

    elif total_lines < 80:
        complexity = "MEDIUM"

    else:
        complexity = "HIGH"

    return {
        "lines": total_lines,
        "functions": len(functions),
        "comments": comments,
        "complexity": complexity
    }