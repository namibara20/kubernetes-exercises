# Exercise 9 — Jenkins Multi-Stage Pipeline

## Objective
Build, test, deploy, and verify a Python Flask application using a Jenkins Declarative Pipeline.

## Technologies Used
- Jenkins
- Git and GitHub
- Python
- Flask
- Pytest
- Jenkins Declarative Pipeline

## Project Structure
```text
Exercise-9-Jenkins-Multi-Stage-Pipeline/
├── app.py
├── requirements.txt
├── test_app.py
├── Jenkinsfile
├── README.md
├── transcript.txt
└── Screenshots/
    └── jenkins-pipeline-success.png
```

## Application
The Flask application serves the following message at `/`:

`Hello, Jenkins Multi-Stage Pipeline!`

## Pipeline Stages
1. **Build:** Create a Python virtual environment and install dependencies.
2. **Test:** Run the Flask application unit test using pytest.
3. **Deploy:** Copy `app.py` into the deployment directory.
4. **Run Application:** Start the Flask application.
5. **Test Application:** Send an HTTP request to verify the deployed application.

## Jenkins Configuration
- Job name: `Jenkins-Multi-Stage-Pipeline`
- Job type: Pipeline
- Source control: Git
- Branch: `main`
- Script path: `Exercise-9-Jenkins-Multi-Stage-Pipeline/Jenkinsfile`

## Result
The pipeline completed successfully. All five stages passed, and the deployed application's HTTP response was verified.

## Conclusion
Successfully implemented and executed a Jenkins multi-stage pipeline for a Python Flask application.