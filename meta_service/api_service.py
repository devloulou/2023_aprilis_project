import tmdbsimple as tmdb

class ApiService:
    tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'
    web_url = "https://image.tmdb.org/t/p/original"

    def __init__(self):
        self.search = tmdb.Search()

    def get_meta_data(self, movie):
        data = self.search.movie(query=movie)['results']
        if not data:
            print(f'Nincs ilyen adat az adatbázisban: {movie}')
            return {}
        
        return data[0]
    
    def get_image_url(self, poster_path):
        from urllib.request import urlopen
        return urlopen(self.web_url + poster_path)
    

if __name__ == '__main__':
    api = ApiService()
    # elvárt működés tesztelése -> 'Happy Path' tesztelés

    for item in ['Vukk', 'Prey', 'Predator']:
        movie = api.get_meta_data(item)
        
        if not movie.get('poster_path'):
            print(f'Nincs poster_path: {item}')
            continue

        url = api.get_image_url(movie['poster_path'])
        # ide jön a json kiírás
        # ide jön a képkiírás