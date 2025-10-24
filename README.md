# 🏏 IPL Statistics Dashboard

A Django-based IPL data visualization app built using **Google Charts** and real **Kaggle IPL dataset**.

## 📊 Features
- Matches played per year
- Matches won by each team
- Real IPL dataset integrated using Django ORM
- Simple and clean visualization using Google Charts

## ⚙️ Tech Stack
- Python 3.11
- Django 5.x
- Pandas
- Google Charts

## 🧩 Setup Instructions
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python load_data.py
python manage.py runserver
