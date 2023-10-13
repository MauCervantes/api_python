from db.db import connect
from models.Helado import Helado

cur = connect.cursor(dictionary=True)

def new(new_helado):
    query = "insert into helado (id, name, flavor) values (null, %s, %s)"
    vals = (new_helado.name, new_helado.flavor)
    cur.execute(query, vals)
    return cur

def view():
    query = "select * from helado"
    cur.execute(query)
    return cur