from django.urls import path
from . import views

urlpatterns = [
    path('personal-card/', views.create_or_get_personal_card, name='create_or_get_personal_card'),
    path('vaccination-detail/', views.create_vaccination_detail, name='create_vaccination_detail'),
    path('personal-cards/', views.list_personal_cards, name='list_personal_cards'),
    path('personal-card/<int:pk>/', views.personal_card_detail, name='personal_card_detail'),
    path('check-vaccination/<int:person_id>/<str:vaccination_name>/', views.check_vaccination_validity, name='check_vaccination_validity'),
]
