from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aws/', views.aws, name='aws'),
    path('docker/', views.docker, name='docker'),
    path('jenkins/', views.jenkins, name='jenkins'),
    path('kubernetes/', views.kubernetes, name='kubernetes'),
    path('monitoring/', views.monitoring, name='monitoring'),
    path('ai-assistant/', views.ai_assistant, name='ai_assistant'),
    path('security/', views.security, name='security'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]