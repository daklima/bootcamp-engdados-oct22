select 
	b.artist
	,b.song
	,count(*) as qtd_musica
from public.billboard as b
where b.artist = 'Chuck Berry'
group by 1,2
order by 3 desc
