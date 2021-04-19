from django.contrib import admin
from .models import *


class SecondaryImageInline(admin.TabularInline):
    model = ProjectSecondaryImage
    extra = 3


class ProjectsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['main_image']}),
        ('Content', {'fields': ['name']}),
        (None,      {'fields': ['description']}),
        ('Date',    {'fields': ['date']}),
    ]
    inlines = [SecondaryImageInline]


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ProjectSecondaryImage)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Messages)



