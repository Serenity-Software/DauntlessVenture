"""
Models to manage the story.

Since ultimately the purpose of this system is to tell a story, we adopted
film-making terminology: program, season, episode, act, scene, beat.
"""
from django.db import models
from jsonfield import JSONField
from django.contrib import auth


class Program(models.Model):
    """
    The Program, or series.

    A Program contains one or more Seasons.
    """
    creator_user = models.ForeignKey(auth.models.User)
    title = models.CharField(max_length=128)


class Season(models.Model):
    """
    The Program Season.

    A Season belongs to a program, and contains one or more Episodes.
    """
    series = models.ForeignKey(Program)
    number = models.IntegerField()

    # TODO: This should be a property-y method, whatever those are called.
    # I think you can do it via decorators.
    #def episode_count:


class Episode(models.Model):
    """
    The Episode.

    An Episode belongs to 1 and only 1 Season, and contains one or more Acts.
    """
    season = models.ForeignKey(Season)
    title = models.CharField(max_length=128)
    number = models.IntegerField()


class Act(models.Model):
    """
    The Act.

    An Act belongs to a single Episode, and contains one or more Scenes.
    """
    episode = models.ForeignKey(Episode)
    number = models.IntegerField()


class Scene(models.Model):
    """
    The Scene.

    A Scene belongs to a single Act, and contains one or more Beats.
    """
    act = models.ForeignKey(Act)
    number = models.IntegerField()


class Component(models.Model):
    """
    The Component.

    A Component represents a single piece of the story.  This is the part
    that the user interacts with.
    """
    name = models.CharField(max_length=32)
    class_name = models.CharField(max_length=128)
    # TODO: need to name this something that makes it clear that this is merely
    # a list of properties that need to be set
    properties = JSONField()


class Beat(models.Model):
    """
    The Beat.

    A Beat belongs to a single Scene, and contains the definition of each
    step or shot of the scene.
    """
    scene = models.ForeignKey(Scene)
    component = models.ForeignKey(Component)
    # these are the property values
    properties = JSONField()

    def validate(self):
        """
        Validates the Beat against the Component.

        Make sure the component properties match the component definition.
        """
        pass
