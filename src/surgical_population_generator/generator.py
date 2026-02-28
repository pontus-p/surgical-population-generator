from classes import Diagnosis, Patient
from pprint import pprint
import random
from distributions.distributions_data import diagnosis_dict
from distributions.patient_names import patient_names

def generate_population(n: int, diags: list, random_sample=False):
    """Generates n Patient class with a primary diagnosis based on diagnosis probability.
    Result follow the distribution deterministically.
    Rounding errors in small sets are added in based on the probability distribution.
    If random_sample is True, all individuals are sampled randomly.
    """
    probs = [d.probability for d in diags]
    if random_sample:
        population = random.choices(diags, weights=probs, k=n)
    else:
        population = []
        for d in diags:
            for _ in range(int(d.probability*n)):
                population.append(d)
        patients_to_add_in = n - len(population)
        population.extend(random.choices(diags, weights=probs, k=patients_to_add_in))
        print("added in random patients: ", patients_to_add_in)
        assert n == len(population)
    patient_population = []
    for d in population:
        gender = select_gender(d)
        name = select_name(gender)
        age = select_age(d)
        LoS = select_LoS(d)
        patient_population.append(Patient(name, age, gender, d, LoS))
    return patient_population


def select_gender(diag: Diagnosis):
    if random.random() < diag.male_probability:
        return "male"
    return "female"

def select_name(gender: str):
    return random.choice(patient_names[gender])

def select_age(diag: Diagnosis):
    age_distribution = diag.normalized_age_distribution()
    age_span = random.choices(list(age_distribution.keys()), age_distribution.values(), k=1)[0]
    if age_span == "90+":
        return random.randint(90, 99)
    if age_span == "0-17":
        return random.randint(16, 17)
    lo, hi = [int(x) for x in age_span.split("-")]
    return random.randint(lo, hi)

def select_LoS(diag: Diagnosis):
    return diag.LoS

def create_patients(n: int, random_sample=False):
    patient_population = generate_population(n, diags, random_sample=random_sample)
    # TODO: formatera det som en string som ska till botten.

diags = []
for k, v in diagnosis_dict.items():
    diags.append(Diagnosis(**v))

sum_individuals = sum(diag.occurances for diag in diags)
for d in diags:
    d.probability = d.occurances / sum_individuals

output_string = create_patients(10, random_sample=False)
