from asyncio import constants
from app.database import get_db

def scan():
    statement = "SELECT * FROM notes"
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, ())
    out = cursor.fetchall()
    cursor.close()
    return out

def select_by_id(id=1):
    statement = "SELECT * FROM notes WHERE id=?"
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, (id, ))
    out = cursor.fetchall()
    cursor.close()
    return out

def create(data):
    statement = """
        INSERT INTO notes (
            title,
            subtitle,
            body
        ) VALUES (?, ?, ?)
    """
    conn = get_db()
    conn.execute(statement, (data["title"], data["subtitle"], data["body"]))
    conn.commit()
    conn.close()

def update(data, pk):
    statement = """
        UPDATE notes
        SET title =?,
        subtitle =?,
        body =?
        WHERE id=?   
    """
    conn = get_db()
    conn.execute(statement, (data["title"], data["subtitle"], data["body"], pk))
    conn.commit()
    conn.close()

def delete(pk):
    statement = "DELETE FROM notes WHERE id=?"
    conn = get_db()
    conn.execute(statement, (pk, ))
    conn.commit()
    conn.close()
