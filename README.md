# ANA 680 – Assignment 4  
## Machine Learning Model Deployment  
### Wisconsin Breast Cancer – Linear SVM Classifier

**Author:** Randall C. Crawford  

**Course:** ANA 680 – Machine Learning Deployment  

---

## Assignment Overview

This assignment focuses on the **end-to-end deployment of a machine learning model** as a web-accessible service. The objective was to take a fully evaluated and finalized model from **Assignment 2**, validate the deployment configuration locally, and then deploy the model to a **cloud-hosted production environment**.

The deployed model is a **Linear Support Vector Machine (LinearSVM)** trained on the **Wisconsin Breast Cancer Diagnostic dataset**, selected based on recall-critical performance and deployment stability.

---

## Deployment Workflow

The deployment process followed a **two-stage workflow** designed to mirror real-world machine learning operations:

### 1. Local Deployment Verification (Flask)

Before cloud deployment, a **Flask application** was used to:
- Validate the inference pipeline
- Confirm correct loading of:
  - Trained model (`model.pkl`)
  - Feature scaler (`scaler.pkl`)
- Verify request handling and response formatting
- Ensure consistency between training-time preprocessing and inference-time inputs

This step ensured the model could be reliably served as an API before introducing cloud infrastructure complexity.

---

### 2. Cloud Deployment (Heroku)

After local verification, the Flask application was deployed to **Heroku** as a production-style web service.

Deployment configuration included:
- `app.py` – Flask application defining inference endpoints  
- `Procfile` – Heroku process definition  
- `requirements.txt` – Python dependencies  
- `runtime.txt` – Python runtime specification  
- `model.pkl` – Serialized LinearSVM model  
- `scaler.pkl` – Serialized feature scaler  
- `breast-cancer-wisconsin_cleaned.csv` – Reference dataset
- `templates/index.html` - Web service format  
- `.github/workflows/deploy.yml` – CI/CD deployment workflow  

Heroku was selected to demonstrate:
- Lightweight cloud deployment
- Model serving via HTTP
- Reproducible environment configuration
- Continuous deployment practices

---

## Live Deployment

The deployed application is publicly accessible at:

👉 **https://bcw-linearsvm-a8d8f9a62dba.herokuapp.com/**

The endpoint accepts feature inputs consistent with the Wisconsin Breast Cancer dataset and returns a **binary classification result** indicating *Benign* or *Malignant*.

---

## Model Details

- **Model:** Linear Support Vector Machine (LinearSVM)
- **Dataset:** Wisconsin Breast Cancer Diagnostic (WBCD)
- **Features:** 30 numeric features derived from cell nucleus characteristics
- **Target:** Binary classification (Malignant / Benign)

The model and decision threshold were finalized in **Assignment 2** and reused **unchanged** for deployment to ensure traceability and reproducibility.

---

## Deployment Design Considerations

Several deployment-focused decisions were made:

- **Threshold control:** The deployed model uses a recall-optimized decision threshold to minimize false negatives.
- **Model simplicity:** LinearSVM provides stable, fast inference suitable for production.
- **Explicit preprocessing:** Feature scaling is enforced via a saved scaler to prevent data leakage.
- **Artifact versioning:** Model and scaler are version-locked for reproducibility.

These considerations reflect real-world deployment constraints where reliability and safety outweigh marginal accuracy gains.

---

## Tools & Technologies

- **Python**
- **Flask**
- **scikit-learn**
- **Heroku**
- **GitHub Actions (CI/CD)**
- NumPy, Pandas

---

## Relationship to Assignment 2

- **Assignment 2:**  
  - Exploratory Data Analysis (EDA)  
  - Data cleaning and dataset generation  
  - Model benchmarking and optimization  
  - Final LinearSVM model selection  

- **Assignment 4:**  
  - Deployment verification  
  - API creation  
  - Cloud hosting and serving  

This separation mirrors industry workflows where **model determination precedes deployment**.

---

## Outcome

This assignment demonstrates the ability to:
- Transition from model development to production deployment
- Validate inference pipelines prior to cloud hosting
- Deploy machine learning models as web services
- Apply deployment-aware model decisions

The result is a fully functional, cloud-hosted machine learning application suitable for real-world use.

---
