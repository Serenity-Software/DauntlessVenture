"""Models to manage the story.

Since ultimately the purpose of this system is to tell a story, we adopted
film-making terminology: program, season, episode, act, scene, beat.
"""
from django.contrib import auth
from django.db import models
from jsonfield import JSONField


class Program(models.Model):
    """The Program, or series.

    A Program contains one or more Seasons.

    Attributes:
    """
    creator_user = models.ForeignKey(auth.models.User)
    title = models.CharField(max_length=128)


class Season(models.Model):
    """The Program Season.

    A Season belongs to a program, and contains one or more Episodes.

    Attributes:
    """
    series = models.ForeignKey(Program)
    number = models.IntegerField()

    # TODO: This should be a property-y method, whatever those are called.
    # I think you can do it via decorators.
    #def episode_count:


class Episode(models.Model):
    """The Episode.

    An Episode belongs to 1 and only 1 Season, and contains one or more Acts.

    Attributes:
    """
    season = models.ForeignKey(Season)
    title = models.CharField(max_length=128)
    number = models.IntegerField()


class Act(models.Model):
    """The Act.

    An Act belongs to a single Episode, and contains one or more Scenes.

    Attributes:
    """
    episode = models.ForeignKey(Episode)
    number = models.IntegerField()


class Scene(models.Model):
    """The Scene.

    A Scene belongs to a single Act, and contains one or more Beats.

    Attributes:
    """
    act = models.ForeignKey(Act)
    number = models.IntegerField()


class Component(models.Model):
    """The Component.

    A Component represents a single piece of the story.  This is the part
    that the user interacts with.

    Attributes:
        property_list: a dict containing the properties.
    """
    name = models.CharField(max_length=32)
    class_name = models.CharField(max_length=128)
    # TODO: this is basically a dict, but can't be stored in the DB this way.
    # What's the proper Djangoesque approach?
    # I think the actual class (as defined by class_name) should define
    # this data.  Maybe we don't need this field at all, since we can just
    # validate the class itself?
    property_list = JSONField()


class Beat(models.Model):
    """The Beat.

    A Beat belongs to a single Scene, and contains the definition of each
    step or shot of the scene.

    Attributes:
    """
    scene = models.ForeignKey(Scene)
    component = models.ForeignKey(Component)
    component_properties = JSONField(validators=[Beat.validate])

    #TODO: implement this; there's probably a correct djangoesque way to do it.
    def validate(self):
        """Validates the Beat against the Component.

        Ensures the component properties match the component definition.
        """
        pass
