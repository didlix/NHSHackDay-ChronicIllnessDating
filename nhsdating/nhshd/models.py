from django.db import models


def format_filename(format_string):
    """
    Takes a Django format string like

        "/a/path/{instance.lol}/"

    and returns a function for the FileField
    """
    def upload_to(instance, filename):
        return format_string.format(obj=instance, filename=filename)
    return upload_to


class Patient(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(null=True, max_length=200)
    gender = models.FloatField(default=0.5)
    age = models.IntegerField(null=True)

    photo = models.ForeignKey('Photo')

    locations = models.ManyToManyField('Place')
    symptoms = models.ManyToManyField('Symptom')
    interests = models.ManyToManyField('Interest')

    personal_words = models.TextField()
    favourite_words = models.TextField()


class Place(models.Model):
    name = models.CharField(max_length=200)


class Interest(models.Model):
    name = models.CharField(max_length=200)


class Symptom(models.Model):
    name = models.CharField(max_length=200)


class Photo(models.Model):
    created_by = models.ForeignKey('auth.User')
    image = models.FileField(upload_to=format_filename("/photos/{filename}"))
