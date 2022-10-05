from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyView(ListCreateAPIView):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailView(RetrieveUpdateDestroyAPIView):

	queryset = Company.objects.all()
	serializer_class = CompanySerializer

	lookup_url_kwarg = "company_id"