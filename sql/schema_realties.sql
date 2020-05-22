create table realties
(
    id      serial  not null
        constraint realties_pkey
            primary key,
    name    varchar not null,
    address varchar not null,
    floor   integer not null,
    area    numeric not null,
    type    integer not null
        constraint realties_type_fkey
            references types,
    rooms   integer not null
);