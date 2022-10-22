# import psycopg2
# from psycopg2 import sql
# from dotenv import load_dotenv
# import os


# load_dotenv()

# configs = {
#     'host': os.environ.get('DB_HOST'),
#     'database': os.environ.get('DB_NAME'),
#     'user': os.environ.get('DB_USER'),
#     'password': os.environ.get('DB_PWD')
# }


# conn = psycopg2.connect(**configs)

# class Anime:
    
#     fields = ['id', 'anime', 'released_date', 'seasons']

#     def __init__(self, 
#         anime: str, 
#         released_date: str, 
#         seasons: int
#     ):
#         self.anime = anime.title()
#         self.released_date = released_date
#         self.seasons = seasons


#     def create_table():
#         conn = psycopg2.connect(**configs)

#         cur = conn.cursor()

#         query = """
#             CREATE TABLE IF NOT EXISTS animes (
#                 id BIGSERIAL PRIMARY KEY,
#                 anime VARCHAR(100) NOT NULL UNIQUE,
#                 released_date DATE NOT NULL,
#                 seasons INTEGER NOT NULL
#             );   
#         """

#         cur.execute(query)
#         conn.commit()
#         cur.close()
#         conn.close()

    
#     def create_animes(self):
#         conn = psycopg2.connect(**configs)
#         cur = conn.cursor()

#         print(self)

#         columns = [sql.Identifier(key) for key in self.__dict__.keys()]
#         values = [sql.Literal(value) for value in self.__dict__.values()]

#         query = sql.SQL(
#             """
#                 INSERT INTO
#                     animes (id, {columns})
#                 VALUES
#                     (DEFAULT, {values})
#                 RETURNING *
#             """).format(columns=sql.SQL(',').join(columns),
#                         values=sql.SQL(',').join(values))
            
#         print(query.as_string(cur))

#         cur.execute(query)

#         results = cur.fetchone()

#         conn.commit()
#         cur.close()
#         conn.close()

#         serialized = dict(zip(self.fields, results))

#         return serialized


#     @staticmethod
#     def get_animes():
#         conn = psycopg2.connect(**configs)

#         cur = conn.cursor()

#         query = """
#             SELECT *
#             FROM animes;
#         """

#         cur.execute(query)

#         results = cur.fetchall()

#         conn.commit()
#         cur.close()
#         conn.close()

#         print(results)

#         return results

#     @staticmethod
#     def get_animes_by_id(id):

#         conn = psycopg2.connect(**configs)
#         cur = conn.cursor()

#         cur.execute("""
#             SELECT *
#             FROM animes
#             WHERE id=(%s);
#         """, (id, ))

#         result = cur.fetchone()
#         print(result)

#         conn.commit()
#         cur.close()
#         conn.close()

#         fields = ['id', 'anime', 'released_date', 'seasons']

#         serialized = dict(zip(fields, result))

#         return serialized

#     def delete(id):
#         conn = psycopg2.connect(**configs)
#         cur = conn.cursor()

#         cur.execute("""
#             DELETE FROM
#                 animes
#             WHERE
#                 id=(%s)
#             RETURNING *;""", (id, ))

#         result = cur.fetchone()

#         conn.commit()
#         cur.close()
#         conn.close()

#         fields = ['id', 'anime', 'released_date', 'seasons']

#         serialized = dict(zip(fields, result))

#         return serialized

#     def update(id, data):
#         conn = psycopg2.connect(**configs)
#         cur = conn.cursor()

#         columns = [sql.Identifier(key) for key in data.keys()]
#         values = [sql.Literal(value) for value in data.values()]

#         query = sql.SQL(
#             """
#                 UPDATE
#                     animes
#                 SET
#                     ({columns}) = row({values})
#                 WHERE
#                     id={id}
#                 RETURNING *
#             """).format(id=sql.Literal(str(id)),
#                         columns=sql.SQL(',').join(columns),
#                         values=sql.SQL(',').join(values))

#         print(query.as_string(cur))

#         cur.execute(query)

#         result = cur.fetchone()

#         conn.commit()
#         cur.close()
#         conn.close()

#         if not result:
#             return {"error": "Not found"}, 404

#         fields = ['id', 'anime', 'released_date', 'seasons']

#         serialized = dict(zip(fields, result))

#         return serialized