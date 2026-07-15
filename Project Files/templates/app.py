"""Flask web application for credit card approval prediction."""

from flask import Flask, flash, redirect, render_template, request, url_for

from predictor import predict_approval

app = Flask(__name__)
app.secret_key = "dev-secret-change-in-production"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("predict.html")

    try:
        age = int(request.form["age"])
        annual_income = float(request.form["annual_income"])
        credit_score = int(request.form["credit_score"])
        employment_status = request.form["employment_status"]
        years_employed = float(request.form["years_employed"])
        existing_debt = float(request.form["existing_debt"])
        credit_history_years = float(request.form["credit_history_years"])
        num_credit_cards = int(request.form["num_credit_cards"])
        missed_payments = int(request.form["missed_payments"])
        loan_amount = float(request.form["loan_amount"])
    except (KeyError, ValueError, TypeError):
        flash("Please fill in all fields with valid values.", "error")
        return redirect(url_for("predict"))

    if not (18 <= age <= 100):
        flash("Age must be between 18 and 100.", "error")
        return redirect(url_for("predict"))
    if not (300 <= credit_score <= 850):
        flash("Credit score must be between 300 and 850.", "error")
        return redirect(url_for("predict"))
    if annual_income < 0 or existing_debt < 0 or loan_amount < 0:
        flash("Income, debt, and loan amount cannot be negative.", "error")
        return redirect(url_for("predict"))

    result = predict_approval(
        age=age,
        annual_income=annual_income,
        credit_score=credit_score,
        employment_status=employment_status,
        years_employed=years_employed,
        existing_debt=existing_debt,
        credit_history_years=credit_history_years,
        num_credit_cards=num_credit_cards,
        missed_payments=missed_payments,
        loan_amount=loan_amount,
    )

    form_data = {
        "age": age,
        "annual_income": annual_income,
        "credit_score": credit_score,
        "employment_status": employment_status.replace("_", " ").title(),
        "years_employed": years_employed,
        "existing_debt": existing_debt,
        "credit_history_years": credit_history_years,
        "num_credit_cards": num_credit_cards,
        "missed_payments": missed_payments,
        "loan_amount": loan_amount,
    }

    return render_template("result.html", result=result, form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
