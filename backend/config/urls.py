from django.contrib import admin
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response
class Health(APIView):
    authentication_classes=[]; permission_classes=[]
    def get(self, request): return Response({"status":"ok","service":"InterviewVault"})
urlpatterns=[path("admin/",admin.site.urls),path("api/health/",Health.as_view()),path("api/auth/",include("accounts.urls")),path("api/questions/",include("questions.urls")),path("api/companies/",include("companies.urls"))]
