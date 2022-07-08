from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src = "{}" width = "40" style = "border-radius : 5px"/>'.format(object.photo.url))

    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'first_name',
                    'last_name', 'designation', 'created_date')
    list_display_links = ('first_name', 'id', 'thumbnail')

    search_fields = ('first_name', 'last_name', 'id', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)
