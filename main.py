"""Run the Student Performance Analytics System from the command line."""

import argparse
from pathlib import Path

import pandas as pd

from functions import (
    add_performance_metrics,
    build_subject_summary,
    get_top_performers,
    load_student_data,
)


def print_report(data: pd.DataFrame) -> None:
    """Display the dataset and its student, class, and subject analysis."""
    results = add_performance_metrics(data)
    subject_summary = build_subject_summary(results)
    passed_count = int((results["status"] == "Pass").sum())
    best_student = results.loc[results["average_marks"].idxmax()]
    lowest_student = results.loc[results["average_marks"].idxmin()]
    best_subject = subject_summary.iloc[0]

    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 42)
    print(f"Records: {len(results)} | Columns: {len(data.columns)}")
    print(f"Departments: {', '.join(sorted(results['department'].unique()))}")
    print("\nSTUDENT RESULTS")
    print("-" * 42)
    student_columns = [
        "student_id",
        "name",
        "total_marks",
        "average_marks",
        "grade",
        "attendance_percent",
        "status",
    ]
    print(
        results[student_columns].to_string(
            index=False,
            formatters={
                "average_marks": "{:.2f}".format,
                "attendance_percent": "{:.1f}".format,
            },
        )
    )

    print("\nCLASS SUMMARY")
    print("-" * 42)
    print(f"Class average: {results['average_marks'].mean():.2f} / 100")
    print(f"Students passed: {passed_count} / {len(results)}")
    print(f"Students failed: {len(results) - passed_count} / {len(results)}")
    print(f"Average attendance: {results['attendance_percent'].mean():.1f}%")
    print(
        f"Highest average: {best_student['name']} "
        f"({best_student['average_marks']:.2f}, grade {best_student['grade']})"
    )
    print(
        f"Lowest average: {lowest_student['name']} "
        f"({lowest_student['average_marks']:.2f}, "
        f"grade {lowest_student['grade']})"
    )
    print(
        f"Best subject: {best_subject['subject']} "
        f"(class average {best_subject['average_marks']:.2f})"
    )

    print("\nSUBJECT ANALYSIS")
    print("-" * 42)
    print(
        subject_summary.to_string(
            index=False,
            formatters={
                "average_marks": "{:.2f}".format,
                "highest_marks": "{:.0f}".format,
                "lowest_marks": "{:.0f}".format,
            },
        )
    )

    print("\nTOP PERFORMERS")
    print("-" * 42)
    top_columns = ["student_id", "name", "average_marks", "grade"]
    print(
        get_top_performers(results)[top_columns].to_string(
            index=False, formatters={"average_marks": "{:.2f}".format}
        )
    )


def main() -> int:
    """Parse the optional CSV path, load records, and print the report."""
    parser = argparse.ArgumentParser(
        description="Analyze student marks and attendance from a CSV file."
    )
    default_csv = Path(__file__).resolve().parent / "students.csv"
    parser.add_argument(
        "--csv",
        type=Path,
        default=default_csv,
        help=f"path to the student CSV file (default: {default_csv.name})",
    )
    args = parser.parse_args()

    try:
        student_data = load_student_data(args.csv)
    except (FileNotFoundError, pd.errors.EmptyDataError, ValueError) as error:
        print(f"Could not analyze student data: {error}")
        return 1

    print_report(student_data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
