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
