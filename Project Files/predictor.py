"""Credit card approval prediction engine."""

from dataclasses import dataclass


@dataclass
class PredictionResult:
    approved: bool
    confidence: float
    score: float
    reasons: list[str]


def _clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def predict_approval(
    *,
    age: int,
    annual_income: float,
    credit_score: int,
    employment_status: str,
    years_employed: float,
    existing_debt: float,
    credit_history_years: float,
    num_credit_cards: int,
    missed_payments: int,
    loan_amount: float,
) -> PredictionResult:
    """
    Score-based approval model using weighted financial indicators.
    Returns approval decision, confidence, and human-readable reasons.
    """
    score = 50.0
    reasons: list[str] = []

    # Credit score (strongest signal)
    if credit_score >= 750:
        score += 25
        reasons.append("Excellent credit score (750+)")
    elif credit_score >= 700:
        score += 18
        reasons.append("Good credit score (700–749)")
    elif credit_score >= 650:
        score += 8
        reasons.append("Fair credit score (650–699)")
    elif credit_score >= 600:
        score -= 8
        reasons.append("Below-average credit score (600–649)")
    else:
        score -= 25
        reasons.append("Poor credit score (below 600)")

    # Debt-to-income ratio
    dti = existing_debt / max(annual_income, 1)
    if dti <= 0.20:
        score += 12
        reasons.append("Low debt-to-income ratio")
    elif dti <= 0.35:
        score += 4
        reasons.append("Moderate debt-to-income ratio")
    elif dti <= 0.50:
        score -= 10
        reasons.append("High debt-to-income ratio")
    else:
        score -= 22
        reasons.append("Very high debt-to-income ratio")

    # Employment stability
    if employment_status == "employed":
        if years_employed >= 3:
            score += 12
            reasons.append("Stable employment (3+ years)")
        elif years_employed >= 1:
            score += 6
            reasons.append("Employed for at least 1 year")
        else:
            score += 1
            reasons.append("Recently employed")
    elif employment_status == "self_employed":
        if years_employed >= 2:
            score += 6
            reasons.append("Self-employed with established history")
        else:
            score -= 4
            reasons.append("Limited self-employment history")
    elif employment_status == "student":
        score -= 6
        reasons.append("Student applicant — higher risk profile")
    else:
        score -= 18
        reasons.append("Unemployed — significant risk factor")

    # Credit history length
    if credit_history_years >= 7:
        score += 8
        reasons.append("Long credit history (7+ years)")
    elif credit_history_years >= 3:
        score += 4
        reasons.append("Established credit history (3+ years)")
    elif credit_history_years < 1:
        score -= 10
        reasons.append("Very limited credit history")

    # Payment history
    if missed_payments == 0:
        score += 10
        reasons.append("No missed payments on record")
    elif missed_payments == 1:
        score -= 8
        reasons.append("One missed payment on record")
    else:
        score -= 20
        reasons.append(f"{missed_payments} missed payments — major concern")

    # Number of existing cards
    if num_credit_cards == 0:
        score -= 4
        reasons.append("No existing credit cards")
    elif num_credit_cards <= 3:
        score += 4
        reasons.append("Reasonable number of credit accounts")
    else:
        score -= 6
        reasons.append("Many existing credit accounts")

    # Requested loan vs income
    loan_ratio = loan_amount / max(annual_income, 1)
    if loan_ratio <= 0.10:
        score += 6
        reasons.append("Conservative credit limit request")
    elif loan_ratio <= 0.25:
        score += 2
    elif loan_ratio > 0.50:
        score -= 12
        reasons.append("Requested limit is high relative to income")

    # Age factor
    if age < 21:
        score -= 12
        reasons.append("Applicant under 21")
    elif age < 25:
        score -= 4
        reasons.append("Young applicant — limited financial history expected")
    elif age >= 25:
        score += 3

    score = _clamp(score)
    approved = score >= 55
    confidence = _clamp(abs(score - 55) * 1.8 + 52, 52, 98)

    if approved:
        reasons.insert(0, f"Application approved with a risk score of {score:.0f}/100")
    else:
        reasons.insert(0, f"Application declined with a risk score of {score:.0f}/100")

    return PredictionResult(
        approved=approved,
        confidence=round(confidence, 1),
        score=round(score, 1),
        reasons=reasons,
    )
