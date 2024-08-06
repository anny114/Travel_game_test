from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['phonenum', 'gender']
        widgets = {
            'gender': forms.RadioSelect(choices=UserInfo.GENDER_CHOICES)
        }
