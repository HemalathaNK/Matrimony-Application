from django import forms
from .models import Signup


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['name', 'email','mobile', 'age', 'gender', 'height', 'marital_status',
                  'religion', 'mother_tongue', 'family_type', 'job_details', 'salary',
                  'address', 'profile_picture','video']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['name', 'email', 'mobile', 'age', 'gender', 'height', 'marital_status',
                  'religion', 'mother_tongue', 'family_type', 'job_details', 'salary',
                  'address', 'profile_picture', 'video']


