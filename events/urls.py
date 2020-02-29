from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.EventsList.as_view(),name='events'),
    path('<int:pk>/', views.EventDetail.as_view(), name='event_details'),
    path('single', views.single, name='single')
]



