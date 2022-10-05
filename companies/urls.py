from django.urls import path

from companies.views import CompanyView, CompanyDetailView

urlpatterns = [
    path("companies/", CompanyView.as_view()),
    path("companies/<uuid:company_id>/", CompanyDetailView.as_view()),
]
