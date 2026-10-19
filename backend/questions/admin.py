from django.contrib import admin
from .models import Question,QuestionReport
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['id','text','topic','difficulty','created_at']
    list_filter=['topic','difficulty']
    search_fields=['text','normalized_text']
@admin.register(QuestionReport)
class QuestionReportAdmin(admin.ModelAdmin):
    list_display=['question','interview_round','reported_by','created_at']
