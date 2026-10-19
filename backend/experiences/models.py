from django.conf import settings
from django.db import models
from companies.models import Company
class InterviewExperience(models.Model):
    candidate=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="interview_experiences")
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name="experiences")
    job_role=models.CharField(max_length=150)
    interview_date=models.DateField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=["candidate","company","job_role"],name="unique_candidate_company_role")]
    def __str__(self): return f"{self.candidate} - {self.company} ({self.job_role})"
class InterviewRound(models.Model):
    ROUND_CHOICES=[("online_assessment","Online Assessment"),("technical","Technical"),("technical_1","Technical Round 1"),("technical_2","Technical Round 2"),("hr","HR"),("managerial","Managerial"),("system_design","System Design"),("other","Other")]
    experience=models.ForeignKey(InterviewExperience,on_delete=models.CASCADE,related_name="rounds")
    round_number=models.PositiveIntegerField(default=1)
    round_type=models.CharField(max_length=30,choices=ROUND_CHOICES)
    notes=models.TextField(blank=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=["experience","round_number"],name="unique_round_number_per_experience")]
    def __str__(self): return f"{self.experience} - Round {self.round_number}"
