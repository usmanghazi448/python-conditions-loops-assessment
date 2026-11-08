"""
Student Scholarship Eligibility System
Topic: Conditional Statements (if, elif, else)

Evaluates a student's scholarship eligibility from academic marks,
attendance percentage and monthly family income.
"""

# ---------- Eligibility thresholds ----------
MIN_MARKS = 80
FULL_SCHOLARSHIP_MARKS = 90
MIN_ATTENDANCE = 85
MAX_INCOME = 50000


def get_name():
    """Ask for a non-empty name made of letters and spaces."""
    while True:
        name = input("Enter student name: ").strip()
        if name == "":
            print("  Error: Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("  Error: Name must contain only letters and spaces.")
        else:
            return name.title()


def get_number(prompt, minimum, maximum=None):
    """Ask for a number and keep asking until it is valid."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("  Error: Please enter a valid number.")
            continue

        if value < minimum:
            print(f"  Error: Value cannot be less than {minimum}.")
        elif maximum is not None and value > maximum:
            print(f"  Error: Value cannot be greater than {maximum}.")
        else:
            return value


def evaluate(marks, attendance, income):
    """Return (scholarship_type, list_of_reasons)."""
    reasons = []

    if marks < MIN_MARKS:
        reasons.append(f"Academic marks ({marks:.2f}%) are below the required {MIN_MARKS}%.")
    if attendance < MIN_ATTENDANCE:
        reasons.append(f"Attendance ({attendance:.2f}%) is below the required {MIN_ATTENDANCE}%.")
    if income > MAX_INCOME:
        reasons.append(f"Monthly family income (Rs. {income:,.2f}) exceeds the limit of Rs. {MAX_INCOME:,}.")

    # Decide the outcome with if / elif / else
    if len(reasons) > 0:
        scholarship = "None"
    elif marks >= FULL_SCHOLARSHIP_MARKS:
        scholarship = "Full Scholarship"
    elif marks >= MIN_MARKS:
        scholarship = "Partial Scholarship"
    else:
        scholarship = "None"

    return scholarship, reasons


def print_report(name, marks, attendance, income, scholarship, reasons):
    line = "=" * 56
    print("\n" + line)
    print("        SCHOLARSHIP EVALUATION REPORT")
    print(line)
    print(f"Student Name           : {name}")
    print(f"Academic Marks         : {marks:.2f}%")
    print(f"Attendance             : {attendance:.2f}%")
    print(f"Monthly Family Income  : Rs. {income:,.2f}")
    print("-" * 56)
    print("Criteria Check:")
    print(f"  Marks >= {MIN_MARKS}%            : {'PASS' if marks >= MIN_MARKS else 'FAIL'}")
    print(f"  Attendance >= {MIN_ATTENDANCE}%      : {'PASS' if attendance >= MIN_ATTENDANCE else 'FAIL'}")
    print(f"  Income <= Rs. {MAX_INCOME:,}   : {'PASS' if income <= MAX_INCOME else 'FAIL'}")
    print("-" * 56)

    if scholarship == "None":
        print("Status                 : NOT ELIGIBLE")
        print("Reason(s) for ineligibility:")
        for number, reason in enumerate(reasons, start=1):
            print(f"  {number}. {reason}")
    else:
        print("Status                 : ELIGIBLE")
        print(f"Scholarship Awarded    : {scholarship}")
        if scholarship == "Full Scholarship":
            print("Remarks                : Outstanding performance (90% or above).")
        else:
            print("Remarks                : Good performance (80% - 89%).")
    print(line)


def main():
    print("=" * 56)
    print("   STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM")
    print("=" * 56)

    while True:
        name = get_name()
        marks = get_number("Enter academic marks (0-100%): ", 0, 100)
        attendance = get_number("Enter attendance percentage (0-100%): ", 0, 100)
        income = get_number("Enter monthly family income (Rs.): ", 0)

        scholarship, reasons = evaluate(marks, attendance, income)
        print_report(name, marks, attendance, income, scholarship, reasons)

        again = input("\nEvaluate another student? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the Scholarship Eligibility System.")
            break
        print()


if __name__ == "__main__":
    main()