import sqlite3


class Database:
    def __init__(self, database):
        self.db = sqlite3.connect(database)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.__init_movies()
        self.__init_projections()
        self.__init_reservations()

    def show_movies(self):
        query = """
            SELECT id, name
            FROM movies
            ORDER BY rating DESC
        """
        return self.cursor.execute(query).fetchall()

    def show_movie_projection(self, movie_id, date=None):
        query = """
            SELECT type, date, time
            FROM projections
            WHERE movie_id = ?
        """
        if date is not None:
            query += """
                AND date = ?
            """
            return self.cursor.execute(query, movie_id, date).fetchall()
        else:
            return self.cursor.execute(query, movie_id).fetchall()

    def make_reservation(self, movie_name, number_of_tickets):
        pass

    def cancel_reservation(self, name):
        pass
