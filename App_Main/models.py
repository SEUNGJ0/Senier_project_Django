from django.db import models
from App_User.models import User

pet_status_choices = [
    ('성견__중성화', "Adult_Neutering"),
    ('성견__미중성화', 'Adult_NonNeutering'),
    ('성견__비만경향', 'Adult_Obese_NonActive'),
    ('성견__활동적', 'Adult_Active'),
    ('성견__매우 활동적', 'Adult_Very_Active'),
    ('성견__체중감량', 'Adult_Wloss'),
    ('성견__체중증가', 'Adult_gain'),
    ('성견__아픔', 'Adult_Week'),
    ('성장기__생후 4개월 전', 'Growth_Ud4'),
    ('성장기__4개월 이후 ~ 성견 전', 'Growth_Up4'),
    ('임신 전반 6주', 'Pregent_6W'),
    ('임신 전반 3주', 'Pregent_3W'),
    ('수유 1마리', 'Nursing_1'),
    ('수유 2마리', 'Nursing_2'),
    ('수유 3~4마리', 'Nursing_3_4'),
    ('수유 5~6마리', 'Nursing_5_6'),
    ('수유 7~8마리', 'Nursing_7_8'),
    ('수유 9마리 이상', 'Nursing_9')
]

class Pet_info(models.Model):
    pet_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    pet_name = models.CharField(max_length = 100)
    pet_birth = models.DateField(null = True, blank = True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        # 객체를 출력할 떄 나타날 값
        return self.pet_name

class Pet_diet_set(models.Model):

    pet_name = models.ForeignKey(Pet_info, on_delete = models.CASCADE)

    pet_weight = models.DecimalField(decimal_places=2, max_digits = 100)
    pet_feed_Kcal = models.IntegerField()
    pet_status = models.CharField(max_length=100, choices = pet_status_choices ,verbose_name="반려견 상태")
    
    pet_feed_time_B = models.TimeField()
    pet_feed_time_L = models.TimeField()
    pet_feed_time_D = models.TimeField(null=True, blank = True)
    
    pet_needKcal = models.IntegerField(verbose_name="하루 필요 칼로리")
    pet_feed_amount = models.IntegerField(verbose_name="사료 총량")

class Pet_daily_feed(models.Model):
    pet_name = models.ForeignKey(Pet_info, on_delete = models.CASCADE)

    Daily_date = models.DateField(verbose_name = "날짜")
    Daily_feed = models.IntegerField(verbose_name = '지급된 사료량')
    Remain_feed = models.IntegerField(verbose_name = "남은 사료량", null = True)

    def __str__(self):
    # 객체를 출력할 떄 나타날 값
        return f"{self.Daily_date} 지급 일지"    