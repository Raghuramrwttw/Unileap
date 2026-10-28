from django.urls import path

from . import views

app_name = "loans"

urlpatterns = [
    path("", views.loan, name="loan"),
    path("<slug:section>/", views.loan_section, name="section"),
]
