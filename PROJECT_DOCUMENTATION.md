# Project Documentation

## 1. Project Title

**Student Performance Analytics System**

Student name: _Add your name_

Student ID / roll number: _Add your ID_

## 2. Objective

The project analyzes student marks and attendance from a CSV file. It calculates individual results and summarizes class and subject performance so that common questions about progress and pass status can be answered from the data.

## 3. Technologies Used

- Python 3.10 or newer
- Pandas for reading, validating, organizing, and displaying tabular data
- NumPy for totals, averages, minimums, maximums, and numerical counts
- `unittest` from the Python standard library for automated checks

## 4. Dataset Description

`students.csv` contains 20 fictional sample records. Each row includes a unique student ID, name, department, marks in Maths, Science, English, and Computer Science, plus attendance percentage. Marks and attendance are represented on a 0–100 scale. Replace the sample data with approved class data if required by the trainer; do not publish private student information without permission.

## 5. Implementation

1. `load_student_data` reads the CSV into a Pandas DataFrame.
2. `validate_student_data` checks required columns, unique IDs, numeric values, and the 0–100 ranges for marks and attendance.
3. `add_performance_metrics` uses NumPy arrays to calculate each student's total and average marks. A loop assigns grades and pass/fail results.
4. `build_subject_summary` loops through the four subjects and calculates each subject's average, highest mark, lowest mark, and number of students scoring at least 40.
5. `main.py` prints the student results, class summary, subject analysis, and top five performers in readable tables.

### Grading and pass rules

- A: average at least 90
- B: average at least 80 and below 90
- C: average at least 70 and below 80
- D: average at least 60 and below 70
- E: average at least 50 and below 60
- F: average below 50
- Overall pass: at least 40 marks in every subject and attendance of at least 75%.
- Subject-wise pass count: number of marks at least 40 in that subject.

The class average is calculated as the mean of all student averages. This gives each student equal weight in the class summary.

## 6. Key Features

- CSV loading and data validation
- Student total, average, grade, and pass/fail calculations
- Class pass/fail counts and average attendance
- Highest- and lowest-average student identification
- Subject-wise average, highest, lowest, and pass-count analysis
- Top-five performer list
- Optional command-line path for analyzing a different CSV file

## 7. Output / Screenshots

The program prints the full student results table, class summary, subject analysis, and top performers in the terminal. Run `python main.py` and add a screenshot of the output here if a screenshot is required by the trainer.

## 8. Final Outcome

The project turns a CSV of student records into validated, readable performance summaries. For the included sample dataset, the class average is 76.83, 16 of 20 students pass, Computer Science has the highest subject average at 79.70, and Saanvi Das has the highest student average at 95.50. The sample dataset and calculations are verified by automated unit tests.

## 9. Challenges and Learning

Complete this section with your own experience after running the project. Possible topics include validating CSV values, choosing clear grade/pass thresholds, using DataFrames and NumPy arrays together, and testing boundary cases.

## 10. GitHub Repository

Repository URL: _Paste your GitHub repository URL after creating and checking the repository._

Google Form: Submit the repository URL through the form provided by EWB Courses. The form link is supplied by the course and is not included in the assignment PDF.