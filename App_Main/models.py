from django.db import models
from django.urls import reverse
from App_User.models import User
 
class Pet_info(models.Model):
    pet_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    pet_name = models.CharField(max_length = 100)
    pet_birth = models.DateField(null = True, blank = True)
    pet_weight = models.DecimalField(decimal_places=2, max_digits = 100)
    pet_race = models.CharField(max_length = 100, verbose_name="견종")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        # 객체를 출력할 떄 나타날 값
        return self.pet_name

class Pet_diet_set(models.Model):
    pet_name = models.ForeignKey(Pet_info, on_delete = models.CASCADE)

    pet_breed = models.CharField(max_length=100)
    pet_diet = models.IntegerField(verbose_name="식단")
    
    pet_feed_time_B = models.TimeField()
    pet_feed_time_L = models.TimeField()
    pet_feed_time_D = models.TimeField()
    pet_feed_amount = models.IntegerField(verbose_name="먹이 총량")

class Pet_daily_feed(models.Model):
    pet_name = models.ForeignKey(Pet_info, on_delete = models.CASCADE)
    Daily_date = models.DateField(verbose_name = "날짜")
    Daily_feed = models.IntegerField(verbose_name = '지급된 사료량')
    Remain_feed = models.IntegerField(verbose_name = "남은 사료량", null = True)

    def __str__(self):
    # 객체를 출력할 떄 나타날 값
        return f"{self.Daily_date} 지급 일지"    