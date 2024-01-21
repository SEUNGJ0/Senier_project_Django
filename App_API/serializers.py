from rest_framework import serializers
from App_Main.models import Pet_diet_set, Pet_daily_feeding

class Pet_diet_setSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet_diet_set
        fields = ('id','pet_name','pet_feed_time_B','pet_feed_time_L','pet_feed_time_D','pet_feed_amount','pet_standard_feed')

class Pet_daily_feedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet_daily_feeding
        fields = '__all__'