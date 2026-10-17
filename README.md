# InterviewReady — AI Tutor for Interview Preparation

**InterviewReady** is a web-based interview practice application built with Python and Streamlit. It helps learners prepare for job interviews by practising sample questions, reviewing feedback on their answers, and tracking their practice progress.

🔗 **Live Demo:** [Try InterviewReady](https://ai-tutor-for-interview-preparation-3eytlqpyxi4vjatngxw23e.streamlit.app/)

📂 **GitHub Repository:** [AI-Tutor-for-Interview-Preparation](https://github.com/anuragaries1/AI-Tutor-for-Interview-Preparation)

## Project Objectives

- Provide an accessible environment for practising interview questions.
- Help users assess and improve their written interview answers.
- Encourage consistent interview preparation through progress tracking.
- Demonstrate the development and deployment of a Python-based educational web application.

## Features

### 1. Dashboard
Introduces the application and provides an entry point to the interview preparation activities.

### 2. Practice Questions
- Offers prepared interview questions across three categories:
  - HR and Introduction
  - Behavioral Questions
  - Technical Questions and Projects
- Allows users to select a question and submit a written answer.
- Provides a score, feedback, and suggestions for improvement.

### 3. Answer Evaluation
Uses a local rule-based evaluation approach to analyse submitted answers. The evaluation considers factors such as answer length, relevant keywords, and example phrases to provide preliminary feedback.

### 4. My Progress
- Displays recorded practice attempts.
- Presents practice results in a table.
- Provides a CSV export option for further review.

### 5. About
Explains the application's purpose, evaluation approach, and current limitations.

## Technology Stack

- **Programming language:** Python
- **Web application framework:** Streamlit
- **Data handling:** Python data structures and CSV export
- **Evaluation:** Local rule-based and keyword-based logic
- **Version control:** Git and GitHub
- **Deployment:** Streamlit Community Cloud

## Getting Started

### Prerequisites

- Python installed on your computer
- Git (optional, for cloning the repository)
- A web browser

### 1. Clone the repository

Open PowerShell or a terminal and run:

```bash
git clone https://github.com/anuragaries1/AI-Tutor-for-Interview-Preparation.git
cd AI-Tutor-for-Interview-Preparation
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the application using the virtual environment's Python executable directly instead.

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
python -m streamlit run main.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`, which you can open in your browser.

## Screenshots

Screenshots of the following application sections can be added here to demonstrate the user experience:

- Dashboard
- Practice Questions and answer feedback
- My Progress and CSV export
- About

For a portfolio presentation, save screenshots in a `screenshots/` folder in the repository and embed them in this section using Markdown image links.

## Current Limitations

InterviewReady is an early-stage portfolio prototype. Its current limitations include:

- **No live AI model:** Answer evaluation currently uses local rules and keyword matching; it does not call a live large language model.
- **Limited question bank:** The application currently uses a small set of seven prepared interview questions.
- **Basic evaluation:** Scores and suggestions are heuristic and should not be treated as definitive measures of interview performance.
- **Session-based progress:** Practice history is stored in the active Streamlit session. It is not currently a permanent user account or database-backed record, so progress may not persist across sessions.
- **No authentication:** The application does not currently provide user accounts or personalised multi-user data storage.

These limitations provide opportunities for future development.

## Future Enhancements

Potential improvements include:

- Integrating an AI model for more contextual answer feedback.
- Expanding the question bank by role, industry, and experience level.
- Adding interview simulations and follow-up questions.
- Introducing persistent progress storage and user accounts.
- Improving evaluation with structured rubrics for clarity, relevance, and completeness.
- Adding more detailed performance reports and visual analytics.

## Learning Outcomes

This project demonstrates practical experience with:

- Building an interactive application using Python and Streamlit.
- Designing a question-and-answer practice workflow.
- Implementing rule-based text evaluation.
- Managing dependencies and project files.
- Using Git and GitHub for version control.
- Deploying a web application for public access.

## Disclaimer

InterviewReady is intended for educational and practice purposes. Its feedback is a preliminary aid for improving interview answers, not a guarantee of interview success or a substitute for professional recruitment advice.

## License

No open-source license has been specified for this repository yet. Unless a license is added, the project should not be assumed to be available for unrestricted reuse or redistribution.

---

**Project:** InterviewReady — AI Tutor for Interview Preparation  
**Status:** Deployed portfolio prototype  
**Live application:** [Open InterviewReady](https://ai-tutor-for-interview-preparation-3eytlqpyxi4vjatngxw23e.streamlit.app/)