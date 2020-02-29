from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'', views.safaricom, name='safaricom'),
    re_path(r'^create_payment/', views.create_payment, name='create_payment'),
    re_path(r'^verify_payment/$', views.verify_payment, name='verify_payment'),

]
