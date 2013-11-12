from django.contrib import admin
from dv.series.models import Series
from dv.series.models import Season
from dv.series.models import Episode
from dv.series.models import Act
from dv.series.models import Scene
from dv.series.models import Component
from dv.series.models import ComponentType

admin.site.register(Series)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Act)
admin.site.register(Scene)
admin.site.register(Component)
admin.site.register(ComponentType)
