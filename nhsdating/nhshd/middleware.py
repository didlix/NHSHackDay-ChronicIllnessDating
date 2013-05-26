from django.contrib.auth.models import User


class Didlix(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            request.user = User.objects.get(username='didlix')
