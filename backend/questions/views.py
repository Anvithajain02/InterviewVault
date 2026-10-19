from django.db import transaction
from django.db.models import Count,Q
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from companies.models import Company
from experiences.models import InterviewExperience,InterviewRound
from .models import Question,QuestionReport
from .serializers import QuestionSerializer
from .services import normalize_question
from .submission_serializers import QuestionSubmissionSerializer
class QuestionListAPIView(generics.ListAPIView):
    serializer_class=QuestionSerializer
    pagination_class=None
    def get_queryset(self):
        qs=Question.objects.annotate(report_count=Count("reports",distinct=True)).prefetch_related("reports__interview_round__experience__company")
        search=self.request.query_params.get("search","").strip()
        company=self.request.query_params.get("company","").strip()
        topic=self.request.query_params.get("topic","").strip().lower()
        difficulty=self.request.query_params.get("difficulty","").strip().lower()
        sort=self.request.query_params.get("sort","frequency").strip().lower()
        if search: qs=qs.filter(Q(text__icontains=search)|Q(topic__icontains=search))
        if company:
            if company.isdigit(): qs=qs.filter(reports__interview_round__experience__company_id=int(company))
            else: qs=qs.filter(reports__interview_round__experience__company__name__icontains=company)
        if topic and topic!="all": qs=qs.filter(topic=topic)
        if difficulty and difficulty!="all": qs=qs.filter(difficulty=difficulty)
        qs=qs.distinct()
        if sort=="newest": return qs.order_by("-created_at","-id")
        if sort=="difficulty": return qs.order_by("difficulty","-report_count","-created_at")
        return qs.order_by("-report_count","-created_at","-id")
class QuestionSubmitAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    @transaction.atomic
    def post(self,request):
        s=QuestionSubmissionSerializer(data=request.data); s.is_valid(raise_exception=True); d=s.validated_data
        company=Company.objects.filter(name__iexact=d["company_name"]).first()
        if company is None: company=Company.objects.create(name=d["company_name"])
        experience,_=InterviewExperience.objects.get_or_create(candidate=request.user,company=company,job_role=d["job_role"])
        round_obj,_=InterviewRound.objects.get_or_create(experience=experience,round_number=d["round_number"],defaults={"round_type":d["round_type"]})
        if round_obj.round_type!=d["round_type"]: return Response({"detail":"That round number already has a different round type."},status=400)
        normalized=normalize_question(d["text"])
        question=Question.objects.filter(normalized_text=normalized,topic=d["topic"]).first()
        duplicate=question is not None
        if question is None: question=Question.objects.create(text=d["text"],normalized_text=normalized,topic=d["topic"],difficulty=d["difficulty"])
        report,created=QuestionReport.objects.get_or_create(question=question,interview_round=round_obj,reported_by=request.user)
        if not created: return Response({"detail":"You already submitted this question for this round."},status=409)
        return Response({"message":"Question submitted successfully.","question_id":question.id,"report_id":report.id,"duplicate_match":duplicate},status=201)
class QuestionStatsAPIView(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self,request):
        from companies.models import Company
        return Response({"questions":Question.objects.count(),"companies":Company.objects.count(),"reports":QuestionReport.objects.count()})
