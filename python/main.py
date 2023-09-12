import cleaning
import db
import pairs_detect


def main():
    # remove_stop_skills() # Done
    # stop_symbols() # Done
    # remove_100_percent() # Done

    find_fuzzy_pairs()


def find_fuzzy_pairs():
    skills = db.get_all_skill_with_id()
    result = pairs_detect.get_duplicate_ids_by_fuzzy(skills)
    db.add_pairs(result)

def remove_100_percent():
    skills = db.get_all_skill_with_id()
    ids_to_remove = cleaning.find_100_percent_similarity_skills(skills)
    db.set_is_deleted_minus_ids(ids_to_remove)

def stop_symbols():
    skills = db.get_all_skill_with_id()
    updated_skills = cleaning.update_skills_with_stop_symbols(skills)
    print("Updated: ", len(updated_skills))

    db.update_skills(updated_skills)

def remove_stop_skills():
    skills = db.get_all_skills_name()
    print("Общее количество навыков:", len(skills))

    skills_to_remove = cleaning.cut_minus_words(skills) # Done
    skills_to_remove += cleaning.cut_minus_skills(skills) # Done
    db.set_is_deleted_minus_names(skills_to_remove) # Done


if __name__ == "__main__":
    main()