from psycopg2 import sql
from .run_sql import run_sql

class Anime:
    
    fields = ['id', 'anime', 'released_date', 'seasons']

    def __init__(self, 
        anime: str, 
        released_date: str, 
        seasons: int
    ):
        self.anime = anime.title()
        self.released_date = released_date
        self.seasons = seasons


    def create_table():

        query = """
            CREATE TABLE IF NOT EXISTS anime (
                id BIGSERIAL PRIMARY KEY,
                anime VARCHAR(100) NOT NULL UNIQUE,
                released_date DATE NOT NULL,
                seasons INTEGER NOT NULL
            );   
        """

        run_sql(query)   

    
    def create_animes(self):

        columns = [sql.Identifier(key) for key in self.__dict__.keys()]
        values = [sql.Literal(value) for value in self.__dict__.values()]

        print(columns,"columns")
        print(values,"values")

        query = sql.SQL(
            """
                INSERT INTO
                    anime (id, {columns})
                VALUES
                    (DEFAULT, {values})
                RETURNING *
            """).format(columns=sql.SQL(',').join(columns),
                        values=sql.SQL(',').join(values))
            
        run_sql(query,'fetchone')

        results_return = run_sql(query,'fetchone')

        serialized = dict(zip(self.fields, results_return))

        return serialized


    @staticmethod
    def get_animes():

        query = """
            SELECT *
            FROM anime;
        """

        get = run_sql(query,'fetchall')

        return get

    @staticmethod
    def get_animes_by_id(id):

        query = """
            SELECT *
            FROM anime
            WHERE id=(%s);
        """, (id, )

        results_return = run_sql(query,'fetchone')
        print(results_return)

        fields = ['id', 'anime', 'released_date', 'seasons']

        serialized = dict(zip(fields, results_return))

        return serialized

    def delete_anime(id):
       
        query = """
            DELETE FROM
                anime
            WHERE
                id=(%s)
            RETURNING *;""", (id, )

        results_return = run_sql(query,'fetchone')

        fields = ['id', 'anime', 'released_date', 'seasons']
        print('results_return',results_return)
        serialized = dict(zip(fields, results_return))

        return serialized

    def update_anime(id, data):

        columns = [sql.Identifier(key) for key in data.keys()]
        values = [sql.Literal(value) for value in data.values()]

        query = sql.SQL(
            """
                UPDATE
                    anime
                SET
                    ({columns}) = row({values})
                WHERE
                    id={id}
                RETURNING *
            """).format(id=sql.Literal(str(id)),
                        columns=sql.SQL(',').join(columns),
                        values=sql.SQL(',').join(values))


        run_sql(query,'fetchone')

        results_return = run_sql(query,'fetchone')

        if not results_return:
            return {"error": "Not found"}, 404

        fields = ['id', 'anime', 'released_date', 'seasons']

        serialized = dict(zip(fields, results_return))

        return serialized