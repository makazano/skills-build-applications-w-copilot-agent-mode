from rest_framework import serializers

from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ["id", "activity_type", "duration_minutes", "performed_at"]

    def get_id(self, obj):
        return str(obj.id)
