from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/<str:id>', views.dashboard, name='dashboard'),
]
