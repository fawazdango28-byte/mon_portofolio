from django.urls import path
from . import views

urlpatterns = [
    # Pages principales
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', views.contact, name='contact'),
    
    # Actions
    path('download-cv/', views.download_cv, name='download_cv'),
    
    # API endpoints
    path('api/projects/', views.projects_api, name='projects_api'),
    path('api/skills/', views.skills_api, name='skills_api'),
]