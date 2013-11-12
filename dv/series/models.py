from django.db import models
from django.contrib import auth


class Series(models.Model):
    """
    """
    creator_user = models.ForeignKey(auth.models.User)
    title = models.CharField(max_length=128)


class Season(models.Model):
    """
    """
    series = models.ForeignKey(Series)
    number = models.IntegerField()

    # TODO: This should be a property-y method, whatever those are called.
    # I think you can do it via decorators.
    #def episode_count:


class Episode(models.Model):
    """
    """
    season = models.ForeignKey(Season)
    title = models.CharField(max_length=128)
    number = models.IntegerField()


class Act(models.Model):
    """
    """
    episode = models.ForeignKey(Episode)
    number = models.IntegerField()


class Scene(models.Model):
    """
    """
    act = models.ForeignKey(Act)
    number = models.IntegerField()


class ComponentType(models.Model):
    """
    """
    name = models.CharField(max_length=32)
    class_name = models.CharField(max_length=128)
    # need to name this something that makes it clear that this is merely a
    # list of properties that need to be set
    # TODO: properties = JSONField()


class Component(models.Model):
    """
    """
    scene = models.ForeignKey(Scene)
    component_type = models.ForeignKey(ComponentType)
    # these are the property values
    # TODO: properties = models.JSONField()

    def validate(self):
        """
        Make sure the component properties match the component_type definition.
        """
        pass
