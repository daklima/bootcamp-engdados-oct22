from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql+psycopg2://root:root@localhost/test_db')

sql='''
select * from first_appearences_artist
'''

df = pd.read_sql_query(sql, engine)
df.head()

##############################################

sql_insert = '''
insert into tb_acdc (
select "date"
    ,"rank"
    ,artist
    ,song
from public.billboard
where artist = 'Nirvana'
order by artist, song, "date"
);
'''

engine.execute(sql_insert)