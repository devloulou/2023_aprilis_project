import tmdbsimple as tmdb

from meta_service import ApiService
from meta_service import FileService
from meta_service import MOVIES_PATH

def download_meta():
    file = FileService()
    api = ApiService(tmdb.Search())

    movies = file.get_data_from_folder(MOVIES_PATH)

    for item in movies:
        movie = api.get_meta_data(item)
        
        json_path = f"{file.meta_folder}/{item}.json"
        file.write_json_data(data=movie, json_path=json_path)

        image_path = f"{file.poster_folder}/{item}.jpg"
        image_url = api.get_image_url(movie['poster_path'])

        file.write_image(image_path=image_path, image_url=image_url)

if __name__ == '__main__':
    download_meta()
