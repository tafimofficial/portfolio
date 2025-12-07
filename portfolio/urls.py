from django.urls import path
from .views import (
    home, project_detail, public_project_list, dashboard,
    project_list, project_create, project_update, project_delete,
    skill_list, skill_create, skill_update, skill_delete,
    experience_list, experience_create, experience_update, experience_delete,
    education_list, education_create, education_update, education_delete,
    social_link_list, social_link_create, social_link_update, social_link_delete,
    profile_update
)

urlpatterns = [
    path('', home, name='home'),
    path('projects/', public_project_list, name='public_project_list'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/projects/', project_list, name='project_list'),
    path('dashboard/projects/add/', project_create, name='project_create'),
    path('dashboard/projects/<int:pk>/edit/', project_update, name='project_update'),
    path('dashboard/projects/<int:pk>/delete/', project_delete, name='project_delete'),
    
    path('dashboard/skills/', skill_list, name='skill_list'),
    path('dashboard/skills/add/', skill_create, name='skill_create'),
    path('dashboard/skills/<int:pk>/edit/', skill_update, name='skill_update'),
    path('dashboard/skills/<int:pk>/delete/', skill_delete, name='skill_delete'),

    path('dashboard/experience/', experience_list, name='experience_list'),
    path('dashboard/experience/add/', experience_create, name='experience_create'),
    path('dashboard/experience/<int:pk>/edit/', experience_update, name='experience_update'),
    path('dashboard/experience/<int:pk>/delete/', experience_delete, name='experience_delete'),

    path('dashboard/education/', education_list, name='education_list'),
    path('dashboard/education/add/', education_create, name='education_create'),
    path('dashboard/education/<int:pk>/edit/', education_update, name='education_update'),
    path('dashboard/education/<int:pk>/delete/', education_delete, name='education_delete'),

    path('dashboard/socials/', social_link_list, name='social_link_list'),
    path('dashboard/socials/add/', social_link_create, name='social_link_create'),
    path('dashboard/socials/<int:pk>/edit/', social_link_update, name='social_link_update'),
    path('dashboard/socials/<int:pk>/delete/', social_link_delete, name='social_link_delete'),

    path('dashboard/profile/', profile_update, name='profile_update'),
]
