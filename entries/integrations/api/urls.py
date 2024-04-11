from django.urls import path

from .views import FormResponseAPI, TestAPI


urlpatterns = [
    path('form-response', FormResponseAPI.as_view()),
    path('tests', TestAPI.as_view()),
]