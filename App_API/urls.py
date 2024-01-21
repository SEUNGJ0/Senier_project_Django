from django.urls import path
from .views import PetDietSetList, PetDailyFeedingList_Page, PetDailtFeedingList_ALL


urlpatterns = [
    path('diet-set', PetDietSetList.as_view(), name='pet-diet-set-list'),
    path('daily-feeding', PetDailyFeedingList_Page.as_view(), name='pet-daily-feeding-list_page'),
    path('daily-feeding-all',PetDailtFeedingList_ALL.as_view(), name='pet-daily-feeding-list_all')
]