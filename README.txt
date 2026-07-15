# Credit Card Approval Prediction System

A Machine Learning-based web application that predicts whether a credit card application is likely to be **Approved** or **Rejected** using an applicant's financial and personal information.

The project is developed using **Python, Flask, Scikit-learn, HTML, CSS, and the Random Forest Classifier** to provide a fast, accurate, and user-friendly prediction system.

---

## Project Overview

Financial institutions receive a large number of credit card applications every day. Evaluating each application manually requires significant time and effort and may result in inconsistent decisions.

This project aims to simplify the approval process by applying Machine Learning techniques to analyze applicant information and predict the likelihood of approval.

The model considers various applicant details such as:

* Personal Information
* Employment Details
* Annual Income
* Credit Score
* Existing Loans
* Loan Amount
* Loan Duration
* Dependents

Based on these inputs, the trained **Random Forest Classifier** predicts the approval status along with a confidence score to assist in decision-making.

---

## Key Features

* User-friendly Flask web application
* Responsive and modern interface
* Real-time prediction of credit card approval
* Validation of user inputs
* Confidence score for every prediction
* Automatic loading of the trained model
* Automatic model generation if the model file is unavailable
* Detailed applicant summary on the result page

---

## Technology Stack

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Random Forest Classifier
* Pandas
* NumPy
* Joblib

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

---

## Project Structure

```text
Credit-Card-Approval-Prediction/
│
├── app.py
├── train_model.py
├── requirements.txt
├── credit_model.pkl
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── predict.html
│   ├── result.html
│   └── about.html
│
├── static/
│   └── css/
│       └── style.css
│
├── models/
│   └── credit_model.pkl
│
└── README.md
```

---

## Machine Learning Model

The prediction system is powered by the **Random Forest Classifier**, an ensemble learning algorithm known for its high accuracy and robustness.

### Data Processing

* One-Hot Encoding of categorical data
* Scaling of numerical features
* Feature transformation
* Prediction using the trained model

---

## Input Features

The model uses twelve important applicant attributes.

| Feature         | Description                       |
| --------------- | --------------------------------- |
| Gender          | Male / Female                     |
| Age             | Applicant Age                     |
| Education       | Education Qualification           |
| Marital Status  | Single / Married / Divorced       |
| Employment Type | Salaried, Business, Self-employed |
| Property Area   | Urban / Semi-Urban / Rural        |
| Annual Income   | Annual Income                     |
| Credit Score    | Credit Rating                     |
| Existing Loans  | Number of Existing Loans          |
| Loan Amount     | Requested Loan Amount             |
| Loan Term       | Loan Repayment Duration           |
| Dependents      | Number of Dependents              |

---

## Model Training

The training script (`train_model.py`) performs the following tasks:

* Generates a synthetic dataset
* Cleans and preprocesses data
* Performs feature engineering
* Splits the dataset into training and testing sets
* Trains the Random Forest Classifier
* Evaluates model performance
* Saves the trained model using Joblib

The trained model is stored as:

```text
models/credit_model.pkl
```

---

## Web Application

The Flask application consists of four main pages.

### Home

* Introduction to the project
* Project objectives
* Navigation to the prediction page

### Predict

Users enter:

* Personal Details
* Employment Information
* Financial Information

The application validates every input before making a prediction.

### Result

Displays:

* Approval or Rejection Prediction
* Confidence Score
* Applicant Information Summary

### About

Contains:

* Project description
* Features used by the model
* Technology stack
* Development information

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Credit-Card-Approval-Prediction.git
```

### Navigate to the Project Folder

```bash
cd Credit-Card-Approval-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5001
```

---

## Requirements

```text
Flask
scikit-learn
pandas
numpy
joblib
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Application Workflow

```text
Applicant Information
        │
        ▼
Input Validation
        │
        ▼
Data Preprocessing
        │
        ▼
Random Forest Model
        │
        ▼
Prediction
        │
        ▼
Confidence Score
        │
        ▼
Display Final Result
```

---

## Use Cases

### Bank Credit Evaluation

Helps banking professionals quickly evaluate applicants and reduce manual effort.

### Risk Assessment

Supports financial institutions in identifying potential high-risk applicants by analyzing financial and credit-related factors.

### Customer Eligibility Check

Allows customers to estimate their approval chances before submitting an official credit card application.

---

## Future Enhancements

* XGBoost Integration
* Logistic Regression Comparison
* Decision Tree Comparison
* Explainable AI using SHAP and LIME
* IBM Watson Cloud Deployment
* User Authentication
* Database Integration
* REST API Development
* Docker Containerization
* Cloud Deployment using AWS or Azure

---

## Author

**THATHA VENKATATEJ KUMAR**

Machine Learning Enthusiast | Python Developer | Flask Developer | Data Science Learner

---

## License

This project is licensed under the **MIT License**.

---

## Support

If you find this project useful:

* Star the repository.
* Fork the project.
* Report issues.
* Suggest improvements.

---

Thank you for exploring this project.
