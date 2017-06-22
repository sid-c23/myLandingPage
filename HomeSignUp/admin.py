from django.contrib import admin
from .models import SignUp
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_name', 'timestamp']
    class Meta:
        model = SignUp


admin.site.register(SignUp, SignUpAdmin)