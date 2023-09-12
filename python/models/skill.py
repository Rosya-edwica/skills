from typing import NamedTuple

class Skill(NamedTuple):
    Id: int
    Name: str

class Pair(NamedTuple):
    SkillIDOne: int
    SkillIDTwo: int
    Similarity: int 