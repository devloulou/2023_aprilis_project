from .config import db_config
from .postgres_service import PostgresService
from .sql_helper import (genre_cre_table,
                         movies_cre_table,
                         db_objects,
                         insert_meta,
                         insert_genre_ids,
                         select_meta,
                         delete_genre_id,
                         delete_meta)