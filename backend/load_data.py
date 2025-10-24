import os
import django
import pandas as pd
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from iplapp.models import Match, Delivery

# Clear old data
Match.objects.all().delete()
Delivery.objects.all().delete()
print("🧹 Cleared existing records...")

# ✅ Update the paths below — your CSVs are in backend/data/
base_path = os.path.join(os.getcwd(), 'data')

matches_path = os.path.join(base_path, 'matches.csv')
deliveries_path = os.path.join(base_path, 'deliveries.csv')

# --- Load matches.csv ---
print("📂 Loading matches.csv...")
matches_df = pd.read_csv(matches_path)

for _, row in matches_df.iterrows():
    Match.objects.create(
        id=int(row['id']),
        season=int(row['season']),
        city=row.get('city'),
        date=datetime.strptime(str(row['date']), '%Y-%m-%d').date() if pd.notnull(row.get('date')) else None,
        team1=row['team1'],
        team2=row['team2'],
        winner=row.get('winner')
    )

print(f"✅ Loaded {len(matches_df)} matches successfully!")

# --- Load deliveries.csv ---
print("📂 Loading deliveries.csv...")
deliveries_df = pd.read_csv(deliveries_path)

batch = []
for _, row in deliveries_df.iterrows():
    batch.append(Delivery(
        match_id=int(row['match_id']),
        inning=row['inning'],
        batting_team=row['batting_team'],
        bowling_team=row['bowling_team'],
        over=row['over'],
        ball=row['ball'],
        bowler=row['bowler'],
        total_runs=row['total_runs'],
        extra_runs=row['extra_runs'],
        player_dismissed=row.get('player_dismissed')
    ))

Delivery.objects.bulk_create(batch)
print(f"✅ Loaded {len(batch)} deliveries successfully!")

print("🎉 Data loading complete!")
