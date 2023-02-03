from django import forms
from .models import *

class PetForm(forms.ModelForm):
    pet_name = forms.CharField(error_messages={'required':'반려견의 이름을 입력해주세요!'}, label='반려견 이름')
    
    class Meta:
        model = Pet_info  # 사용할 모델
        fields = ['pet_name', 'pet_birth']

class PetdietForm(forms.ModelForm):
    pet_feed_Kcal = forms.IntegerField(label='사료 칼로리')
    pet_status = forms.ChoiceField(choices = pet_status_choices, label='반려견 상태')
    pet_weight = forms.CharField(label='체중')

    pet_feed_time_B = forms.TimeField(label='첫 번째 급여')
    pet_feed_time_L = forms.TimeField(label='두 번째 급여')


    class Meta:
        model = Pet_diet_set
        fields = ['pet_feed_Kcal','pet_status', 'pet_weight','pet_feed_time_B','pet_feed_time_L','pet_feed_time_D',]

