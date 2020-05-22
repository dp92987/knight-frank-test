create table realty_metros
(
    id        serial not null
        constraint realty_metros_pkey
            primary key,
    realty_id integer
        constraint realty_metros_realty_id_fkey
            references realties,
    metro_id  integer
        constraint realty_metros_metro_id_fkey
            references metros
);