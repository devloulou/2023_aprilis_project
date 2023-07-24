create table docker_test_table(
    id serial primary key,
    name text,
    age integer,
    load_date date default now()
);


insert into docker_test_table (name, age) values ('Ricsi', 33);
insert into docker_test_table (name, age) values ('Ricsi', 33);
insert into docker_test_table (name, age) values ('Ricsi', 33);
insert into docker_test_table (name, age) values ('Ricsi', 33);
insert into docker_test_table (name, age) values ('Ricsi', 33);
insert into docker_test_table (name, age) values ('Ricsi', 33);
insert into docker_test_table (name, age) values ('Ricsi', 33);
insert into docker_test_table (name, age) values ('Ricsi', 33);
insert into docker_test_table (name, age) values ('Ricsi', 33);

commit;