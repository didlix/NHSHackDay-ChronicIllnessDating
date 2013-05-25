import datetime
from haystack import indexes
from nhshd.models import Patient

class NHSHD(indexes.SearchIndex, indexes.Indexable):
    text            = indexes.CharField(document=True, use_template=True)
    name            = indexes.CharField(model_attr='name')
    gender          = indexes.CharField(model_attr='gender')
    age             = indexes.CharField(model_attr='age')
    locations       = indexes.CharField(model_attr='locations')
    symptoms        = indexes.CharField(model_attr='symptoms')
    interests       = indexes.CharField(model_attr='interests')
    personal_words  = indexes.CharField(model_attr='personal_words')
    favourite_words = indexes.CharField(model_attr='favourite_words')
    
    def get_model(self):
        return Patient

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter()