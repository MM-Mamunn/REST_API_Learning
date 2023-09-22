from django.contrib import admin

# Register your models here.
from .models import database 

@admin.register(database)
class databaseAdmin(admin.ModelAdmin):
    list_display=['id','teacher_name','course_name','course_duration','seat']