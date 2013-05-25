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
    gender = models.CharField(max_length=200)
    age = models.IntegerField(null=True)

    photo = models.ForeignKey('Photo', null=True)

    locations = models.ManyToManyField('Place', null=True)
    symptoms = models.ManyToManyField('Symptom', null=True)
    interests = models.ManyToManyField('Interest', null=True)
    personal_words = models.TextField()
    favourite_words = models.TextField()

    healthcare_location = models.ManyToManyField('HealthcareLocation', null=True)
    primary_condition = models.ForeignKey('Condition')
    other_conditions = models.ManyToManyField('Condition')
    life_plan = models.TextField()
    skills = models.TextField()
    favourite_things = models.TextField()
    music = models.TextField()
    books = models.TextField()
    films = models.TextField()
    food = models.TextField()
    other_things = models.TextField()
    interets = models.TextField()
    religion = models.TextField()
    preocupations = models.TextField()
    what_im_looking_for = models.TextField()


class Place(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


class HealthcareLocation(models.Model):
    name = models.CharField(max_length=200)


class Interest(models.Model):
    name = models.CharField(max_length=200)


class Symptom(models.Model):
    name = models.CharField(max_length=200)


class Condition(models.Model):
    name = models.CharField(max_length=200)


class Photo(models.Model):
    created_by = models.ForeignKey('auth.User')
    image = models.FileField(upload_to=format_filename("/photos/{filename}"))
