from .models import Patient

def _pks(models):
    return [model.pk for model in models]

def sort_matches(matches, interests, conditions, symptoms, age_from, age_to, locations):

    def sort_key(p):
        pc = p.primary_condition.name in conditions if conditions else None
        c = p.other_conditions.filter(pk__in=_pks(conditions)).count() if conditions else None
        s = p.symptoms.filter(pk__in=_pks(symptoms)).count() if symptoms else None
        i = p.interests.filter(pk__in=_pks(interests)).count() if interests else None
        l = p.locations.filter(pk__in=_pks(locations)).count() if locations else None

        return (
            p.age >= int(age_from) and p.age <= int(age_to),
            l,
            pc,
            c,
            s,
            i
        )

    return sorted(matches, key=sort_key, reverse=True)
