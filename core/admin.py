from django.contrib import admin
from .models import Video, Tag
# Register your models here.

admin.site.register(Video)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}