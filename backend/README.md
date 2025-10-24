IPL Project - Backend + Frontend scaffold
----------------------------------------
This scaffold provides:
 - A Django backend with APIs to support the requested analyses.
 - A React frontend skeleton (in frontend/) with pages placeholder for charts.

IMPORTANT:
 - Download the Kaggle IPL dataset (matches.csv and deliveries.csv) and place them in backend/data/
 - Install Python dependencies listed in backend/requirements.txt
 - For frontend, run `npm install` in frontend/ and then `npm start`

Backend quick start (Linux / WSL / Mac):
  cd backend
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  python manage.py migrate
  # place matches.csv and deliveries.csv into backend/data/
  python manage.py loaddata_csv
  python manage.py runserver

The backend exposes endpoints under /api/ for:
  - /api/matches_per_year/
  - /api/stacked_wins/
  - /api/extra_runs/<year>/
  - /api/top_bowlers/<year>/
  - /api/played_vs_won/<year>/

Frontend:
  - frontend/ contains a React scaffold with pages Home.js, Charts.js and README instructions.
  - It uses Chart.js via react-chartjs-2 in the scaffold (install in frontend).

This scaffold is meant to save you time; fill in UI styling or extend logic as needed.