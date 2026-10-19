from rest_framework import serializers
from .models import Question
class QuestionSerializer(serializers.ModelSerializer):
    report_count=serializers.IntegerField(read_only=True)
    companies=serializers.SerializerMethodField()
    class Meta:
        model=Question
        fields=["id","text","topic","difficulty","report_count","companies","created_at"]
    def get_companies(self,obj):
        return list(obj.reports.select_related("interview_round__experience__company").values_list("interview_round__experience__company__name",flat=True).distinct())
