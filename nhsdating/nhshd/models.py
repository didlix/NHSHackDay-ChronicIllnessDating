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

    photo = models.ForeignKey('Photo', null=True, blank=True)

    locations = models.ManyToManyField('Place', null=True)
    symptoms = models.ManyToManyField('Symptom', null=True)
    interests = models.ManyToManyField('Interest', null=True)
    personal_words = models.TextField()
    favourite_words = models.TextField()

    healthcare_location = models.ManyToManyField('HealthcareLocation', null=True)
    primary_condition = models.ForeignKey('Condition', related_name="primary_condition", null=True)
    other_conditions = models.ManyToManyField('Condition', related_name="other_condition", null=True)
    life_plan = models.TextField(null=True)
    skills = models.TextField(null=True)
    favourite_things = models.TextField(null=True)
    music = models.TextField(null=True)
    books = models.TextField(null=True)
    films = models.TextField(null=True)
    food = models.TextField(null=True)
    other_things = models.TextField(null=True)
    interets = models.TextField(null=True)
    religion = models.TextField(null=True)
    preocupations = models.TextField(null=True)
    what_im_looking_for = models.TextField(null=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.user.username)

class Place(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class HealthcareLocation(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Photo(models.Model):
    created_by = models.ForeignKey('auth.User')
    image = models.FileField(upload_to=format_filename("/photos/{filename}"))
