from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from App_Main.models import Pet_diet_set, Pet_daily_feeding, Pet_info
from App_API.serializers import *
from App_API.pagination import PaginationHandlerMixin

class PetPagination(PageNumberPagination):
    page_size_query_param = 'limit'

class PetDietSetList(APIView):
    def get(self, request):
        pet_name = Pet_info.objects.get(pet_owner = request.user)
        dietsetting = Pet_diet_set.objects.filter(pet_name = pet_name)
        serializers = Pet_diet_setSerializer(dietsetting, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
class PetDailyFeedingList(APIView, PaginationHandlerMixin):
    pagination_class = PetPagination
    serializer_class = Pet_daily_feedingSerializer
    def get(self, request):
        pet_name = Pet_info.objects.get(pet_owner = request.user)
        instance = Pet_daily_feeding.objects.filter(pet_name = pet_name)
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Pet_daily_feedingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)