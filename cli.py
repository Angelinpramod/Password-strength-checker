from core import (
    rule_based_checks,
    entropy_calc,
    entropy_rating,
    common_pass_check
)

def main():
    password = input("Enter password: ")

    issues = rule_based_checks(password)
    entropy = entropy_calc(password)
    rating = entropy_rating(entropy)
    is_common = common_pass_check(password)

    print("\n-- Password Analysis --\n")

    if issues:
        for issue in issues:
            print(f"- {issue}")
    else:
        print("All rule-based checks passed")

    print(f"\nEstimated entropy: {entropy} bits")
    print(f"Entropy rating: {rating}")

    if is_common:
        print("\n⚠️ Warning: This password is very commonly used.")

if __name__ == "__main__":
    main()
