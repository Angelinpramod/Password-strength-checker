import re
import math

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty",
    "admin", "letmein", "welcome", "iloveyou",
    "password1", "123456789", "abc123"
}

def rule_based_checks(password):
    issues = []

    if len(password) < 8:
        issues.append("Password is too short; it should be at least 8 characters long.")
    
    if not re.search(r"[A-Z]",password):
        issues.append("Add at least one uppercase letter")

    if not re.search(r"[a-z]",password):
        issues.append("Add at least one lowercase letter")

    if not re.search(r"\d",password):
        issues.append("Add at least one digit")
    if not re.search(r"[!@#$%^&*()<>?\":{}|<>]",password):
        issues.append("Add at least one special character")
    
    return issues

def entropy_calc(password):
    pool_sz=0

    if re.search(r"[A-Z]",password):
        pool_sz +=26

    if re.search(r"[a-z]",password):
        pool_sz +=26    
    
    if re.search(r"\d",password):
        pool_sz +=10
    
    if re.search(r"[!@#$%^&*()<>?\":{}|<>]",password):
        pool_sz +=32

    if pool_sz==0:
        return 0
    entropy=len(password)*math.log2(pool_sz)

    return round(entropy,2)


def entropy_rating(entropy):
    if entropy < 28:
        return "Very Weak"
    elif 28 <= entropy < 36:
        return "Weak"
    elif 36 <= entropy < 60:
        return "Reasonable"
    elif 60 <= entropy < 128:
        return "Strong"
    else:
        return "Very Strong"


def common_pass_check(password):
    return password.lower() in COMMON_PASSWORDS
