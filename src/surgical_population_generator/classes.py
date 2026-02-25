from dataclasses import dataclass


@dataclass
class Diagnosis:
    name: str
    ICD: str
    description: str
    occurances: int
    LoS: float
    male_percent: int
    age_distribution: dict