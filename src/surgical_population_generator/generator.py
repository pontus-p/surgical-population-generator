from classes import Diagnosis
from pprint import pprint
import random
from distributions.distributions_data import diagnosis_distributions

def generate_diagnosis_probabilities(diags: list):
    sum_individuals = sum(diag.occurances for diag in diags)
    ret = {}
    for diag in diags:
        ret[diag.ICD] = diag.occurances / sum_individuals
    return ret

def generate_population(n: int, diagnosis_probabilities: dict, random_sample=False):
    """Generates n individuals with a primary diagnosis given a diagnosis probability distribution.
    Result follow the distribution deterministically.
    Rounding errors in small sets are added in based on the probability distribution.
    If random_sample is True, all individuals are sampled randomly.
    """
    diags = list(diagnosis_probabilities.keys())
    probs = list(diagnosis_probabilities.values())
    if random_sample:
        return random.choices(diags, weights=probs, k=n)

    distributed_diagnosis_list = []
    for diag, p in diagnosis_probabilities.items():
        for _ in range(int(p*n)):
            distributed_diagnosis_list.append(diag)
    patients_to_add_in = n - len(distributed_diagnosis_list)
    distributed_diagnosis_list.extend(random.choices(diags, weights=probs, k=patients_to_add_in))
    assert n == len(distributed_diagnosis_list)
    return distributed_diagnosis_list


diags = []
for k, v in diagnosis_distributions.items():
    diags.append(Diagnosis(**v))

# pprint(generate_diagnosis_probabilities(diags))
diagnosis_probabilities = generate_diagnosis_probabilities(diags)
x = (generate_population(10, diagnosis_probabilities, random_sample=False))
print(len(x))

