import sqlite3

def read_db(): 
    con = None
    try:
        con = sqlite3.connect('Kinolar.db')
        kino_db = '''
           SELECT * FROM MOUVE
        '''
        cur = con.cursor()
        cur.execute(kino_db)
        red = cur.fetchall()
        cur.close()
        return red
    except sqlite3.Error as eror:
        print(eror)
    finally:
        if con:
            con.close()
            
            print('good')

kod = 14423
for i in read_db():
    if kod == i[0]:
        print(i[3])



def add_movie(id,name,des,url): 
    con = None
    try:
        con = sqlite3.connect('Kinolar.db')
        kino_db = '''
            INSERT INTO MOUVE (
            ID,NAME,DESCRIPTION,URL
            ) VALUES(?, ?, ?, ?)
        '''
        cur = con.cursor()
        cur.execute(kino_db,(id,name,des,url))
        con.commit()
        cur.close()
    except sqlite3.Error as eror:
        print(eror)
    finally:
        if con:
            con.close()
            
            print('good')

# add_movie(12345,'kulgu','comedy','https://t.me/c/2129717515/3')








# try:
#     con = sqlite3.connect('Kinolar.db')
#     kino_db = '''
#     CREATE TABLE MOUVE (
#     ID INTEGER PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     DESCRIPTION TEXT NOT NULL,
#     URL TEXT NOT NULL
#     );
#     '''
#     cur = con.cursor()
#     cur.execute(kino_db)
#     cur.close()
# except sqlite3.Error as eror:
#     print(eror)
# finally:
#     if con:
#         con.close()
        
#         print('good')