from django.contrib import admin
from .models import Worksite, WorksiteImage

class WorksiteImageInline(admin.TabularInline):
    model = WorksiteImage
    extra = 1

class WorksiteAdmin(admin.ModelAdmin):
    inlines = [WorksiteImageInline]

admin.site.register(Worksite, WorksiteAdmin)
admin.site.register(WorksiteImage)
