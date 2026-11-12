import re


def average_marks(marks_csv):
    if not isinstance(marks_csv, str):
        return None
    try:
        marks = [int(m) for m in marks_csv.split(',')]
        return round(sum(marks) / len(marks), 2)
    except (ValueError, OverflowError, ZeroDivisionError):
        return None


def parse_srn(srn):
    if not isinstance(srn, str):
        return None
    m = re.fullmatch(r'PES\dUG(\d{2})([A-Z]{2})\d{3}', srn, re.ASCII)
    if not m:
        return None
    return srn[:4], int(m.group(1)), m.group(2)


def short_name(full_name):
    if not isinstance(full_name, str):
        return None
    parts = full_name.split()
    if len(parts) != 2:
        return None
    first, last = parts
    return first[0].upper() + ". " + last.capitalize()


def main():
    print("==== Running average_marks ====")
    user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
    result = average_marks(user_input)
    print("Average Marks:", result if result is not None else "Invalid input")

    print("\n==== Running parse_srn ====")
    user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
    result = parse_srn(user_input)
    print("Campus, Year and Dept:", result if result is not None else "Invalid input")

    print("\n==== Running short_name ====")
    user_input = input("Enter first and last name (e.g. ravi kumar): ")
    result = short_name(user_input)
    print("Short Name:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()