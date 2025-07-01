from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_view, name='login'),
    path('add-student/', views.add_student, name='addStudent'),
    path('home/', views.home_view, name='getInfo'),
    path('update/<str:id>/', views.update_view, name='update'),
    path('delete/<str:id>/', views.delete_view, name='delete'),
    path('logout/', views.logout_view, name='logout'),
]
