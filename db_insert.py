import re

def emoji_insert(cursor, data):
    sql = """INSERT INTO EMOJI VALUES (DEFAULT, ?, ?)"""
    cursor.executemany(sql, [(col['hexcode'], col['label']) for col in data if (not re.match(r"^[^가-힣]*$", col['label']) or col['label']=='DNA')])
    cursor.commit()
    return