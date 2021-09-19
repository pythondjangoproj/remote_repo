from django.contrib import admin
from marksapp.models import marks
# Register your models here.
class markadmin(admin.ModelAdmin):
    list_display=['name','marks']


admin.site.register(marks,markadmin)
