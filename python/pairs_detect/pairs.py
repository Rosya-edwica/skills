from fuzzywuzzy import fuzz
from models import Skill, Pair
from rich.progress import track

def get_duplicate_ids_by_fuzzy(skills: list[Skill]) -> list[Pair]:
    pairs = []
    for index in track(range(len(skills)-1)):
        skill_one = skills[index]
        for index2 in range(index+1, len(skills)):
            skill_two = skills[index2]
            similarity = fuzz.WRatio(skill_one.Name, skill_two.Name)
            if similarity > 90:
                pairs.append(Pair(skill_one.Id, skill_two.Id, similarity))
    return pairs