from django.conf import settings
from django.db import models
class Question(models.Model):
    TOPIC_CHOICES=[("dsa","Data Structures & Algorithms"),("python","Python"),("sql","SQL"),("oops","Object-Oriented Programming"),("dbms","DBMS"),("os","Operating Systems"),("networking","Computer Networks"),("aptitude","Aptitude"),("hr","HR"),("theory","Other Theory"),("other","Other")]
    DIFFICULTY_CHOICES=[("easy","Easy"),("medium","Medium"),("hard","Hard")]
    text=models.TextField()
    normalized_text=models.TextField(db_index=True)
    topic=models.CharField(max_length=30,choices=TOPIC_CHOICES,default="other")
    difficulty=models.CharField(max_length=10,choices=DIFFICULTY_CHOICES,default="medium")
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["-created_at"]
    def __str__(self): return self.text[:100]
class QuestionReport(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="reports")
    interview_round=models.ForeignKey("experiences.InterviewRound",on_delete=models.CASCADE,related_name="question_reports")
    reported_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="question_reports")
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=["question","interview_round","reported_by"],name="unique_question_report_per_round_user")]
