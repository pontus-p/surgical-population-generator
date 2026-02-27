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

    def __post_init__(self):
        del self.age_distribution["NA"]
        self.male_probability = self.male_percent / 100

    def normalized_age_distribution(self):
        total_occurances = sum(v for v in self.age_distribution.values())
        ret = {}
        for k, v in self.age_distribution.items():
            ret[k] = v/total_occurances
        return ret
