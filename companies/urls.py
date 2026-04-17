from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('image-capture/', views.image_capture, name='image_capture'),
    path('learning/', views.learning, name='learning'),
    path('notes/', views.notes, name='notes'),
    path('summarization/', views.summarization, name='summarization'),
    path('text-input/', views.text_input, name='text_input'),
    path('text-processing/', views.text_processing, name='text_processing'),
]