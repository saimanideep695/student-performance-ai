# Student Performance Analytics System

A Python command-line project that reads student marks and attendance from a CSV file and produces student-level, class-level, and subject-level summaries. It uses Pandas to load and organize the data and NumPy for numerical calculations. It is a data-analysis project; it does not use machine learning.

## Project contents

- `main.py` runs the analysis and prints the report.
- `functions.py` contains reusable validation, calculation, grading, and analysis functions.
- `students.csv` contains 20 fictional sample student records.
- `PROJECT_DOCUMENTATION.md` contains the project documentation and submission fields.
- `tests/test_functions.py` contains automated checks for the analysis rules.

## Requirements

- Python 3.10 or newer
- NumPy
- Pandas

Install the dependencies from the project folder:

```powershell
python -m pip install -r requirements.txt
```

## Run the analysis

```powershell
python main.py
```

To analyze another CSV file with the same column names:

```powershell
python main.py --csv path\to\students.csv
```

The program prints each student's total and average marks, grade and result; class averages and pass counts; subject-wise averages and ranges; and the top five students.

## Analysis rules

- Each subject is marked out of 100.
- Grades: A = 90 or above; B = 80–89.99; C = 70–79.99; D = 60–69.99; E = 50–59.99; F = below 50.
- A student passes when every subject mark is at least 40 and attendance is at least 75%.
- Subject pass counts use the subject mark rule only: at least 40 marks.
- The class average is the mean of the students' four-subject averages.

## Test

Run the standard-library unit tests from the project folder:

```powershell
python -m unittest discover -s tests -v
```

## GitHub submission checklist

1. Create a repository named `student-performance-analytics` (or another clear name).
2. Upload the project files, including the CSV, README, and project documentation.
3. Run the project and tests from a clean environment.
4. Set the repository visibility as instructed by the trainer and verify the uploaded files.
5. Add the repository URL to `PROJECT_DOCUMENTATION.md` and submit it using the Google Form provided by EWB Courses.

The repository and Google Form submission require the student's own GitHub account and course link; neither is created by this local project.