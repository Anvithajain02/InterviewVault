from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer
class CompanyListAPIView(generics.ListAPIView):
    serializer_class=CompanySerializer
    queryset=Company.objects.all()
    pagination_class=None
