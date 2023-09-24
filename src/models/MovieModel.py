from database.db import get_connection
from .entities.Movie import Movie

class MovieModel():

    @classmethod 
    def get_movies(self):
        try:
            connection=get_connection()
            movies=[]

            with connection.cursor () as cursor:
                cursor.execute("SELECT id, title, duration, released FROM movie ORDER BY title ASC")
                resultset=cursor.fetchall()

                for row in resultset:
                    movie=Movie(row[0],row[1],row[2],row[3])
                    movie.append(movie)
            connection.close
            return movies
        except Exception as ex:
            print(ex)
            raise Exception(ex)