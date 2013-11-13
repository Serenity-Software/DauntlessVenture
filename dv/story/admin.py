"""
Admin definition for story.
"""
from django.contrib import admin
from dv.story.models import Program
from dv.story.models import Season
from dv.story.models import Episode
from dv.story.models import Act
from dv.story.models import Scene
from dv.story.models import Beat
from dv.story.models import Component

admin.site.register(Program)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Act)
admin.site.register(Scene)
admin.site.register(Beat)
admin.site.register(Component)
