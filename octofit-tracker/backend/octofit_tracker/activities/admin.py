from django.contrib import admin


from .models import Activity, User, Team, Workout, Leaderboard



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "team")
    search_fields = ("name", "email", "team")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "activity_type", "duration_minutes", "performed_at")
    search_fields = ("activity_type", "user")


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "score")
    search_fields = ("user",)
