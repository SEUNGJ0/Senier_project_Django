from django import forms
from .models import *

class PetForm(forms.ModelForm):
    pet_name = forms.CharField(label='반려견 이름')
    pet_birth = forms.CharField(label='생일')
    pet_weight = forms.CharField(label='체중')
    pet_race = forms.ChoiceField(label='품종')
    class Meta:
        model = Pet_info  # 사용할 모델
        fields = ['pet_name', 'pet_birth', 'pet_weight', 'pet_race']  # PetForm에서 사용할 Board 모델의 속성