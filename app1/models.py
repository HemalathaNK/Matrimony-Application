from django.contrib.auth.models import User
from django.db import models

class Signup(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile_edit')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100,null=False)
    mobile = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'),('Other','Other')])
    height = models.CharField(max_length=10,null=True)
    marital_status = models.CharField(max_length=20)
    religion = models.CharField(max_length=50)
    mother_tongue = models.CharField(max_length=50)
    family_type = models.CharField(max_length=50)
    job_details = models.TextField()
    salary = models.CharField(max_length=100)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='image/', null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True)


    def __str__(self):
        return self.name
