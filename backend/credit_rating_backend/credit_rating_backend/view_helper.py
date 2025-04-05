from .models import Mortgage


def calculate_risk_score(data):
    risk_score = 0
    risk_score = loan_to_value_ratio_risk_score(data.get("loan_amount"), data.get("property_value"))+debt_to_income_ratio_risk_score(data.get("debt_amount"), data.get("annual_income"))+credit_score_risk_score(
        data.get("credit_score"))+loan_type_risk_score(data.get("loan_type"))+property_type_risk_score(data.get("property_type"))+average_credit_score_risk_score(data.get("credit_score"))
    return risk_score


def loan_to_value_ratio_risk_score(loan_amount, property_value):
    risk_score = 0
    ltv = loan_amount / property_value
    if ltv > 0.9:
        risk_score += 2
    elif ltv > 0.8:
        risk_score += 1
    return risk_score


def debt_to_income_ratio_risk_score(debt_amount, annual_income):
    risk_score = 0
    dti = debt_amount / annual_income
    if dti > 0.5:
        risk_score += 2
    elif dti > 0.4:
        risk_score += 1
    return risk_score


def credit_score_risk_score(credit_score):
    risk_score = 0
    if credit_score >= 700:
        risk_score -= 1
    elif 650 <= credit_score < 700:
        pass
    elif credit_score < 650:
        risk_score += 1
    return risk_score


def loan_type_risk_score(loan_type):
    risk_score = 0
    if loan_type == 'adjustable':
        risk_score += 1
    else:
        risk_score -= 1
    return risk_score


def property_type_risk_score(property_type):
    risk_score = 0
    if property_type == 'condo':
        risk_score += 1
    return risk_score


def average_credit_score_risk_score(credit_score):
    risk_score = 0
    mortgage = Mortgage()
    avg_credit_score = mortgage.get_average_credit_score()
    if credit_score >= avg_credit_score:
        risk_score -= 1
    elif credit_score < avg_credit_score - 50:
        risk_score += 1
    return risk_score


def determine_credit_rating(data):
    risk_score = calculate_risk_score(data)
    if risk_score <= 2:
        return 'AAA'
    elif 3 <= risk_score <= 5:
        return 'BBB'
    else:
        return 'C'
