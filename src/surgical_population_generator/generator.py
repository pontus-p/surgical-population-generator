from classes import Diagnosis
from distributions.distributions_data import diagnosis_distributions

diags = []
for k, v in diagnosis_distributions.items():
    diags.append(Diagnosis(**v))

print(diags)