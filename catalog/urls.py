from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("study-destinations/", views.destinations, name="destinations"),
    path("study-destinations/<slug:slug>/", views.destination_detail, name="destination"),
    path("compare-destinations/", views.compare, name="compare"),
    path("universities-courses/", views.universities, name="universities"),
    path("universities-courses/<slug:slug>/", views.university_detail, name="university"),
    path("courses/", views.courses, name="courses"),
    path("top-universities/", views.top_universities, name="top_universities"),
    path("popular-courses/", views.popular_courses, name="popular_courses"),
]
