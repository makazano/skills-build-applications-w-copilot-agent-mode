from django.core.management.base import BaseCommand
from activities.models import Activity
from django.contrib.auth import get_user_model
from djongo import models as djongo_models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for raw collections
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Insert users
        users = [
            {"name": "Clark Kent", "email": "superman@dc.com", "team": "dc"},
            {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "dc"},
            {"name": "Diana Prince", "email": "wonderwoman@dc.com", "team": "dc"},
            {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "captain@marvel.com", "team": "marvel"},
            {"name": "Natasha Romanoff", "email": "blackwidow@marvel.com", "team": "marvel"},
        ]
        db.users.insert_many(users)

        # Insert teams
        teams = [
            {"name": "marvel", "members": ["Tony Stark", "Steve Rogers", "Natasha Romanoff"]},
            {"name": "dc", "members": ["Clark Kent", "Bruce Wayne", "Diana Prince"]},
        ]
        db.teams.insert_many(teams)

        # Insert activities
        activities = [
            {"user": "Clark Kent", "activity_type": "Flight", "duration_minutes": 60},
            {"user": "Bruce Wayne", "activity_type": "Martial Arts", "duration_minutes": 90},
            {"user": "Tony Stark", "activity_type": "Engineering", "duration_minutes": 120},
            {"user": "Steve Rogers", "activity_type": "Running", "duration_minutes": 45},
            {"user": "Diana Prince", "activity_type": "Sword Training", "duration_minutes": 80},
            {"user": "Natasha Romanoff", "activity_type": "Espionage", "duration_minutes": 100},
        ]
        db.activities.insert_many(activities)

        # Insert workouts
        workouts = [
            {"name": "Super Strength", "description": "Heavy lifting and resistance training."},
            {"name": "Agility", "description": "Parkour and acrobatics."},
        ]
        db.workouts.insert_many(workouts)

        # Insert leaderboard
        leaderboard = [
            {"user": "Clark Kent", "score": 1000},
            {"user": "Tony Stark", "score": 950},
            {"user": "Diana Prince", "score": 900},
            {"user": "Steve Rogers", "score": 850},
            {"user": "Bruce Wayne", "score": 800},
            {"user": "Natasha Romanoff", "score": 750},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
