from .models import Patient

def generate_matches(interests, conditions, symptoms, age_from, age_to, locations):
    matches = Patient.objects.all()

    def sort_key(p):
        pc = p.primary_condition.name in conditions if conditions else None
        c = p.other_conditions.filter(name__in=conditions).count() if conditions else None
        s = p.symptoms.filter(name__in=symptoms).count() if symptoms else None
        i = p.interests.filter(name__in=interests).count() if interests else None
        l = p.locations.filter(name__in=locations).count() if locations else None

        return (
            p.age >= int(age_from) and p.age <= int(age_to),
            l,
            pc,
            c,
            s,
            i
        )

    return sorted(matches, key=sort_key, reverse=True)
