from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('learner_register/', views.learner_register, name='learner_register'),  # Add this line
    path('mentor_register/', views.mentor_register, name='mentor_register'),  # Add this line
    path('login/', views.login_view, name='login'),
]