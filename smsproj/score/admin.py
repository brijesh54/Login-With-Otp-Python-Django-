from django.contrib import admin
from .models import Score

# Register your models here.

@admin.register(Score)
class ScoreModelAdmin(admin.ModelAdmin):
    list_display = ['id','result']
