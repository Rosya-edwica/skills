import csv
from rich.progress import track
from models import Skill

STOP_SYMBOLS = {
        "*",
        "?",
        "•",
        "«",
        "»",
        "'",
        '"',
        "!"
}


def cut_minus_words(skills: list[str]) -> list[str]:
    """
    Ищет навыки в которых встречаются стоп-слова
    """
    for_remove_list = []
    minus_words = get_minus_words("../data/minus_words.csv")
    for i in track(range(len(skills))):
        skill = skills[i]
        for word in minus_words:
            if word in skill:
                for_remove_list.append(skill)
                break
    return for_remove_list


def cut_minus_skills(skills: list[str]) -> list[str]:
    """В отличие от cut_minus_skill для удаления навыка необходимо полное совпадание слова"""
    minus_skills_set = set(get_minus_words("../data/minus_skills.csv"))
    skill_set = set(i.lower().strip() for i in skills)

    for_remove_set = minus_skills_set & skill_set
    return list(for_remove_set)


def get_minus_words(path: str) -> set[str]:
    with open(path, encoding="utf-8", mode="r", newline="") as f:
        reader = csv.reader(f)
        skills = [row[0].lower().strip() for row in reader]
        return skills


def update_skills_with_stop_symbols(skills: list[Skill]) -> list[Skill]:
    updated = []
    for skill in skills:
        new_name = skill.Name
        for sym in STOP_SYMBOLS:
            new_name = new_name.replace(sym, "")
        
        if new_name != skill.Name:
            updated.append(Skill(Name=new_name, Id=skill.Id))
    return updated


def find_100_percent_similarity_skills(skills: list[Skill]) -> list[int]:
    """ стоит ли в эту проверку включать навыки с is_deleted = true? """
    duplicatesId = []
    # for index, skill_one in enumerate(skills[:-1]):
    for index in track(range(len(skills)-1)):
        skill_one = skills[index]
        for index2 in range(index+1, len(skills)):
            skill_two = skills[index2]
            if skill_one.Name.lower().strip() == skill_two.Name.lower().strip():
                duplicatesId.append(skill_two.Id)
    return duplicatesId