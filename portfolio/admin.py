from django.contrib import admin
from .models import Contact, Project, Skill


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    readonly_fields = ['created_at']
    search_fields = ['name', 'email', 'subject']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technology', 'created_at']
    search_fields = ['title', 'technology']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']
