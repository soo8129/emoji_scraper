def emoji_insert(cursor, data):
    sql = """INSERT INTO CONTENT_COMMENT VALUES (DEFAULT, ?, ?)"""
    cursor.executemany(sql, [(col['label'], col['hexcode']) for col in data])
    cursor.commit()
    return