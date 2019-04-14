from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.persons_list, name='person_list'),
    path('new/', views.person_new, name='newperson'),
    path('update/<int:id>/', views.person_update, name='updateperson'),
    path('delete/<int:id>/', views.person_delete, name='deleteperson'),
]