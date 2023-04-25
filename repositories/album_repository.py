from db.run_sql import run_sql

from models.album import Album #  ADDED
from models.artist import Artist
import repositories.artist_repository as artist_repo

def select_all():
    albums = []
    sql = "SELECT * FROM album"
    results = run_sql(sql)

    for row in results:
        artist = artist_repo.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row ['id'])
        albums.append(album)
    return albums




def save(album):
    sql = "INSERT INTO album (title, genre, artist_id) VALUES (%s,%s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    rows = run_sql(sql, values)
    id = rows[0]['id'] 
    album.id = id 
    return album

def delete_all():
    sql = "DELETE  FROM album"
    run_sql(sql)


def select(id):
    album = None
    sql = "SELECT * FROM album WHERE id = %s"
    values = [id]


    rows = run_sql(sql, values)
    # could also have len(rows)> 0
    if rows:
        album_info = rows[0]
        artist = artist_repo.select(album_info['artist_id'])
        album = Album(album_info['title'], album_info['genre'], artist, album_info['id'])

    return album



