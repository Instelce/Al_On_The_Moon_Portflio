from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name="home"),
    path('projet/<int:project_id>/<str:project_name>', views.project_detail, name="project_detail"),
    path('tous_les_projets/', views.all_projects, name="all_projects"),
    path('merci/', views.thanks_messages)
]