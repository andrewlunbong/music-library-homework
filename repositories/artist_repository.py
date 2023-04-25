from db.run_sql import run_sql
from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artist (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artist"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'] )
        artists.append(artist)
    return artists

def delete_all():
    sql = "DELETE  FROM artist"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artist WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'])
    return artist
