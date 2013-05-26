from .models import Patient

def generate_matches(interests, conditions, symptoms, age_from, age_to, locations):
    matches = Patient.objects.all()

    def sort_key(p):
        c = p.other_conditions.filter(name__in=conditions).count() if conditions else None
        s = p.symptoms.filter(name__in=symptoms).count() if symptoms else None
        i = p.interests.filter(name__in=interests).count() if interests else None

        return (
            p.age >= age_from and p.age <= age_to,
            c,
            s,
            i
        )

    return sorted(matches, key=sort_key)
