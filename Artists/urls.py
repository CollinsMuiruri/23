from django.urls import path
from . import views

urlpatterns=[
    path('', views.ArtistList.as_view(), name='artists'),
    path('<int:pk>/', views.ArtistDetails.as_view(), name='artist_details')
]