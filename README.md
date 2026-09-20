# 🤖 TestGenAI - AI Software Testing Assistant

## 📌 Project Overview

TestGenAI is an AI-powered Software Testing Assistance platform developed using Python, Flask, SQLite, HTML, CSS, and Google Gemini AI.

The system automatically analyzes Python source code, generates test cases, detects potential bugs, evaluates code quality, calculates software metrics, generates documentation, and creates testing reports.

This project is developed as a Flexi Credit Mini Project under Agentic AI & Automation.

---

## 🎯 Project Objectives

- Automate source code analysis
- Generate software test cases
- Detect potential bugs and runtime issues
- Improve code quality assessment
- Generate function documentation
- Create professional testing reports
- Store analysis history

---

## 🚀 Features

### Code Analyzer Agent
Analyzes uploaded Python source code and extracts functions.

### Test Generator Agent
Generates test cases automatically for detected functions.

### Bug Detector Agent
Uses Google Gemini AI to identify:
- Possible bugs
- Runtime issues
- Input validation issues
- Improvement suggestions

### Documentation Agent
Generates function descriptions automatically.

### Metrics Agent
Calculates:
- Lines of Code
- Number of Functions
- Number of Comments
- Complexity Level

### Quality Assessment Agent
Evaluates maintainability and code quality score.

### Report Generator Agent
Creates professional software testing reports in DOCX format.

### Analysis History Database
Stores previous analysis records using SQLite.

---

## 🧠 Agentic AI Workflow

User Uploads Python File

⬇

Code Analyzer Agent

⬇

Test Generator Agent

⬇

Bug Detector Agent (Gemini AI)

⬇

Documentation Agent

⬇

Metrics Agent

⬇

Quality Assessment Agent

⬇

Report Generator Agent

⬇

SQLite Database

⬇

Final Testing Report

---

## 🛠 Technology Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite

### AI Integration
- Google Gemini API

### Deployment
- GitHub
- Render

### Report Generation
- Python DOCX

---

## 📂 Project Structure

```text
TestGenAI/
│
├── agents/
│   ├── analyzer.py
│   ├── bug_detector.py
│   ├── documentation_agent.py
│   ├── metrics.py
│   ├── quality_analyzer.py
│   ├── report_generator.py
│   └── test_generator.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── history.html
│
├── app.py
├── database.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Jayyende/TestGenAI.git
cd TestGenAI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment Variable

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📊 Sample Output

- Function Detection
- Test Case Generation
- Bug Analysis
- Documentation Generation
- Code Metrics
- Quality Assessment
- DOCX Report Generation

---

## 🔐 AI Integration

This project integrates Google Gemini API for intelligent bug detection and software testing recommendations.

Gemini AI is used by the Bug Detector Agent to analyze uploaded Python functions and provide software testing insights.

---

## 👨‍💻 Developer

### Jay Yende

B.Tech Computer Science & Engineering

Symbiosis Institute of Technology, Nagpur

Batch: 2024–2028

Semester: 3rd Semester

Course: Flexi Credit – Agentic AI & Automation

Project: AI Agent for Software Testing Assistance

---

## 📜 License

This project is developed for academic and educational purposes.

---

## ⭐ Future Enhancements

- Multi-language code support
- Advanced AI-based bug prediction
- Automated unit test execution
- PDF report generation
- Dashboard analytics
- Cloud deployment enhancements
