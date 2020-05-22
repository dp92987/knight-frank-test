create table types
(
    id   serial  not null
        constraint types_pkey
            primary key,
    name varchar not null
);