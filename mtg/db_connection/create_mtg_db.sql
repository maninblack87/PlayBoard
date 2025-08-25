create database if not exists mtg
    default character set utf8mb4
    collate utf8mb4_general_ci;

use mtg;

create table if not exists user (
    id varchar(32) primary key not null,
    pw varchar(20) not null,
    plwkr_id1 varchar(100),     -- user 아이디 뒤에 planeswalker 이름이 붙게 됨
    plwkr_id2 varchar(100),
    plwkr_id3 varchar(100),
    plwkr_id4 varchar(100),
    plwkr_id5 varchar(100),
)