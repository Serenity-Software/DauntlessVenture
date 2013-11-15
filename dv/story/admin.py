"""
Admin definition for story.
"""
from django.contrib import admin
from dv.story.models import Act
from dv.story.models import Beat
from dv.story.models import Component
from dv.story.models import Episode
from dv.story.models import Program
from dv.story.models import Scene
from dv.story.models import Season


class SeasonAdmin(admin.ModelAdmin):  # pylint: disable=too-many-public-methods
    """Admin for Season records"""
    list_display = ('program', 'number', 'create_date', 'change_date')
    list_display_links = ('number',)
    list_filter = ('program', 'create_date', 'change_date')
    readonly_fields = ('create_date', 'change_date')


class SeasonInline(admin.TabularInline):
    """Inline admin for Season records"""
    model = Season
    readonly_fields = ('create_date', 'change_date')
    list_display = ('program', 'number', 'create_date', 'change_date')
    list_filter = ('program', 'create_date', 'change_date')


class ProgramAdmin(admin.ModelAdmin):  # pylint: disable=too-many-public-methods
    """Admin for Program records"""
    list_display = ('title', 'create_date', 'change_date')
    list_filter = ('create_date', 'change_date')
    search_fields = ('title',)
    readonly_fields = ('create_date', 'change_date')
    inlines = [SeasonInline, ]


admin.site.register(Program, ProgramAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Episode)
admin.site.register(Act)
admin.site.register(Scene)
admin.site.register(Beat)
admin.site.register(Component)
