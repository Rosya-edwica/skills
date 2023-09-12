from db import connect_to_mysql
from models import Pair

def add_pairs(pairs: list[Pair]):
    groups = group_pairs(pairs)
    conn = connect_to_mysql()
    cursor = conn.cursor()
    query = "INSERT IGNORE INTO demand_duplicate_gpt(demand_id, dup_demand_id, similarity) VALUES(%s, %s, %s)"

    for group in groups:
        cursor.executemany(query, group)
        
    conn.commit()
    conn.close()

def group_pairs(pairs: list[Pair], size: int = 1000) -> list[list[Pair]]:
    groups = []
    for index in range(0, len(pairs), size):
        group = pairs[index:][:size]
        groups.append(group)
    return groups