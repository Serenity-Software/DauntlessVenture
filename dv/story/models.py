"""Models to manage the story.

Since ultimately the purpose of this system is to tell a story, we adopted
film-making terminology: program, season, episode, act, scene, beat.

TODO: make the change_date fields update on record change
"""
from django.contrib import auth
from django.db import models
from django.utils import timezone
from jsonfield import JSONField


class Program(models.Model):
    """The Program, or series.

    A Program contains one or more Seasons.

    Attributes:
    """
    creator_user = models.ForeignKey(auth.models.User)
    title = models.CharField(max_length=128)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    change_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return unicode(self.title)


class Season(models.Model):
    """The Program Season.

    A Season belongs to a program, and contains one or more Episodes.

    Attributes:
    """
    program = models.ForeignKey(Program)
    number = models.IntegerField()
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    change_date = models.DateTimeField(default=timezone.now)

    # TODO: This should be a property-y method, whatever those are called.
    # I think you can do it via decorators.
    #def episode_count:

    def __unicode__(self):
        return unicode(self.number)


class Episode(models.Model):
    """The Episode.

    An Episode belongs to 1 and only 1 Season, and contains one or more Acts.

    Attributes:
    """
    season = models.ForeignKey(Season)
    number = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    change_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return unicode(self.title)


class Act(models.Model):
    """The Act.

    An Act belongs to a single Episode, and contains one or more Scenes.

    Attributes:
    """
    episode = models.ForeignKey(Episode)
    number = models.IntegerField()
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    change_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return unicode(self.number)


class Scene(models.Model):
    """The Scene.

    A Scene belongs to a single Act, and contains one or more Beats.

    Attributes:
    """
    act = models.ForeignKey(Act)
    number = models.IntegerField()
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    change_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return unicode(self.number)


class Component(models.Model):
    """The Component.

    A Component represents a single piece of the story.  This is the part
    that the user interacts with.

    Attributes:
        name:
        class_name:
        property_list: a dict containing the properties.
    """
    name = models.CharField(max_length=32)
    class_name = models.CharField(max_length=128)


class Beat(models.Model):
    """The Beat.

    A Beat belongs to a single Scene, and contains the definition of each
    step or shot of the scene.

    Attributes:
    """
    scene = models.ForeignKey(Scene)
    component = models.ForeignKey(Component)
    name = models.CharField(max_length=128)
    description = models.TextField()
    component_properties = JSONField()
    create_date = models.DateTimeField(default=timezone.now)
    change_date = models.DateTimeField(default=timezone.now)

    #TODO: implement this; there's probably a correct djangoesque way to do it.
    def validate(self):
        """Validates the Beat against the Component.

        Ensures the component properties match the component definition.
        """
        pass


class InputComponent(Component):
    """Component to handle input of any type.

    Attributes:
    """
    name = ''
