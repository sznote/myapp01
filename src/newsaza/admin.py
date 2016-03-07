from django.contrib import admin

# Register your models here.
#from newsaza.models import SignUP

from .models import SignUP


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","fullname","timestamp"]
    class Meta:
        model = SignUP

admin.site.register(SignUP,SignUpAdmin)

