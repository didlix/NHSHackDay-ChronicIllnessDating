from django.db import models


def format_filename(format_string):
    """
    Takes a Django format string like

        "/a/path/{instance.lol}/"

    and returns a function for the FileField
    """
    def upload_to(instance, filename):
        return format_string.format(obj=instance, filename=filename})


class Patient(models.Model):
    pass


class Place(models.Model):
    pass


class Symptom(models.Model):
    pass


class Photo(models.Model):
    created_by = models.ForeignKey('contrib.auth.models.User')
    image = models.ImageField(upload_to=format_filename("/photos/{filename}"))
