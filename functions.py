"""Reusable data loading and analysis functions for the student project."""

from pathlib import Path

import numpy as np
import pandas as pd

SUBJECT_COLUMNS = ["maths", "science", "english", "computer_science"]
PASS_MARK = 40
MINIMUM_ATTENDANCE = 75
REQUIRED_COLUMNS = {
    "student_id",
    "name",
    "department",
    "attendance_percent",
    *SUBJECT_COLUMNS,
}


def validate_student_data(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of student records with numeric fields parsed."""
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Dataset is missing required columns: {missing}")

    clean_data = data.copy()
    if clean_data["student_id"].duplicated().any():
        raise ValueError("Student IDs must be unique.")

    numeric_columns = [*SUBJECT_COLUMNS, "attendance_percent"]
    try:
        clean_data[numeric_columns] = clean_data[numeric_columns].apply(
            pd.to_numeric, errors="raise"
        )
    except (TypeError, ValueError) as error:
        message = "Marks and attendance must contain numeric values."
        raise ValueError(message) from error

    marks = clean_data[SUBJECT_COLUMNS]
    if ((marks < 0) | (marks > 100)).any().any():
        raise ValueError("Subject marks must be between 0 and 100.")
    attendance = clean_data["attendance_percent"]
    if ((attendance < 0) | (attendance > 100)).any():
        raise ValueError("Attendance must be between 0 and 100.")

    return clean_data


def load_student_data(file_path: str | Path) -> pd.DataFrame:
    """Read a CSV file and validate its student records."""
    return validate_student_data(pd.read_csv(file_path))


def assign_grade(average_marks: float) -> str:
    """Assign a letter grade using the project's published grade boundaries."""
    if average_marks >= 90:
        return "A"
    if average_marks >= 80:
        return "B"
    if average_marks >= 70:
        return "C"
    if average_marks >= 60:
        return "D"
    if average_marks >= 50:
        return "E"
    return "F"


def add_performance_metrics(data: pd.DataFrame) -> pd.DataFrame:
    """Add total, average, grade, and pass/fail columns to student records."""
    result = validate_student_data(data)
    marks = result[SUBJECT_COLUMNS].to_numpy(dtype=float)
    result["total_marks"] = np.sum(marks, axis=1)
    result["average_marks"] = np.mean(marks, axis=1)

    grades = []
    pass_statuses = []
    attendance_values = result["attendance_percent"].to_numpy(dtype=float)
    for average, subject_marks, attendance in zip(
        result["average_marks"], marks, attendance_values
    ):
        grades.append(assign_grade(average))
        passed = all(mark >= PASS_MARK for mark in subject_marks)
        passed = passed and attendance >= MINIMUM_ATTENDANCE
        pass_statuses.append("Pass" if passed else "Fail")

    result["grade"] = grades
    result["status"] = pass_statuses
    return result


def build_subject_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Calculate average, highest, lowest, and pass count for each subject."""
    records = []
    for subject in SUBJECT_COLUMNS:
        marks = data[subject].to_numpy(dtype=float)
        records.append(
            {
                "subject": subject.replace("_", " ").title(),
                "average_marks": float(np.mean(marks)),
                "highest_marks": float(np.max(marks)),
                "lowest_marks": float(np.min(marks)),
                "students_passed": int(np.count_nonzero(marks >= PASS_MARK)),
            }
        )
    return pd.DataFrame(records).sort_values(
        "average_marks", ascending=False, ignore_index=True
    )


def get_top_performers(data: pd.DataFrame, limit: int = 5) -> pd.DataFrame:
    """Return up to ``limit`` students ordered by average marks."""
    if limit < 1:
        raise ValueError("The number of top performers must be at least 1.")
    sorted_data = data.sort_values(
        ["average_marks", "name"], ascending=[False, True]
    )
    return sorted_data.head(limit)
