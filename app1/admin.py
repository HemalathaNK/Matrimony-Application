from django.contrib import admin
from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'password', 'age', 'gender','height',
                    'marital_status', 'religion', 'mother_tongue', 'family_type',
                    'job_details', 'salary', 'address', 'profile_picture','video')

    # Include all fields in the form for easy editing in the admin
    fields = ('name', 'email', 'password', 'mobile', 'age', 'gender','height','marital_status',
              'religion', 'mother_tongue', 'family_type', 'job_details', 'salary',
              'address', 'profile_picture','video')

    # Allow users to search by name and email
    search_fields = ('name',)
    list_filter = ('gender', 'religion', 'job_details')

admin.site.register(Signup, SignupAdmin)
