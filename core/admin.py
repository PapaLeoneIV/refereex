from django.contrib import admin
from .models import League, Team

class TeamInline(admin.TabularInline):
    model = Team
    extra = 1  # Number of blank forms

class LeagueAdmin(admin.ModelAdmin):
    inlines = [TeamInline]

admin.site.register(League, LeagueAdmin)
admin.site.register(Team)  # Optional: if you want Team to also have a separate admin page

