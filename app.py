from flask import Flask, render_template, request, send_file
import os

from agents.analyzer import analyze_code
from agents.test_generator import generate_test_cases
from agents.bug_detector import detect_bugs
from agents.report_generator import create_report
from agents.documentation_agent import generate_documentation
from agents.metrics import calculate_metrics
from agents.quality_analyzer import calculate_quality

from database import (
    init_db,
    save_analysis,
    get_history
)

app = Flask(__name__)

init_db()

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["REPORT_FOLDER"] = REPORT_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "codefile" not in request.files:
        return "No file selected or form not submitted correctly."

    file = request.files["codefile"]

    if file.filename == "":
        return "Please select a Python file."

    filename = file.filename

    if filename.endswith(".py.py"):
        filename = filename.replace(".py.py", ".py")

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # Agent 1
    functions = analyze_code(filepath)

    # Agent 2
    test_cases = generate_test_cases(functions)

    # Agent 3
    bug_report = detect_bugs(functions)

    # Agent 4
    documentation = generate_documentation(functions)

    # Agent 5
    metrics = calculate_metrics(
        filepath,
        functions
    )

    # Agent 6
    quality = calculate_quality(metrics)

    save_analysis(
        filename,
        len(functions),
        quality["score"],
        bug_report["risk_level"]
    )

    report_path = os.path.join(
        app.config["REPORT_FOLDER"],
        "Testing_Report.docx"
    )

    # Agent 7
    create_report(
        functions,
        test_cases,
        bug_report,
        report_path
    )

    return render_template(
        "result.html",
        functions=functions,
        test_cases=test_cases,
        bug_report=bug_report,
        documentation=documentation,
        metrics=metrics,
        quality=quality
    )


@app.route("/download-report")
def download_report():

    report_path = os.path.join(
        app.config["REPORT_FOLDER"],
        "Testing_Report.docx"
    )

    if not os.path.exists(report_path):
        return "Report not found."

    return send_file(
        report_path,
        as_attachment=True
    )


@app.route("/history")
def history():

    history_data = get_history()

    return render_template(
        "history.html",
        history=history_data
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        use_reloader=False
    )