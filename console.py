from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository 
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()


artist1 = Artist("Drake")
artist_repository.save(artist1)
artist2 = Artist("Giveon")
artist_repository.save(artist2)
artist3 = Artist("Khalid")
artist_repository.save(artist3)

album1 = Album("Wings", "K-POP", artist1)
album_repository.save(album1)
album2 = Album("Astro World", "Rap", artist2)
album_repository.save(album2)
album3 = Album("Recovery", "Rap", artist3)
album_repository.save(album3)

result = artist_repository.select(25)
print(result.name)

result = album_repository.select(19)
print(result.title)

artists_results = artist_repository.select_all()

for artist in artists_results:
    print(artist.name)

album_results = album_repository.select_all()


for album in album_results:
    print(album.title)


