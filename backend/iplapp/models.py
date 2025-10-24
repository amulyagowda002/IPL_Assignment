from django.db import models

class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    city = models.CharField(max_length=200, null=True)
    team1 = models.CharField(max_length=200)
    team2 = models.CharField(max_length=200)
    winner = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f'Match {self.id} - {self.season}'

class Delivery(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=200)
    bowling_team = models.CharField(max_length=200)
    over = models.IntegerField()
    ball = models.IntegerField()
    bowler = models.CharField(max_length=200)
    total_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=200, null=True)