import sqlite3
from datetime import datetime

conn = sqlite3.connect('post.sqlite3')
cursor = conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                information TEXT,
                category TEXT,
                date_post TEXT
            )
''')
conn.commit()

def load_posts(title,information,category):
    date_posted = datetime.now().strftime('%Y-%M-%D %H-%M-%S')
    cursor.execute('''
                    INSERT INTO posts(title, information, category, date_post)
                    VALUES (?, ?, ?, ?)
                    ''',(title,information,category,date_posted))
    conn.commit()

def fetch_post_by_name(title):
    cursor.execute('''
                    SELECT * FROM posts WHERE title = ?
            ''',(title,)
)
    posts =cursor.fetchone()
    return posts

sample_title = 'salom bu 1-title'
sample_information = 'salom bu 1-info'
sample_category = 'yangiliklar categoriyasi'
load_posts(sample_title,sample_information,sample_category)
fetch_post = fetch_post_by_name(sample_title)

if fetch_post:
    print('saqlangan habar')
    print('title',fetch_post[1])
    print('information',fetch_post[2])
    print('category',fetch_post[3])
    print('date',fetch_post[4])
else:
    print('Post Error')
conn.close()    