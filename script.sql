create table alembic_version
(
    version_num varchar(32) not null
        constraint alembic_version_pkc
            primary key
);

alter table alembic_version
    owner to wm;

create table "user"
(
    id            serial
        primary key,
    username      varchar(64)  not null
        unique,
    email         varchar(120) not null
        unique,
    password_hash varchar(500)
);

alter table "user"
    owner to wm;

create table crypto_holding
(
    id             serial
        primary key,
    user_id        integer          not null
        references "user",
    crypto_symbol  varchar(10)      not null,
    quantity       double precision not null,
    purchase_price double precision not null
);

alter table crypto_holding
    owner to wm;

create table mutual_fund_holding
(
    id             serial
        primary key,
    user_id        integer          not null
        references "user",
    fund_symbol    varchar(10)      not null,
    quantity       integer          not null,
    purchase_price double precision not null
);

alter table mutual_fund_holding
    owner to wm;

create table stock_holding
(
    id             serial
        primary key,
    user_id        integer          not null
        references "user",
    stock_symbol   varchar(10)      not null,
    quantity       integer          not null,
    purchase_price double precision not null
);

alter table stock_holding
    owner to wm;


