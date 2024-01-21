from django.urls import path
from .views import PetDietSetList, PetDailyFeedingList


urlpatterns = [
    path('diet-set', PetDietSetList.as_view(), name='pet-diet-set-list'),
    path('daily-feeding', PetDailyFeedingList.as_view(), name='pet-daily-feeding-list'),
]