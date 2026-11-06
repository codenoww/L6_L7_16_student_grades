import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# ---------- letter_grade: both outcomes of every decision ----------
def test_s_grade():
    assert letter_grade(95) == "S"


def test_a_grade():
    assert letter_grade(85) == "A"


def test_b_grade():
    assert letter_grade(75) == "B"


def test_c_grade():
    assert letter_grade(65) == "C"


def test_d_grade():
    assert letter_grade(55) == "D"


def test_e_grade():
    assert letter_grade(45) == "E"


def test_f_grade():
    assert letter_grade(20) == "F"


@pytest.mark.parametrize("marks, expected", [
    (90, "S"), (89, "A"), (80, "A"), (79, "B"), (70, "B"), (69, "C"),
    (60, "C"), (59, "D"), (50, "D"), (49, "E"), (40, "E"), (39, "F"),
    (0, "F"), (100, "S"),
])
def test_letter_grade_boundaries(marks, expected):
    assert letter_grade(marks) == expected


def test_letter_grade_negative_marks():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_letter_grade_above_100():
    with pytest.raises(ValueError):
        letter_grade(101)


# ---------- final_marks: every branch ----------
def test_final_marks_no_project():
    assert final_marks(30, 40, False) == 70


def test_final_marks_with_project_below_cap():
    assert final_marks(30, 50, True) == 85


def test_final_marks_project_capped_at_100():
    assert final_marks(40, 60, True) == 100


def test_final_marks_project_exactly_100():
    assert final_marks(35, 60, True) == 100


def test_final_marks_internal_too_high():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)


def test_final_marks_external_too_high():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)


def test_final_marks_boundary_values_valid():
    assert final_marks(40, 60, False) == 100
    assert final_marks(0, 0, False) == 0


# ---------- exam_eligibility: every branch ----------
def test_blocked_fees_not_paid():
    assert exam_eligibility(90, False, False) == "blocked"


def test_blocked_even_with_medical():
    assert exam_eligibility(90, False, True) == "blocked"


def test_eligible():
    assert exam_eligibility(80, True, False) == "eligible"


def test_eligible_attendance_exactly_75():
    assert exam_eligibility(75, True, False) == "eligible"


def test_eligible_with_medical_condonation():
    assert exam_eligibility(70, True, True) == "eligible"


def test_eligible_medical_attendance_exactly_65():
    assert exam_eligibility(65, True, True) == "eligible"


def test_detained_no_medical():
    assert exam_eligibility(70, True, False) == "detained"


def test_detained_medical_but_attendance_below_65():
    assert exam_eligibility(64, True, True) == "detained"


def test_detained_low_attendance():
    assert exam_eligibility(50, True, False) == "detained"
