# Study Planner

A Flask-based web application that helps students plan their study schedule by selecting their availability and generating a topic-wise plan from the syllabus.

## Features

- Student login form
- Availability selection by day/week/month
- Topic planning based on syllabus content
- Final generated study schedule
- CSV-based syllabus data handling
- Simple multi-page Flask flow

## Tech Stack

- Python
- Flask
- Pandas
- HTML
- CSV

## Project Structure

```text
STUDY_PLANNER/
├─ app.py
├─ data/
│  └─ BAD601 SYLLABUS CONTENT.csv
├─ templates/
│  ├─ login.html
│  ├─ page2_availability.html
│  ├─ page3_planner.html
│  └─ page4_result.html
└─ screenshots/
```
## Prerequisites
1. Python 3.x
2. Flask
3. Pandas
## Installation
1. Clone the repository or open the project folder in VS Code.
2. Install the required packages:
   pip install flask pandas

## How It Works
1. Open the login page.
2. Enter student details.
3. Select your available days, weeks, and months.
4. Choose the subject and topics you want to study.
5. Generate the final study plan.
6. View the result page with the planned schedule.

## Usage
Start the application using:
python app.py

Then open the local address shown in the terminal, usually:
http://127.0.0.1:5000/

## Future Improvements
1. Add user authentication
2. Improve UI design
3. Support multiple subjects
4. Allow exporting the study plan as PDF
5. Save plans in a database
6. Add reminders and notifications

## Author
Sangtina Jagtiani
Data Science Student
