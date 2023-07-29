from collections import OrderedDict

movies_cre_table = f"""
create table meta(
adult boolean,
backdrop_path varchar(50),
id integer primary key,
original_language varchar(3),
original_title varchar(50),
overview text,
popularity decimal,
poster_path varchar(50) ,
release_date date ,
title varchar(50) ,
video boolean,
vote_average decimal,
vote_count integer
)
"""
genre_cre_table = f"""
create table genre_ids (
meta_id integer,
genre_id integer,
constraint fk_meta_id
foreign key (meta_id)
references meta(id)
)
"""

db_objects = OrderedDict({
    "tables": {
        "meta": movies_cre_table,
        "genre_ids": genre_cre_table
    }
})

insert_meta = """
insert into meta
    (adult,
    backdrop_path,
    id,
    original_language,
    original_title,
    overview,
    popularity,
    poster_path,
    release_date,
    title,
    video,
    vote_average,
    vote_count)
values (
    :adult,
    :backdrop_path,
    :id,
    :original_language,
    :original_title,
    :overview,
    :popularity,
    :poster_path,
    :release_date,
    :title,
    :video,
    :vote_average,
    :vote_count
)
"""

insert_genre_ids = """
insert into genre_ids (
    meta_id,
    genre_id)
values (
    :meta_id,
    :genre_id
)
"""

select_meta = """
select original_title from meta
"""

delete_genre_id = """
delete from genre_ids gi where exists
(select id from meta m where original_title = '{movie}'
and gi.meta_id = m.id)
"""

delete_meta = """
delete from meta where original_title = '{movie}'
"""