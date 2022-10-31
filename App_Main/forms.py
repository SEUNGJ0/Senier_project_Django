from django import forms
from .models import *

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet_info  # 사용할 모델
        fields = ['pet_name', 'pet_birth', 'pet_weight', 'pet_race']  # PetForm에서 사용할 Board 모델의 속성