import tmdbsimple as tmdb

from meta_service import ApiService, FileService, MOVIES_PATH
from meta_service.db_service import (PostgresService,
                                     db_objects,
                                     db_config,
                                     insert_meta,
                                     insert_genre_ids,
                                     select_meta,
                                     delete_genre_id,
                                     delete_meta)


def download_meta():
    url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['db']}"
    file = FileService()
    api = ApiService(tmdb.Search())
    sql = PostgresService(url)

    movies = file.get_data_from_folder(MOVIES_PATH)
    meta = [item[0] for item in sql.run_query(select_meta, True).fetchall()]

    # adatbázisból kell a metaadatokat lekérdezni mind a 2 esetben: letöltés és törlés
    need_to_delete = [item for item in meta if item not in movies]
    need_to_download = [item for item in movies if item not in meta]

    for item in need_to_delete:
        # json_path = f"{file.meta_folder}/{item}.json"
        image_path = f"{file.poster_folder}/{item}.jpg"

        # adatbázisból töröljük az adatokat, nem a JSON-t töröljük
        sql.run_query(delete_genre_id.format(movie=item))
        sql.run_query(delete_meta.format(movie=item))
        # file.remove_file(json_path)
        file.remove_file(image_path)

    for item in need_to_download:
        movie = api.get_meta_data(item)
        # adatbázisba való betölsének itt a helye
        sql.insert_data(insert_meta, movie)
        
        ids = []

        for _ in movie['genre_ids']:
            ids.append({
                "meta_id": movie['id'],
                "genre_id": _
            })

        sql.insert_data(insert_genre_ids, ids)

        # a posterek és a meta adatok nem tudnak egymásról: ezen dolgozzunk

        image_path = f"{file.poster_folder}/{item}.jpg"
        image_url = api.get_image_url(movie['poster_path'])

        file.write_image(image_path=image_path, image_url=image_url)

if __name__ == '__main__':
    download_meta()
