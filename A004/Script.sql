--create table clientes (
--	id serial not null,
--	nome varchar(250) not null,
--	idade integer,
--	primary key (id)
--);

create table public.billboard (
	"date" date null,
	"rank" int4 null,
	song varchar(300) null,
	artist varchar(300) null,
	"last-week" int4 null,
	"peak-rank" int4 null,
	"weeks-on-board" int4 null
);
-----

select *
from public.billboard
limit 100;
-----

create table first_appearences as (
	with first_appearence_artist as (
		select "date"
			,artist
			,"rank"
			,row_number() over(partition by artist order by "date") as row_num_by_artist
		from public.billboard
		order by artist, "date"
	)
	select 
		"date"
		,artist
		,"rank"
	from first_appearence_artist
	where row_num_by_artist = 1
);

select * from first_appearences;

drop table if exists tb_acdc;
create table tb_acdc as (
	select "date"
		,"rank"
		,artist
		,song
	from public.billboard
	where artist = 'AC/DC'
	order by artist, song, "date"
);

select * from tb_acdc

create view first_appearences_artist as (
	with first_appearence_artist as (
		select "date"
			,artist
			,"rank"
			,row_number() over(partition by artist order by "date") as row_num_by_artist
		from tb_acdc
		order by artist, "date"
	)
	select 
		"date"
		,artist
		,"rank"
	from first_appearence_artist
	where row_num_by_artist = 1
);

select * from first_appearences_artist;

insert into tb_acdc (
	select "date"
		,"rank"
		,artist
		,song
	from public.billboard
	where artist = 'Arctic Monkeys'
	order by artist, song, "date"
);

select * from first_appearences_artist;