from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('hello/', views.hello_view, name='hello'),
    path('student_form/', views.student_form, name='student_form'),
]

