from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('<int:id>/', views.image_detail, name='image_detail'),
    path('generate/', views.generate_image, name='generate_image'),
]
