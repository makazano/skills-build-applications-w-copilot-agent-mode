from django.test import TestCase



from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test User", email="test@example.com", team="marvel")
        self.assertEqual(user.name, "Test User")


class TeamModelTestCase(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="marvel", members=["Test User"])
        self.assertEqual(team.name, "marvel")


class ActivityModelTestCase(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="Test User", activity_type="Running", duration_minutes=30)
        self.assertEqual(activity.activity_type, "Running")


class WorkoutModelTestCase(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Strength", description="Strength training")
        self.assertEqual(workout.name, "Strength")


class LeaderboardModelTestCase(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user="Test User", score=100)
        self.assertEqual(lb.score, 100)
