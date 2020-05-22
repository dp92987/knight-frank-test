create table metros
(
    id   serial  not null
        constraint metros_pkey
            primary key,
    name varchar not null
);