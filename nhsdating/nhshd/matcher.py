from .models import Patient

def generate_matches(interests, conditions, symptoms, age_from, age_to,locations):
    matches = Patient.objects.all()
    return matches
