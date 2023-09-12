from db import connect_to_mysql
from models import Skill
from rich.progress import track


def get_all_skills_name() -> list[str]:
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM demand WHERE is_deleted IS FALSE and (type_group='навык' or is_custom is true)")
    skills = [row[0].lower() for row in cursor.fetchall()]
    conn.close()
    return skills


def set_is_deleted_minus_names(skills: list[str]):
    skills_to_query = ",".join((f"'{i}'" for i in skills))
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE demand SET is_deleted=true WHERE lower(name) IN ({skills_to_query})")
    conn.commit()
    conn.close()

def set_is_deleted_minus_ids(ids: list[int]):
    skills_to_query = ",".join((str(i) for i in ids))
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE demand SET is_deleted=true WHERE id IN ({skills_to_query})")
    conn.commit()
    conn.close()

def get_all_skill_with_id() -> list[Skill]:
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM demand WHERE is_deleted IS FALSE")
    skills = [Skill(*row) for row in cursor.fetchall()]
    conn.close()
    return skills

def update_skills(skills: list[Skill]):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    for i in track(range(len(skills)), description="Updating..."):
        skill = skills[i]
        cursor.execute(f"UPDATE demand SET name='{skill.Name}' WHERE id={skill.Id}")
    conn.commit()
    conn.close()

