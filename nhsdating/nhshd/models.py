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
    personal_words = models.TextField(blank=True)
    favourite_words = models.TextField(blank=True)

    healthcare_location = models.ManyToManyField('HealthcareLocation', null=True)
    primary_condition = models.ForeignKey('Condition', related_name="primary_condition", null=True)
    other_conditions = models.ManyToManyField('Condition', related_name="other_condition", null=True)
    life_plan = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    favourite_things = models.TextField(blank=True, help_text='IGNORE THIS FIELD PLZ')
    other_things = models.TextField(blank=True)
    interets = models.TextField(blank=True)
    religion = models.TextField(blank=True)
    preocupations = models.TextField(blank=True)
    what_im_looking_for = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.user.username)


class Message(models.Model):
    sender = models.ForeignKey('auth.User', related_name="sent_messages")
    receiver = models.ForeignKey('auth.User', related_name="received_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    read_flag = models.BooleanField(default=False)
    body = models.TextField()

    @property
    def sender_photo(self):
        if self.sender.patient_set:
            return self.sender.patient_set.all()[0].photo
        else:
            return None

    def __unicode__(self):
        return u"%s -> %s { %s }" % (self.sender, self.receiver, self.body)

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
    image_url = models.URLField(null=True)
