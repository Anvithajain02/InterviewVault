from rest_framework import serializers
from experiences.models import InterviewRound
from .models import Question
class QuestionSubmissionSerializer(serializers.Serializer):
    company_name=serializers.CharField(max_length=200,trim_whitespace=True)
    job_role=serializers.CharField(max_length=150,trim_whitespace=True)
    round_type=serializers.ChoiceField(choices=InterviewRound.ROUND_CHOICES)
    round_number=serializers.IntegerField(min_value=1,max_value=20)
    text=serializers.CharField(max_length=5000)
    topic=serializers.ChoiceField(choices=Question.TOPIC_CHOICES)
    difficulty=serializers.ChoiceField(choices=Question.DIFFICULTY_CHOICES)
    def validate_company_name(self,v):
        if len(v.strip())<2: raise serializers.ValidationError("Enter a valid company name.")
        return v.strip()
    def validate_job_role(self,v):
        if len(v.strip())<2: raise serializers.ValidationError("Enter a valid job role.")
        return v.strip()
    def validate_text(self,v):
        v=v.strip()
        if len(v)<5: raise serializers.ValidationError("Question must contain at least 5 characters.")
        return v
