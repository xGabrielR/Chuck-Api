from sqlalchemy import create_engine
from databases import Database

def create_table(con):
    query_create_table = """
    create table joke (
        categories TEXT, 
        created_at TEXT, 
        joke_id TEXT, 
        updated_at TEXT, 
        value TEXT
    );
    """.replace('\n', '')

    con.exec_driver_sql(query_create_table)


#db = create_engine("sqlite:////home/grc/arep/api/chuck_api/database.sqlite")
#con = db.connect()

database = Database("sqlite:////home/grc/arep/api/chuck_api/database.sqlite")


#r = con.exec_driver_sql('select * from joke limit 1')
#print(r.fetchall())

#r = con.exec_driver_sql('select distinct categories from joke where categories is not null')
#print(r.fetchall())

#r = con.exec_driver_sql('select * from joke order by random() limit 1')
#print(r.fetchone()._mapping)

#with open("/home/grc/arep/api/chuck_api/sample_data_insert/sample.sql", "r") as f:
#    lines = f.readlines()

#f = open("/home/grc/arep/api/chuck_api/sample_data_insert/sample.sql", "r")
#lines = f.readlines()
#f.close()

#for line in lines:
#    con.exec_driver_sql(line)
#    con.commit()