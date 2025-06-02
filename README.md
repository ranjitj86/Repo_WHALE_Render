[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?repo=yourusername/your-repo)

# WHALE: Multi-Agent Requirement Engineering System

An AI-powered, modular web system for requirements engineering in the Automotive Industry, powered by LLMs and Hugging Face models. Supports end-to-end requirements intake, analysis, review, and test case generation.

---

## Features

- **SYS.1 Elicitation:** Upload and process raw inputs to extract and draft initial requirements.
- **SYS.2 Analysis:** Analyze and structure the drafted requirements.
- **SYS.2 Review:** Review requirements against standards and guidelines.
- **SYS.5 Testcase Generation:** Generate test cases based on requirements.

---

## Prerequisites

- **Python 3.10+** (recommended)
- **pip** (Python package manager)
- Windows 10/11 or Linux/Mac (instructions below are cross-platform)

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download spaCy model:**
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Create a `.env` file:**
   Create a file named `.env` in the project root with at least:
   ```
   SECRET_KEY=your-secret-key-here
   # Add other environment variables as needed
   ```

---

## Running Locally

1. Activate your virtual environment (if not already active):
   ```bash
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
2. Run the app:
   ```bash
   python app.py
   ```
   The app will be available at http://localhost:5000

---

## Running on Render

- Render uses `render.yaml` for deployment. The app will be started with:
  ```yaml
  startCommand: PYTHONPATH=. gunicorn app:app --chdir . -w 4 -b 0.0.0.0:10000
  ```
- Make sure all files are at the project root and imports use the flat structure.

---

## Directory Structure

```
<project-root>/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create manually)
├── agents/                 # Agent logic (intake, sys2, review, testgen)
├── templates/              # Jinja2 HTML templates (UI for each agent)
├── static/                 # Static files (CSS, JS)
├── Inputs/                 # Input/output files (Excel, TXT)
│   ├── sys1_requirements.xlsx
│   ├── sys2_requirements.xlsx
│   ├── sys2_requirements_reviewed.xlsx
│   └── ...
└── uploads/                # Temporary uploaded files
```

---

## Agent Workflows

### Agent 1: SYS.1 Elicitation
- Upload customer requirements (TXT, DOCX, PDF, XLSX, etc.)
- Extracted SYS.1 requirements are displayed and can be exported (XLSX, CSV, DOCX, PDF)

### Agent 2: SYS.2 Analysis
- Loads SYS.1 requirements automatically or via upload
- Drafts and structures SYS.2 requirements
- Export options available

### Agent 3: SYS.2 Review
- Loads SYS.2 requirements (auto/manual)
- Review, accept, or reject each requirement
- Only "Approved" requirements are exported to `Inputs/sys2_requirements_reviewed.xlsx`

### Agent 4: SYS.5 Testcase Generation
- Loads reviewed SYS.2 requirements (auto/manual)
- Generates SYS.5 test cases for each SYS.2 requirement
- Displays traceability dashboard (charts, tables)
- Export test cases in multiple formats

---

## Example Input Files
- Place your input files in the `Inputs/` directory:
    - `sys1_requirements.xlsx` (for Agent 2)
    - `sys2_requirements.xlsx` (for Agent 3)
    - `sys2_requirements_reviewed.xlsx` (for Agent 4)
- Supported formats: `.xlsx`, `.csv`, `.txt`, `.docx`, `.pdf`

---

## Troubleshooting & Common Deployment Issues

- **win10toast or pywin32 errors:** These are Windows-only packages. Ensure your `requirements.txt` does NOT include `win10toast` or `pywin32` when deploying to Linux (e.g., Render).
- **Unresolved Import Warnings in VS Code:**
  - Make sure you have selected the correct Python interpreter (the one in your `venv`).
  - Reload VS Code window after installing packages.
  - Activate your virtual environment in the terminal.
- **File Not Found Errors:**
  - Ensure your input files are named and placed exactly as expected in the `Inputs/` directory.
  - Check file permissions if running on Windows.
- **Port Already in Use:**
  - If you see an error about port 5000, close other Flask instances or change the port in `app.py`.
- **Other Issues:**
  - Check the terminal for error messages and stack traces.
  - Ensure all dependencies in `requirements.txt` are installed.

---

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
