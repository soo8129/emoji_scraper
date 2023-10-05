import re

def emoji_insert(cursor, data):
    sql = """INSERT INTO CONTENT_COMMENT VALUES (DEFAULT, ?, ?)"""
    cursor.executemany(sql, [(col['label'], col['hexcode']) for col in data if (not re.match(r"^[^가-힣]*$", col['label']) or col['label']=='DNA')])
    cursor.commit()
    return