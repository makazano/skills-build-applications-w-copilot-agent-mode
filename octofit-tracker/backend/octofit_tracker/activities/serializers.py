from rest_framework import serializers


from .models import Activity, User, Team, Workout, Leaderboard



class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "name", "email", "team"]

    def get_id(self, obj):
        return str(obj.id)


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ["id", "name", "members"]

    def get_id(self, obj):
        return str(obj.id)


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ["id", "user", "activity_type", "duration_minutes", "performed_at"]

    def get_id(self, obj):
        return str(obj.id)


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ["id", "name", "description"]

    def get_id(self, obj):
        return str(obj.id)


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ["id", "user", "score"]

    def get_id(self, obj):
        return str(obj.id)
