from django.urls import path, include
from . import views

urlpatterns = [
    path('teachers/', views.TeacherList.as_view(), name='teacher-list'),
]