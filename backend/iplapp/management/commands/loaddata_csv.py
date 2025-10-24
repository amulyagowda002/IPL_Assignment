# management command to load matches.csv and deliveries.csv into DB
import csv, os
from django.core.management.base import BaseCommand
from iplapp.models import Match, Delivery
from django.db import transaction

class Command(BaseCommand):
    help = 'Load matches.csv and deliveries.csv from backend/data/'

    def handle(self, *args, **options):
        BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        matches_file = os.path.join(BASE, 'matches.csv')
        deliveries_file = os.path.join(BASE, 'deliveries.csv')
        if not os.path.exists(matches_file) or not os.path.exists(deliveries_file):
            self.stdout.write(self.style.ERROR('CSV files not found in backend/data/. Place matches.csv and deliveries.csv there.'))
            return
        with transaction.atomic():
            Match.objects.all().delete()
            Delivery.objects.all().delete()
            # load matches
            import pandas as pd
            mdf = pd.read_csv(matches_file)
            for _, row in mdf.iterrows():
                Match.objects.create(id=int(row['id']), season=int(row['season']), city=row.get('city'),
                                     team1=row.get('team1'), team2=row.get('team2'), winner=row.get('winner'),
                                     date=row.get('date'))
            self.stdout.write(self.style.SUCCESS(f'Loaded {len(mdf)} matches'))
            ddf = pd.read_csv(deliveries_file)
            for _, row in ddf.iterrows():
                match_id = int(row['match_id'])
                match = Match.objects.filter(id=match_id).first()
                if not match: continue
                Delivery.objects.create(match=match, inning=int(row['inning']), batting_team=row['batting_team'],
                                        bowling_team=row['bowling_team'], over=int(row['over']), ball=int(row['ball']),
                                        bowler=row['bowler'], total_runs=int(row['total_runs']), extra_runs=int(row['extra_runs']),
                                        player_dismissed=row.get('player_dismissed'))
            self.stdout.write(self.style.SUCCESS(f'Loaded {len(ddf)} deliveries'))